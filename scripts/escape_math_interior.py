r"""Escape raw <, > inside \(...\) math interiors to &lt; / &gt; for XHTML cleanliness.
KaTeX/html2epub unescape them before rendering, so output is identical but valid."""
import re, glob, sys

APPLY = "--apply" in sys.argv
# \( ... \)  interior (no nested \( , no $)
PAT = re.compile(r'\\\((?:[^\\]|\\[^()])*?\\\)')

def esc_interior(m):
    seg = m.group(0)
    inner = seg[2:-2]
    inner = inner.replace('<', '&lt;').replace('>', '&gt;')
    return r'\(' + inner + r'\)'

total = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    src = open(f, encoding='utf-8').read()
    blocks = []
    def prot(m):
        blocks.append(m.group(0)); return f"\x00{len(blocks)-1}\x00"
    t = re.sub(r'<(pre|code|script|style)\b.*?</\1>', prot, src, flags=re.DOTALL | re.I)

    def repl(m):
        global total
        seg = m.group(0)
        if '<' in seg[2:-2] or '>' in seg[2:-2]:
            total += 1
            return esc_interior(m)
        return seg

    t2 = PAT.sub(repl, t)
    t2 = re.sub(r"\x00(\d+)\x00", lambda mm: blocks[int(mm.group(1))], t2)
    if t2 != t and APPLY:
        open(f, 'w', encoding='utf-8').write(t2)

print(f"{'APPLIED' if APPLY else 'DRY-RUN'}: escaped angle brackets in {total} math spans")
