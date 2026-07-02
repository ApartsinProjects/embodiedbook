r"""
fix_garbled_math.py — Repair wave-agent garbled inline math of the form
    $MATH1\( SEP \)MATH2$   ->   \(MATH1\) SEP \(MATH2\)
where SEP is a short prose separator (gives / to / m, / , ...). Only fires when
the outer $...$ wraps exactly one \( ... \) with math on both sides.

Usage: python fix_garbled_math.py [--apply]
"""
import re, glob, sys, html

APPLY = "--apply" in sys.argv
# $ M1 \( SEP \) M2 $   -- M1/M2 may contain LaTeX (\cmd) but not \( or \); SEP is prose
_M = r'(?:[^$\\\n]|\\[a-zA-Z])'
PAT = re.compile(r'\$(' + _M + r'{1,70}?)\\\(([^$\\\n]{1,25}?)\\\)(' + _M + r'{1,70}?)\$')

def repl(m):
    m1, sep, m2 = m.group(1), m.group(2), m.group(3)
    # sanity: m1 and m2 should look like math (letters/digits/operators), sep short prose
    return rf'\({m1}\){sep}\({m2}\)'

total = 0
changed = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    src = open(f, encoding='utf-8').read()
    # protect code/pre
    blocks = []
    def prot(mm):
        blocks.append(mm.group(0)); return f"\x00{len(blocks)-1}\x00"
    t = re.sub(r'<(pre|code|script|style)\b.*?</\1>', prot, src, flags=re.DOTALL | re.I)
    new, n = PAT.subn(repl, t)
    new = re.sub(r"\x00(\d+)\x00", lambda mm: blocks[int(mm.group(1))], new)
    if n:
        total += n; changed += 1
        print(f"  {n:3d}  {f.split('module-')[-1][:45]}")
        if APPLY:
            open(f, 'w', encoding='utf-8').write(new)

print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'}: fixed {total} garbled spans across {changed} files")
