r"""Convert inline $...$ math containing raw <, > comparison operators to
\(...\) with the operators escaped (&lt; / &gt;) so it is XHTML-valid and KaTeX
renders it. Only fires on comparison operators, never on HTML tags."""
import re, glob, sys, html

APPLY = "--apply" in sys.argv
PAT = re.compile(r'\$([^$\n]{1,70}?)\$')
TAGLIKE = re.compile(r'</|<[a-zA-Z!]|/>|<br')  # real HTML tag markers -> skip


def ok(s):
    if '<' not in s and '>' not in s:
        return False                      # only handle comparison math here
    if TAGLIKE.search(s):
        return False                      # contains a real tag -> not pure math
    u = html.unescape(s)
    if '\\' in u:
        return True                       # has a LaTeX command -> definitely math
    eng = [w for w in re.findall(r'[A-Za-z]{3,}', u)
           if w.lower() not in ('sin','cos','tan','log','exp','max','min','tau',
                                 'alpha','beta','pi','hat','text','mathcal','ok')]
    if eng:
        return False                      # has prose word -> false pair
    return bool(re.search(r'[\\_^]|\d|[A-Za-z]', u))


def esc(s):
    return s.replace('<', '&lt;').replace('>', '&gt;')


total = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    src = open(f, encoding='utf-8').read()
    blocks = []
    def prot(m):
        blocks.append(m.group(0)); return f"\x00{len(blocks)-1}\x00"
    t = re.sub(r'<(pre|code|script|style)\b.*?</\1>', prot, src, flags=re.DOTALL | re.I)
    t = re.sub(r'\$\$.*?\$\$', prot, t, flags=re.DOTALL)

    n = [0]
    def repl(m):
        c = m.group(1)
        if ok(c):
            n[0] += 1
            return r'\(' + esc(c) + r'\)'
        return m.group(0)

    t2 = PAT.sub(repl, t)
    t2 = re.sub(r"\x00(\d+)\x00", lambda mm: blocks[int(mm.group(1))], t2)
    if n[0]:
        total += n[0]
        print(f"  {n[0]:3d}  {f.split('module-')[-1][:45]}")
        if APPLY:
            open(f, 'w', encoding='utf-8').write(t2)

print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'}: fixed {total} comparison-math spans")
