"""Publica o mesmo build aprovado na home e na comparação de imagens."""
import hashlib
import json
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = pathlib.Path(sys.argv[1]).resolve()
SITE = ROOT / 'site'
DEST = SITE / 'porqueelaraimg'

def metadata(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

manifest = json.loads((SOURCE / 'build.json').read_text(encoding='utf-8'))
assert manifest['dirty'] is False and manifest['mode'] == 'preview'
parent = json.loads((SITE / 'build.json').read_text(encoding='utf-8'))
for relative, info in parent['files'].items():
    assert metadata((SITE / relative).read_bytes()) == info, relative
previous_files = parent['files']
previous_commit = parent['commit']
parent = {**manifest, 'files': {**previous_files, **manifest['files']}, 'previousSourceCommit': previous_commit}
DEST.mkdir(exist_ok=True)
for relative, info in manifest['files'].items():
    source = (SOURCE / relative).resolve()
    target = (DEST / relative).resolve()
    assert source.is_relative_to(SOURCE) and target.is_relative_to(DEST)
    assert metadata(source.read_bytes()) == info, relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    root_target = (SITE / relative).resolve()
    assert root_target.is_relative_to(SITE.resolve())
    root_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, root_target)

entry = (ROOT / 'scripts/image-review-entry.js').read_bytes()
(DEST / 'image-review-entry.js').write_bytes(entry)
html_path = DEST / 'index.html'
html = html_path.read_text(encoding='utf-8')
assert 'id="prova"' in html and 'noindex, nofollow' in html
html = html.replace('</body>', '<script type="module" src="image-review-entry.js"></script></body>')
html_path.write_text(html, encoding='utf-8', newline='')
manifest['files']['index.html'] = metadata(html_path.read_bytes())
manifest['files']['image-review-entry.js'] = metadata(entry)
manifest['entry'] = {'path': 'porqueelaraimg/', 'anchor': 'prova', 'sourceCommit': manifest['commit']}
(DEST / 'build.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

for relative in [*manifest['files'], 'build.json']:
    parent['files']['porqueelaraimg/'+relative] = metadata((DEST / relative).read_bytes())
parent['previews'] = {**parent.get('previews', {}), 'porqueelaraimg': manifest['entry']}
(SITE / 'build.json').write_text(json.dumps(parent, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'source': manifest['commit'], 'entry': manifest['entry'], 'resources': len(parent['files'])}))
