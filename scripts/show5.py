import re, glob

needles = [r'$s_t = 1$', r'$B$', r'$d_2 = 0.6', r'$\tau 1$', r"$\mathcal{K}'$"]
for f in sorted(glob.glob('part-*/module-*/section-*.html')):
    t = open(f, encoding='utf-8').read()
    for n in needles:
        i = t.find(n)
        if i >= 0:
            ctx = re.sub(r'\s+', ' ', t[max(0, i-110):i+len(n)+90])
            print(f"\n### {f.split('/')[-1]}  ::  {n}")
            print("   ..." + ctx + "...")
