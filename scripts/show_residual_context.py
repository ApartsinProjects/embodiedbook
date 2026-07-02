import re, glob, html

targets = ['s_t = 1', 'p_B = (1, 0, 0)', 'd_2 = 0.6', '\\tau 1', "\\mathcal{K}'", '\\Delta F = 0.442']
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    raw = open(f, encoding='utf-8').read()
    for tg in targets:
        needle = '$' + tg
        i = raw.find(needle)
        if i >= 0:
            ctx = raw[max(0, i-140):i+len(needle)+80]
            ctx = re.sub(r'\s+', ' ', ctx)
            print(f"\n### {f.split('/')[-1]}  ::  ${tg}$")
            print("   ", ctx)
