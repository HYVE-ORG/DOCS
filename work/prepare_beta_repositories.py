"""Export reviewed sources into four independent, secret-free repository folders.

No network calls, git commits, dependency installation or deployment.
Destinations must be new, so a remote checkout can never be overwritten.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MVP = ROOT / 'outputs/software-mvp'
PRIVATE = {'.git', 'node_modules', '.data', '.tools', '.npm-cache', '.release-keys',
           'release', 'dist', 'dist-api', 'dist-desktop', 'work', '__pycache__'}
TOKEN = re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----|'
                   rb'\b(?:ghp_|github_pat_|sb_secret_)[A-Za-z0-9_]{20,}')


def safe_bytes(path):
    if path.is_symlink():
        raise ValueError(f'Symbolic link excluded: {path.name}')
    data = path.read_bytes()
    if TOKEN.search(data):
        raise ValueError(f'Possible private credential in {path.relative_to(ROOT)}')
    if len(data) > 50_000_000:
        raise ValueError(f'Large release artifact excluded: {path.name}')
    return data


def write(dest, relative, data):
    target = dest / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data if isinstance(data, bytes) else data.encode('utf-8'))


def copy(dest, relative):
    source = MVP / relative
    paths = sorted(source.rglob('*')) if source.is_dir() else [source]
    for path in paths:
        if not path.is_file():
            continue
        rel = path.relative_to(MVP)
        if PRIVATE.intersection(rel.parts) or (path.name.startswith('.env') and path.name != '.env.example'):
            continue
        if path.suffix in {'.log', '.exe', '.zip', '.pem', '.key'}:
            continue
        write(dest, rel, safe_bytes(path))


def metadata(dest, kind):
    package = json.loads((MVP / 'package.json').read_text(encoding='utf-8'))
    scripts = package['scripts']
    package['name'] = {'api': 'hyve-api', 'web': 'hyve-web', 'desktop': 'hyve-desktop'}[kind]
    if kind == 'api':
        package['scripts'] = {'dev': scripts['dev:api'], 'start': scripts['start'],
                              'typecheck': scripts['typecheck'], 'test': scripts['test'],
                              'build': scripts['build:api'], 'build:api': scripts['build:api']}
    elif kind == 'web':
        package['scripts'] = {'dev': scripts['dev:web'], 'typecheck': scripts['typecheck'],
                              'test': scripts['test'], 'build': scripts['build:web'],
                              'build:web': scripts['build:web'], 'preview': 'vite preview --host 127.0.0.1'}
    else:
        package['scripts'] = {k: v for k, v in scripts.items() if not k.startswith('cloudflare:')}
    # Preserve the exact tested dependency graph; do not re-resolve versions on export.
    lock = json.loads((MVP / 'package-lock.json').read_text(encoding='utf-8'))
    lock['name'] = package['name']
    lock['packages']['']['name'] = package['name']
    write(dest, 'package.json', json.dumps(package, ensure_ascii=False, indent=2) + '\n')
    write(dest, 'package-lock.json', json.dumps(lock, ensure_ascii=False, indent=2) + '\n')
    config = json.loads((MVP / 'tsconfig.json').read_text(encoding='utf-8'))
    if kind == 'api':
        config['include'] = ['apps/api/**/*.ts', 'packages/**/*.ts', 'tests/**/*.ts']
    elif kind == 'web':
        config['include'] = ['apps/web/**/*.ts', 'apps/web/**/*.tsx', 'packages/**/*.ts', 'tests/**/*.ts', 'vite.config.ts']
    write(dest, 'tsconfig.json', json.dumps(config, indent=2) + '\n')
    copy(dest, '.gitignore')
    write(dest, '.gitignore', (dest / '.gitignore').read_text(encoding='utf-8') + '\n.vercel/\nvalidation/\n')


def tests(dest, kind):
    for path in sorted((MVP / 'tests').glob('*.ts')):
        text = path.read_text(encoding='utf-8')
        if kind == 'api' and any(s in text for s in ['apps/web', 'apps/desktop', 'apps/edge', '../scripts/', "resolve('scripts/"]):
            continue
        if kind == 'web' and any(s in text for s in ['apps/api', 'apps/desktop', 'apps/edge', "resolve('scripts/"]):
            continue
        if kind == 'web' and '../scripts/' in text and 'configure-vercel.mjs' not in text:
            continue
        if kind == 'desktop' and ('apps/edge' in text or 'prepareCloudflare' in text):
            continue
        write(dest, path.relative_to(MVP), safe_bytes(path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if ROOT not in output.parents or output.exists():
        raise ValueError('Use a new output folder inside this workspace.')
    output.mkdir(parents=True)
    for repo, kind in [('API-HYVE', 'api'), ('WEB-VERSION', 'web'), ('DESKTOP-VERSION', 'desktop')]:
        dest = output / repo
        dest.mkdir()
        for item in ['packages', '.env.example']:
            copy(dest, item)
        if kind in ('api', 'desktop'):
            copy(dest, 'apps/api')
            copy(dest, 'supabase')
            for name in ['create-studio.mjs', 'check-central.ts', 'check-supabase.ts',
                         'prepare-billing-secret.mjs', 'prepare-upload-verifier.mjs', 'reconcile-billing.ts']:
                copy(dest, 'scripts/' + name)
        if kind == 'api':
            copy(dest, 'apps/edge')
            copy(dest, 'scripts/prepare-cloudflare.mjs')
        if kind in ('web', 'desktop'):
            copy(dest, 'apps/web')
            copy(dest, 'vite.config.ts')
            copy(dest, 'scripts/configure-vercel.mjs')
        if kind == 'desktop':
            copy(dest, 'apps/desktop')
            copy(dest, 'electron-builder.json')
            for name in ['dev.mjs', 'build-installer.mjs', 'package-desktop.mjs', 'release-updates.mjs',
                         'smoke-desktop-operator.mjs', 'smoke-desktop.mjs', 'smoke-updates.cjs',
                         'verify-desktop-package.py', 'verify-installer.mjs']:
                copy(dest, 'scripts/' + name)
        metadata(dest, kind)
        tests(dest, kind)
        write(dest, 'DEPLOYMENT.md', (MVP / 'docs/github-beta.md').read_text(encoding='utf-8'))
        if kind == 'api':
            write(dest, 'Dockerfile', 'FROM node:24-bookworm-slim AS build\nWORKDIR /app\n'
                  'ENV ELECTRON_SKIP_BINARY_DOWNLOAD=1\nCOPY package*.json ./\nRUN npm ci\n'
                  'COPY . .\nRUN npm run typecheck && npm run build\n'
                  'FROM node:24-bookworm-slim\nWORKDIR /app\n'
                  'ENV NODE_ENV=production HOST=0.0.0.0 PORT=4100 DATA_DIR=/app/data\n'
                  'COPY package*.json ./\nRUN npm ci --omit=dev && mkdir data && chown node:node data\n'
                  'COPY --from=build /app/dist-api ./dist-api\nUSER node\nEXPOSE 4100\n'
                  'CMD ["node", "dist-api/main.cjs"]\n')
            copy(dest, '.dockerignore')
        write(dest, 'README.md', f'# {repo} — Forma / HYVE beta\n\n'
              'Fontes separadas do MVP para revisão da beta, sem credenciais ou dados reais.\n'
              'Consulte o repositório HYVE-ORG/DOCS para o relatório e os limites de publicação.\n\n'
              'Node 22.12+ (Node 24 recomendado). Execute `npm ci`, `npm run typecheck`, '
              '`npm test` e `npm run build`. O lockfile preserva o grafo completo já testado.\n\n' +
              {'api': 'API NestJS com Socket.IO: exige processo contínuo e volume persistente. '
                       '`npm start` usa `dist-api/main.cjs`. Não publicar este processo em Vercel Functions.\n',
               'web': 'Frontend Vite. Build `dist`, raiz do projeto `.`. Vite serve `apps/web`. '
                       'O aplicativo usa `/api` e `/socket.io` da mesma origem; o proxy de desenvolvimento '
                       'não existe na Vercel. Leia `DEPLOYMENT.md` antes de publicar.\n',
               'desktop': 'Aplicativo Electron único para todos os cargos. `npm run desktop` executa '
                          'após o build. `npm run desktop:installer` gera instalador Windows. '
                          'Renderer web e API embarcada são dependências necessárias, incluídas como '
                          'snapshot; não são apps adicionais nem dependem de checkouts irmãos. '
                          'Chaves privadas de assinatura não estão neste repositório.\n'}[kind])
    docs = output / 'DOCS'
    docs.mkdir()
    archive = ROOT / 'outputs/documentacao-software-v0.30.zip'
    with zipfile.ZipFile(archive) as z:
        for entry in z.infolist():
            relative = Path(entry.filename)
            if entry.is_dir():
                continue
            if relative.is_absolute() or '..' in relative.parts:
                raise ValueError('Unsafe documentation archive path')
            data = z.read(entry)
            if TOKEN.search(data):
                raise ValueError('Possible private credential in documentation archive')
            write(docs, relative, data)
    write(docs, '.gitignore', '__pycache__/\n*.pyc\n.env\n.env.*\n!.env.example\n.data/\nnode_modules/\noutputs/*.zip\n.vercel/\n')
    manifests = {}
    for dest in sorted(p for p in output.iterdir() if p.is_dir()):
        entries = []
        for path in sorted(dest.rglob('*')):
            if path.is_file():
                data = safe_bytes(path)
                entries.append({'path': path.relative_to(dest).as_posix(), 'bytes': len(data),
                                'sha256': hashlib.sha256(data).hexdigest()})
        manifests[dest.name] = entries
    write(output, 'source-manifest.json', json.dumps(manifests, indent=2) + '\n')
    print(json.dumps({name: {'files': len(files), 'bytes': sum(f['bytes'] for f in files)}
                      for name, files in manifests.items()}, indent=2))


if __name__ == '__main__':
    main()
