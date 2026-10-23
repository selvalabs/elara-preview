"""Validate the approved Astro distribution and legacy review redirect."""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
manifest = json.loads((SITE / 'build.json').read_text(encoding='utf-8'))
assert manifest['dirty'] is False and manifest['mode'] == 'preview' and manifest['framework'] == 'astro'
assert manifest['basePath'] == '/elara-preview/'
assert manifest['distribution']['sourceSha'] == manifest['commit']
for relative, expected in manifest['files'].items():
    target = SITE / relative
    assert target.resolve().is_relative_to(SITE.resolve()) and not target.is_symlink(), relative
    data = target.read_bytes()
    assert len(data) == expected['bytes'] and hashlib.sha256(data).hexdigest() == expected['sha256'], relative
expected = set(manifest['files']) | {'build.json', '.nojekyll'}
actual = {p.relative_to(SITE).as_posix() for p in SITE.rglob('*') if p.is_file()}
assert actual == expected, actual ^ expected
root_html = (SITE / 'index.html').read_text(encoding='utf-8')
child_html = (SITE / 'porqueelaraimg/index.html').read_text(encoding='utf-8')
assert 'noindex, nofollow' in root_html and '<astro-island' in root_html
assert 'url=../#prova' in child_html and 'noindex' in child_html
assert 'image-review-entry.js' not in root_html
assert '/elara-preview/_astro/' in root_html and '="/_astro/' not in root_html
for name in ['obrigada.html', '404.html']:
    html = (SITE / name).read_text(encoding='utf-8')
    assert 'noindex, nofollow' in html and '<script' not in html and '<form' not in html
    assert 'https://wa.me/557191026649' in html
assert '/elara-preview/assets/' in (SITE / '404.html').read_text(encoding='utf-8')
assert not any(name.startswith('editor/') or 'photo-choices' in name for name in manifest['files'])
assert '2026-11-24T23:59:00-03:00' in root_html
assert 'encontros-presenciais-grupo-original-' in root_html
assert root_html.count('href="https://pay.kiwify.com.br/M5pqPmr"') == 6
assert 'https://pay.kiwify.com.br/qAID3mU' not in root_html
for filename in ['card01-opcao-05-', 'card02-opcao-01-', 'card03-opcao-04-']:
    assert filename in root_html
for removed in ['data-photo-choices', 'data-photo-option', 'data-photo-status', 'logic-photo-choices__switch']:
    assert removed not in root_html
assert root_html.count('logic-card__thumb-header--approved') == 3
print('Astro home, support pages and legacy redirect verified; source:', manifest['commit'])
