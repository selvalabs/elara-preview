"""Import a clean, merged Astro preview into a NEW site directory only."""
import argparse
import hashlib
import json
import pathlib
import re

parser = argparse.ArgumentParser()
parser.add_argument('build', type=pathlib.Path)
parser.add_argument('source_sha')
args = parser.parse_args()
root = pathlib.Path(__file__).resolve().parents[1]
source = args.build.resolve(strict=True)
output = root / 'site'
assert not output.exists(), 'Archive the previous site separately; never overwrite or delete it.'
manifest = json.loads((source / 'build.json').read_text(encoding='utf-8'))
assert manifest['dirty'] is False and manifest['mode'] == 'preview'
assert manifest['framework'] == 'astro' and manifest['commit'] == args.source_sha
assert re.fullmatch(r'[0-9a-f]{40}', args.source_sha)
assert not any('editor' in name or 'photo-choices' in name for name in manifest['files'])
assert {p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()} == set(manifest['files']) | {'build.json'}
files = {}
for relative, expected in manifest['files'].items():
    target = (source / relative).resolve(strict=True)
    assert target.is_relative_to(source) and not (source / relative).is_symlink()
    data = target.read_bytes()
    assert len(data) == expected['bytes'] and hashlib.sha256(data).hexdigest() == expected['sha256'], relative
    if relative.endswith('.html'):
        html = data.decode('utf-8')
        html = re.sub(r'((?:href|src|component-url|renderer-url)=")/(?!/)', r'\1/elara-preview/', html)
        html = html.replace('"/_astro/', '"/elara-preview/_astro/').replace("'/_astro/", "'/elara-preview/_astro/")
        data = html.encode('utf-8')
    files[relative] = data
files['porqueelaraimg/index.html'] = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">'
    '<meta http-equiv="refresh" content="0;url=../#prova"><title>ELARA</title></head>'
    '<body><a href="../#prova">Ver a ELARA</a></body></html>').encode('utf-8')
manifest['basePath'] = '/elara-preview/'
manifest['distribution'] = {'issue': 'https://github.com/selvalabs/elara-preview/issues/33',
    'sourceSha': args.source_sha, 'transformations': ['GitHub Pages prefix on root-relative HTML resources', 'Legacy image-review route redirects to home #prova']}
manifest['files'] = {name: {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()} for name, data in files.items()}
for relative, data in files.items():
    target = output / relative
    assert target.resolve().is_relative_to(output.resolve())
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
(output / 'build.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
(output / '.nojekyll').write_bytes(b'')
print(json.dumps({'source': args.source_sha, 'files': len(files), 'bytes': sum(map(len, files.values()))}))
