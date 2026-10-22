"""Valida integridade e equivalência da home e da comparação de imagens."""
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
for folder in [SITE, SITE / 'porqueelaraimg']:
    manifest = json.loads((folder / 'build.json').read_text(encoding='utf-8'))
    assert manifest['dirty'] is False and manifest['mode'] == 'preview'
    for relative, expected in manifest['files'].items():
        target = (folder / relative).resolve()
        assert target.is_relative_to(folder.resolve()) and not target.is_symlink(), relative
        data = target.read_bytes()
        assert len(data) == expected['bytes'] and hashlib.sha256(data).hexdigest() == expected['sha256'], relative
manifest = json.loads((SITE / 'build.json').read_text(encoding='utf-8'))
expected = set(manifest['files']) | {'build.json', '.nojekyll'}
actual = {p.relative_to(SITE).as_posix() for p in SITE.rglob('*') if p.is_file()}
assert actual == expected, actual ^ expected
child = json.loads((SITE / 'porqueelaraimg/build.json').read_text(encoding='utf-8'))
assert child['entry']['sourceCommit'] == child['commit']
assert child['entry']['anchor'] == 'prova'
assert manifest['commit'] == child['commit']
root_html = (SITE / 'index.html').read_text(encoding='utf-8')
child_html = (SITE / 'porqueelaraimg/index.html').read_text(encoding='utf-8')
entry = '<script type="module" src="image-review-entry.js"></script>'
assert entry not in root_html
assert child_html == root_html.replace('</body>', entry+'</body>')
for folder in [SITE, SITE / 'porqueelaraimg']:
    for name in ['obrigada.html', '404.html']:
        html = (folder / name).read_text(encoding='utf-8')
        assert 'noindex, nofollow' in html and '<script' not in html and '<form' not in html
        assert 'https://wa.me/557191026649' in html
    assert '/elara-preview/assets/' in (folder / '404.html').read_text(encoding='utf-8')
assert '2026-11-24T23:59:00-03:00' in root_html
assert 'encontros-presenciais-grupo-original-' in root_html
assert root_html.count('href="https://pay.kiwify.com.br/M5pqPmr"') == 6
assert 'https://pay.kiwify.com.br/qAID3mU' not in root_html
print('Home e comparação equivalentes e íntegras; fonte:', child['commit'])
