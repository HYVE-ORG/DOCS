"""Regression checks for portable, offline documentation maintenance."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'documentacao.py'


def inventory(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='docs espaço á ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.docs = self.root / 'outputs/documentacao-software'
        self.legal = self.root / 'outputs/referencia-legal'
        self.docs.mkdir(parents=True)
        self.legal.mkdir(parents=True)
        self.write('outputs/documentacao-software/README.md',
                   '# Produto\n\nversão 0.4\nData editorial: 2026-10-22\n[Escopo](01-escopo.md)\n')
        self.write('outputs/documentacao-software/01-escopo.md',
                   '# Escopo\n\n| RF-23 | Privacidade |\n\n**RN-20:** Fontes oficiais.\n')
        self.write('outputs/documentacao-software/manifesto-documentacao.json', json.dumps({
            'required_chapters': ['01-escopo.md'],
            'required_requirements': ['RF-23', 'RN-20']}))
        self.write('outputs/referencia-legal/acervo/norma.md', '# Norma preservada\n')
        content = (self.legal / 'acervo/norma.md').read_bytes()
        self.write('outputs/referencia-legal/manifesto.json', json.dumps({'files': [{
            'path': 'acervo/norma.md', 'bytes': len(content),
            'sha256': hashlib.sha256(content).hexdigest()}]}))
        for name in ('AGENTS.md', 'LEIS.md', 'README.md', 'CLAUDE.md', 'RTK.md'):
            self.write(name, '# Instruções de teste\n')
        self.write('work/segredo.txt', 'PRIVATE BACKUP MUST NOT SHIP')
        self.write('.codex/config.toml', '[mcp_servers.example]\nurl="https://example.com"\n')
        self.assertTrue(SCRIPT.exists(), 'Portable maintenance implementation is missing')
        self.write('scripts/documentacao.py', SCRIPT.read_text(encoding='utf-8'))
        self.write('work/finalizar_documentacao.py',
                   (ROOT / 'work/finalizar_documentacao.py').read_text(encoding='utf-8'))
        self.write('tests/test_documentacao.py', Path(__file__).read_text(encoding='utf-8'))
        self.write('work/registrar_referencia_legal.ps1', '# Maintenance fixture\n')
        self.write('work/prepare_beta_repositories.py', '# Repository export fixture\n')
        self.write('outputs/referencia-legal/README.md', '# Referências\n')
        for name in ('01-brainstorming-e-design.md', '02-matriz-de-cobertura.md',
                     '03-plano-de-execucao.md', 'onboarding.md', 'quality.md',
                     'setup.md', 'avaliacao-harness.md'):
            self.write('outputs/toolkit-setup/' + name, '# Setup\n')
        self.write('outputs/toolkit-setup/document-map.json', '{}')
        spec = importlib.util.spec_from_file_location('documentation_under_test', SCRIPT)
        self.api = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.api)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def test_relocated_project_and_unrelated_cwd(self):
        result = subprocess.run([sys.executable, '-B', str(self.root / 'scripts/documentacao.py'),
                                 '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.api.check_project(self.root), [])

    def test_check_does_not_write(self):
        before = inventory(self.root)
        self.assertEqual(self.api.check_project(self.root), [])
        self.assertEqual(inventory(self.root), before)
        result = subprocess.run([sys.executable, '-B', str(self.root / 'scripts/documentacao.py'),
                                 '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(inventory(self.root), before)

    def test_missing_distribution_dependency_is_rejected(self):
        for name in ('scripts/documentacao.py', 'tests/test_documentacao.py',
                     'work/finalizar_documentacao.py', 'outputs/toolkit-setup/document-map.json'):
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_bytes()
                path.unlink()
                self.assertIn(name, '\n'.join(self.api.check_project(self.root)))
                with self.assertRaises(ValueError):
                    self.api.generate_project(self.root)
                path.write_bytes(original)

    def test_zip_metadata_is_platform_independent(self):
        text = self.api.consolidated_bytes(self.root)
        with patch('sys.platform', 'win32'):
            windows = self.api.archive_bytes(self.root, text)
        with patch('sys.platform', 'linux'):
            linux = self.api.archive_bytes(self.root, text)
        self.assertEqual(windows, linux)

    def test_missing_required_rf_fails(self):
        self.write('outputs/documentacao-software/01-escopo.md', '# Escopo\n**RN-20:** Regra\n')
        self.assertIn('RF-23', '\n'.join(self.api.check_project(self.root)))

    def test_missing_required_rn_fails(self):
        self.write('outputs/documentacao-software/01-escopo.md', '# Escopo\n| RF-23 | Requisito |\n')
        self.assertIn('RN-20', '\n'.join(self.api.check_project(self.root)))

    def test_new_contiguous_chapter_is_accepted(self):
        self.write('outputs/documentacao-software/02-novo.md', '# Novo\n')
        self.assertEqual(self.api.check_project(self.root), [])

    def test_missing_required_chapter_fails(self):
        (self.docs / '01-escopo.md').unlink()
        self.assertIn('01-escopo.md', '\n'.join(self.api.check_project(self.root)))

    def test_broken_local_link_fails(self):
        self.write('README.md', '[Erro](nao-existe.md)\n')
        self.assertIn('nao-existe.md', '\n'.join(self.api.check_project(self.root)))

    def test_fenced_example_is_not_a_real_link(self):
        self.write('README.md', '# Guia\n\n```md\n[Exemplo](inexistente.md)\n```\n')
        self.assertEqual(self.api.check_project(self.root), [])

    def test_legal_checksum_mismatch_fails(self):
        self.write('outputs/referencia-legal/acervo/norma.md', '# Norma adulterada\n')
        self.assertIn('acervo/norma.md', '\n'.join(self.api.check_project(self.root)))

    def test_manifest_escape_is_rejected(self):
        self.write('outputs/referencia-legal/manifesto.json', json.dumps({'files': [{
            'path': '../../AGENTS.md', 'bytes': 0, 'sha256': '0' * 64}]}))
        self.assertIn('fora', '\n'.join(self.api.check_project(self.root)).lower())

    def test_archive_contains_maintenance_dependencies(self):
        archive = self.api.generate_project(self.root)
        with zipfile.ZipFile(archive) as z:
            for name in ('scripts/documentacao.py', 'work/finalizar_documentacao.py',
                         'tests/test_documentacao.py', 'AGENTS.md', 'LEIS.md'):
                self.assertIn(name, z.namelist())

    def test_archive_excludes_private_state(self):
        with zipfile.ZipFile(self.api.generate_project(self.root)) as z:
            self.assertNotIn('work/segredo.txt', z.namelist())
            self.assertFalse(any(p.startswith('.codex/') for p in z.namelist()))

    def test_archive_keeps_linked_mvp_guides_without_application_or_private_files(self):
        self.write('README.md', '# Projeto\n\n[Desktop](outputs/software-mvp/docs/desktop.md)\n')
        self.write('outputs/software-mvp/docs/desktop.md', '# Desktop\n\n[Escopo](../../documentacao-software/01-escopo.md)\n')
        self.write('outputs/software-mvp/.data/segredo.md', 'Privado')
        self.write('outputs/software-mvp/.env', 'PRIVATE=value')
        self.write('outputs/software-mvp/release/segredo.md', 'Artefato privado')
        self.write('outputs/software-mvp/apps/api/src/private.ts', 'codigo')
        archive = self.api.generate_project(self.root)
        with zipfile.ZipFile(archive) as z:
            self.assertIn('outputs/software-mvp/docs/desktop.md', z.namelist())
            self.assertFalse(any(name.startswith(('outputs/software-mvp/.data/',
                                                 'outputs/software-mvp/release/',
                                                 'outputs/software-mvp/apps/api/')) or
                                 name == 'outputs/software-mvp/.env' for name in z.namelist()))
            with tempfile.TemporaryDirectory(prefix='docs com mvp ') as destination:
                z.extractall(destination)
                self.assertEqual(self.api.check_project(Path(destination)), [])

    def test_extracted_package_validates(self):
        archive = self.api.generate_project(self.root)
        with tempfile.TemporaryDirectory(prefix='pacote á ') as directory:
            with zipfile.ZipFile(archive) as z:
                z.extractall(directory)
            result = subprocess.run([sys.executable, '-B', str(Path(directory) / 'work/finalizar_documentacao.py'),
                                     '--check'], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_generation_is_repeatable(self):
        archive = self.api.generate_project(self.root)
        before = archive.read_bytes()
        self.api.generate_project(self.root)
        self.assertEqual(archive.read_bytes(), before)

    def test_invalid_sources_preserve_previous_outputs(self):
        archive = self.api.generate_project(self.root)
        consolidated = self.docs / 'DOCUMENTACAO-COMPLETA.md'
        before = (archive.read_bytes(), consolidated.read_bytes())
        self.write('README.md', '[Erro](ausente.md)')
        with self.assertRaises(ValueError):
            self.api.generate_project(self.root)
        self.assertEqual((archive.read_bytes(), consolidated.read_bytes()), before)


if __name__ == '__main__':
    unittest.main()
