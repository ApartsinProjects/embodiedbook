import re, glob, html
from collections import Counter

files = glob.glob('part-*/module-*/section-*.html')
cats = Counter()
currency_risk = []
INLINE = re.compile(r'(?<!\$)\$(?!\$)([^$\n<]{1,80}?)\$(?!\$)')
for f in files:
    t = open(f, encoding='utf-8').read()
    t = re.sub(r'<(pre|code|script|style)\b.*?</\1>', ' ', t, flags=re.DOTALL | re.I)
    t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.DOTALL)     # drop display math
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    for m in INLINE.findall(t):
        s = m.strip()
        if re.search(r'[\\_^{}]', s):
            cats['definite_math (backslash/_/^/{)'] += 1
        elif re.fullmatch(r'[A-Za-z][A-Za-z0-9]?', s):
            cats['single/double var'] += 1
        elif re.fullmatch(r'[A-Za-z0-9_^{}\\+\-*/=(),.|\'\[\]\s]{1,25}', s) and len(s.split()) <= 3:
            cats['mathy_short'] += 1
        else:
            cats['ambiguous'] += 1
            if re.search(r'\d', s) and re.search(r'[A-Za-z]{3,}', s):
                currency_risk.append(s)

for k, v in cats.most_common():
    print(f'  {v:6d}  {k}')
print(f'\ncurrency-risk samples ({len(currency_risk)}):')
for s in currency_risk[:15]:
    print('   ', repr(s))
