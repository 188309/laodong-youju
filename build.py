"""Build a standalone, backend-free public reading edition from the curated corpus."""
import json
import html
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent
corpus = json.loads((root / 'law-sources.json').read_text())
esc = lambda value: html.escape(str(value), quote=True)
cards = []
for law in corpus['records']:
    terms = ' '.join(str(law.get(k, '')) for k in ['title', 'article', 'text', 'summary', 'note']) + ' ' + ' '.join(law.get('topics', []))
    cards.append(f'''<details class="law-card" data-search="{esc(terms)}">
    <summary><span><small>{esc(law['level'])} · {esc(law['article'])}</small><strong>{esc(law['title'])}</strong><span class="law-description">{esc(law['summary'])}</span></span><b class="expand" aria-hidden="true">＋</b></summary>
    <div class="law-content"><h4>法律原文{'（节录）' if '节录' in law['article'] else ''}</h4><blockquote>{esc(law['text'])}</blockquote><h4>理解与适用</h4><p>{esc(law.get('note') or law['summary'])}</p><dl><dt>施行日期</dt><dd>{esc(law['effectiveDate'])}</dd><dt>当前版本施行</dt><dd>{esc(law['versionEffectiveDate'])}</dd><dt>修订情况</dt><dd>{esc(law['revisionNote'])}</dd><dt>效力核查记录</dt><dd>{esc(law['status'])}，核查日期 {esc(law['checkedAt'])}</dd><dt>适用范围</dt><dd>{esc(law['scope'])}</dd></dl><a class="source-link" href="{esc(law['url'])}" target="_blank" rel="noopener noreferrer">查看{esc(law['sourceName'])}原文 <span aria-hidden="true">↗</span></a></div></details>''')
template = (root / 'template.html').read_text()
page = template.replace('<!--LAW_CARDS-->', '\n'.join(cards)).replace('<!--LAW_COUNT-->', str(len(cards))).replace('<!--STATUS_NOTE-->', esc(corpus['statusNote']))
(root / 'index.html').write_text(page)
(root / '.nojekyll').write_text('')
dist = root / 'dist'
dist.mkdir(exist_ok=True)
(dist / 'index.html').write_text(page)
(dist / '.nojekyll').write_text('')
for name in ['community.html','community.css','community.js']:
    shutil.copy2(root / name, dist / name)
print(f'Built standalone index.html: {len(page.encode())} bytes, {len(cards)} sourced provisions')
