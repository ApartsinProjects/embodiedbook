r"""Unwrap internal <a href="..."> links whose target file does not exist
(hallucinated cross-references). Keeps the visible link text."""
import re, glob, sys, os
from pathlib import Path

APPLY = "--apply" in sys.argv
LINK = re.compile(r'<a\b[^>]*\bhref="([^"]+)"[^>]*>(.*?)</a>', re.DOTALL)

total = 0
files = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    t = open(f, encoding='utf-8').read()
    base = Path(f).parent
    n = [0]

    def repl(m):
        href, text = m.group(1), m.group(2)
        # only internal .html links (skip external, anchors, images)
        if href.startswith(('http://', 'https://', 'mailto:', '#')) or '.html' not in href:
            return m.group(0)
        path = href.split('#')[0]
        target = (base / path).resolve()
        if target.exists():
            return m.group(0)
        n[0] += 1
        return text  # unwrap: keep the text, drop the dead link

    t2 = LINK.sub(repl, t)
    if n[0]:
        total += n[0]; files += 1
        print(f"  {n[0]:2d}  {f.split('module-')[-1][:45]}")
        if APPLY:
            open(f, 'w', encoding='utf-8').write(t2)

print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'}: unwrapped {total} dead links across {files} files")
