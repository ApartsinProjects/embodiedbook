import re, glob, html
INLINE = re.compile(r'(?<!\$)\$(?!\$)([^$\n<]{1,80}?)\$(?!\$)')
real = []
falsepair = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    t = open(f, encoding='utf-8').read()
    t = re.sub(r'<(pre|code|script|style)\b.*?</\1>', ' ', t, flags=re.DOTALL | re.I)
    t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    for m in INLINE.findall(t):
        s = m.strip()
        # "real math" = has latex marker or looks like a var-equation, few english words
        english = [w for w in re.findall(r'[A-Za-z]{3,}', s) if w.lower() not in
                   ('sin','cos','tan','log','exp','max','min','arg','det','diag','rank','dim','var','cov','std','tanh','relu','softmax')]
        if (re.search(r'[\\_^]', s) or re.fullmatch(r'[A-Za-z][A-Za-z0-9]?', s)) and len(english) <= 1:
            real.append((f.split('module-')[-1][:38], s[:45]))
        else:
            falsepair += 1
print(f'REAL residual leaks: {len(real)}   |   false-pairs (correctly left): {falsepair}')
print('\nreal residual leaks (file :: content):')
for fn, s in real:
    print(f'  {fn:40s}  ${s}$')
