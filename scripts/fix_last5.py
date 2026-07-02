r"""Final cleanup: in the handful of odd-dollar nodes, convert each remaining
clean-math $...$ fragment to \(...\) by EXACT literal replacement (no pairing).
Only fragments that pass a strict math test are touched."""
import re, glob, sys, html

APPLY = "--apply" in sys.argv
FRAG = re.compile(r'\$([^$\n<]{1,60}?)\$')

def strict_math(s):
    s = html.unescape(s.strip())
    if r'\(' in s or r'\)' in s:
        return False
    # must contain a latex cmd or subscript/superscript or a var-operator-number combo,
    # and no english word >=3 letters (except math funcs)
    eng = [w for w in re.findall(r'[A-Za-z]{3,}', s)
           if w.lower() not in ('sin','cos','tan','log','exp','max','min','arg','det',
                                 'diag','rank','dim','var','cov','std','tanh','relu','text','hat','mathcal','pi','tau','alpha','omega')]
    if eng:
        return False
    return bool(re.search(r'[\\_^]', s) or re.fullmatch(r'[A-Za-z]', s) or
                re.search(r'\d', s))

total = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    src = open(f, encoding='utf-8').read()
    blocks = []
    def prot(m):
        blocks.append(m.group(0)); return f"\x00{len(blocks)-1}\x00"
    t = re.sub(r'<(pre|code|script|style)\b.*?</\1>', prot, src, flags=re.DOTALL | re.I)
    t = re.sub(r'\$\$.*?\$\$', prot, t, flags=re.DOTALL)

    def repl(m):
        global total
        if strict_math(m.group(1)):
            total += 1
            return r'\(' + m.group(1) + r'\)'
        return m.group(0)

    t2 = FRAG.sub(repl, t)
    t2 = re.sub(r"\x00(\d+)\x00", lambda mm: blocks[int(mm.group(1))], t2)
    if t2 != t and APPLY:
        open(f, 'w', encoding='utf-8').write(re.sub(r"\x00(\d+)\x00", lambda mm: blocks[int(mm.group(1))], t))  # placeholder-safe? no
        open(f, 'w', encoding='utf-8').write(t2)

print(f"{'APPLIED' if APPLY else 'DRY-RUN'}: converted {total} remaining math fragments")
