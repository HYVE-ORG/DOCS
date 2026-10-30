"""Portable offline documentation checks and deterministic packaging (stdlib only)."""
import argparse
from collections.abc import Sequence
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile

DOCS = Path('outputs/documentacao-software')
LEGAL = Path('outputs/referencia-legal')
SETUP = Path('outputs/toolkit-setup')
ROOT_FILES = ('README.md', 'AGENTS.md', 'LEIS.md', 'CLAUDE.md', 'RTK.md')
TOOL_FILES = ('scripts/documentacao.py', 'work/finalizar_documentacao.py', 'work/prepare_beta_repositories.py',
              'work/registrar_referencia_legal.ps1', 'tests/test_documentacao.py')
SETUP_FILES = ('01-brainstorming-e-design.md', '02-matriz-de-cobertura.md',
               '03-plano-de-execucao.md', 'document-map.json', 'onboarding.md',
               'quality.md', 'setup.md', 'avaliacao-harness.md')
MVP_DOC_FILES = ('README.md', 'docs/github-beta.md', 'docs/design-system.md', 'docs/spaces.md', 'docs/desktop.md', 'docs/landing-page.md', 'docs/billing.md', 'docs/studio-export.md', 'docs/meeting-room.md',
                 'docs/crm.md', 'docs/navigation-team.md', 'docs/structure-review.md', 'docs/updates.md', 'docs/beta-backend.md', 'docs/cloudflare.md', 'docs/supabase.md', 'docs/central-domain.md', 'docs/central-work.md', 'docs/beta-status-report.md',
                 'apps/web/public/downloads/forma-guia-desktop.md')


def inside(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or re.match(r'^[A-Za-z]:', relative) or relative.startswith(('\\', '/')):
        raise ValueError(f'Caminho fora da raiz: {relative}')
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f'Caminho fora da raiz: {relative}')
    return resolved


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def chapters(root: Path) -> list[Path]:
    return sorted((root / DOCS).glob('[0-9][0-9]-*.md'))


def package_files(root: Path) -> list[Path]:
    paths = [Path(name) for name in ROOT_FILES + TOOL_FILES]
    paths += [DOCS / p.name for p in (root / DOCS).glob('*.md')]
    paths += [DOCS / 'referencias-visuais' / p.name
              for p in (root / DOCS / 'referencias-visuais').glob('*.png')]
    paths += [DOCS / 'manifesto-documentacao.json', LEGAL / 'README.md', LEGAL / 'manifesto.json']
    paths += [LEGAL / row['path'] for row in read_json(root / LEGAL / 'manifesto.json')['files']]
    paths += [SETUP / name for name in SETUP_FILES]
    # Only published guides: application code, profiles and releases stay outside this archive.
    paths += [Path('outputs/software-mvp') / name for name in MVP_DOC_FILES]
    return sorted({p for p in paths if inside(root, p.as_posix()).is_file()}, key=lambda p: p.as_posix())


def markdown_errors(path: Path, root: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    name = path.relative_to(root).as_posix()
    errors = []
    if '\ufffd' in text:
        errors.append(f'{name}: caractere de substituição UTF-8')
    fence, visible = None, []
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
        elif fence is None:
            visible.append(line)
    if fence:
        errors.append(f'{name}: bloco de código não fechado')
    for match in re.finditer(r'\]\(([^)]+)\)', '\n'.join(visible)):
        target = match.group(1).strip().strip('<>')
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        local = unquote(urlsplit(target).path)
        if local:
            destination = (path.parent / local).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f'{name}: link inválido {target}')
    return errors


def check_project(root: Path) -> list[str]:
    """Validate sources only. Never modify artifacts or manifests."""
    root, errors = root.resolve(), []
    try:
        fixed = [Path(name) for name in ROOT_FILES + TOOL_FILES]
        fixed += [SETUP / name for name in SETUP_FILES]
        fixed += [DOCS / 'README.md', LEGAL / 'README.md']
        for relative in fixed:
            if not inside(root, relative.as_posix()).is_file():
                errors.append(f'Arquivo de distribuição obrigatório ausente: {relative.as_posix()}')
        manifest = read_json(root / DOCS / 'manifesto-documentacao.json')
        required, requirements = manifest['required_chapters'], manifest['required_requirements']
        if not isinstance(required, list) or not required or not isinstance(requirements, list) or not requirements:
            raise ValueError('Manifesto documental exige capítulos e requisitos não vazios')
        for name in required:
            if not inside(root, (DOCS / name).as_posix()).is_file():
                errors.append(f'Capítulo obrigatório ausente: {name}')
        found = chapters(root)
        if [int(p.name[:2]) for p in found] != list(range(1, len(found) + 1)):
            errors.append('Capítulos precisam de numeração única e contígua a partir de 01')
        body = '\n'.join(p.read_text(encoding='utf-8') for p in found)
        definitions = set(re.findall(r'(?m)^\|\s*(RF-\d{2})\s*\|', body))
        definitions.update(re.findall(r'\*\*(RN-\d{2}):\*\*', body))
        for requirement in requirements:
            if requirement not in definitions:
                errors.append(f'Requisito obrigatório sem definição: {requirement}')
        legal = read_json(root / LEGAL / 'manifesto.json')
        if not isinstance(legal['files'], list) or not legal['files']:
            raise ValueError('Manifesto legal vazio')
        for record in legal['files']:
            path = inside(root / LEGAL, record['path'])
            content = path.read_bytes()
            if len(content) != record['bytes'] or hashlib.sha256(content).hexdigest() != record['sha256']:
                errors.append(f'Snapshot legal divergente: {record["path"]}')
        for path in package_files(root):
            if path.suffix == '.md' and not path.is_relative_to(LEGAL / 'acervo'):
                if path.name != 'DOCUMENTACAO-COMPLETA.md':
                    errors.extend(markdown_errors(root / path, root))
            if path.suffix == '.json':
                read_json(root / path)
        mapping = root / SETUP / 'document-map.json'
        if mapping.exists():
            for key, targets in read_json(mapping).items():
                for target in targets:
                    if not inside(root, target).is_file():
                        errors.append(f'Mapeamento sem destino: {key}: {target}')
        metadata(root)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        errors.append(f'Fonte inválida ({type(error).__name__}): {str(error).replace(str(root), ".")}')
    return errors


def metadata(root: Path) -> tuple[str, str]:
    index = (root / DOCS / 'README.md').read_text(encoding='utf-8')
    version = re.search(r'versão (\d+\.\d+)', index)
    date = read_json(root / DOCS / 'manifesto-documentacao.json').get('editorial_date')
    if date is None:
        match = re.search(r'Data editorial: (\d{4}-\d{2}-\d{2})', index)
        date = match.group(1) if match else None
    if not version or not isinstance(date, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
        raise ValueError('Índice/manifesto precisam de versão e data editorial ISO explícitas')
    return version.group(1), date


def consolidated_bytes(root: Path) -> bytes:
    version, date = metadata(root)
    intro = ('# Documentação completa · Plataforma de trabalho colaborativo\n\n'
             f'**Versão {version} · {date} · Proposta para revisão**\n\n'
             'Público inicial confirmado: equipe do criador e seus amigos. '
             'Este documento descreve o produto a desenvolver.\n\n'
             'Os capítulos separados são a fonte editorial; esta versão os reúne para distribuição.\n\n')
    return (intro + '\n\n---\n\n'.join(p.read_text(encoding='utf-8') for p in chapters(root)) + '\n').encode('utf-8')


def archive_bytes(root: Path, consolidated: bytes) -> bytes:
    buffer = io.BytesIO()
    members = {p.as_posix(): (root / p).read_bytes() for p in package_files(root)}
    members[(DOCS / 'DOCUMENTACAO-COMPLETA.md').as_posix()] = consolidated
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, content in sorted(members.items()):
            info = zipfile.ZipInfo(name, date_time=(2000, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type, info.external_attr = zipfile.ZIP_DEFLATED, 0o100644 << 16
            archive.writestr(info, content, compresslevel=9)
    return buffer.getvalue()


def artifact_errors(root: Path) -> list[str]:
    """Separate derived-data checks so stale output can still be regenerated."""
    version, _ = metadata(root)
    text = consolidated_bytes(root)
    expected = {DOCS / 'DOCUMENTACAO-COMPLETA.md': text,
                Path(f'outputs/documentacao-software-v{version}.zip'): archive_bytes(root, text)}
    if not any((root / path).exists() for path in expected):
        return []
    return [f'Artefato desatualizado: {path.as_posix()} (execute geração)'
            for path, content in expected.items()
            if path.suffix != '.zip' or (root / path).exists()
            if not (root / path).exists() or (root / path).read_bytes() != content]


def atomic_write(path: Path, content: bytes):
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.docs-', delete=False) as temporary:
        name = temporary.name
        temporary.write(content)
    try:
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def generate_project(root: Path) -> Path:
    errors = check_project(root)
    if errors:
        raise ValueError('\n'.join(errors))
    version, _ = metadata(root)
    text = consolidated_bytes(root)
    data = archive_bytes(root, text)
    destination = root / f'outputs/documentacao-software-v{version}.zip'
    atomic_write(root / DOCS / 'DOCUMENTACAO-COMPLETA.md', text)
    atomic_write(destination, data)
    return destination


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true', help='Validate without writing files')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    errors = check_project(root)
    if not errors and args.check:
        errors = artifact_errors(root)
    if errors:
        print('\n'.join(errors))
        return 1
    if args.check:
        print('PASS: fontes, links, requisitos, manifesto legal e artefatos presentes; sem escrita.')
    else:
        print(f'Gerado: {generate_project(root).relative_to(root).as_posix()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
