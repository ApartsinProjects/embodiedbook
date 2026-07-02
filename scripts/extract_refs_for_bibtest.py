"""Collect all <p class="bib-ref"> citations book-wide, dedupe, and write a single
HTML file (<section class="references"> with one <li> per unique reference) for bibtest."""
import re, glob, html, collections
from pathlib import Path

BIBREF = re.compile(r'<p class="bib-ref">(.*?)</p>', re.DOTALL)
seen = {}
order = []
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    t = open(f, encoding='utf-8').read()
    for m in BIBREF.finditer(t):
        entry = m.group(1).strip()
        # normalize for dedupe: strip tags, lowercase, collapse ws
        norm = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', entry)).strip().lower()
        norm = re.sub(r'https?://\S+', '', norm)  # dedupe ignoring trailing url dupes
        key = norm[:120]
        if key and key not in seen:
            seen[key] = entry
            order.append(entry)

out = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title>refs</title></head><body>',
       '<section class="references"><h2>References</h2><ol>']
for i, entry in enumerate(order, 1):
    out.append(f'<li id="ref-{i}">{entry}</li>')
out.append('</ol></section></body></html>')
Path('KDP/output').mkdir(parents=True, exist_ok=True)
open('KDP/output/all_references.html', 'w', encoding='utf-8').write('\n'.join(out))
print(f"unique references extracted: {len(order)}")
