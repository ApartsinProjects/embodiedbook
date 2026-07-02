"""Count prose-level inline $...$ math (unrendered) excluding <pre>/<code>/script/style."""
import re, glob, html
from collections import Counter

files = glob.glob("part-*/module-*/section-*.html")
per_file = {}
samples = Counter()
total = 0
for f in files:
    t = open(f, encoding="utf-8").read()
    # remove code/pre/script/style/katex-rendered spans (already-rendered math)
    t = re.sub(r"<pre\b.*?</pre>", " ", t, flags=re.DOTALL | re.I)
    t = re.sub(r"<code\b.*?</code>", " ", t, flags=re.DOTALL | re.I)
    t = re.sub(r"<script\b.*?</script>", " ", t, flags=re.DOTALL | re.I)
    t = re.sub(r"<style\b.*?</style>", " ", t, flags=re.DOTALL | re.I)
    t = re.sub(r'<span class="katex[^"]*".*?</span>', " ", t, flags=re.DOTALL | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    # inline math: $...$ not $$ , content has no newline, length 1..60, contains a math-ish char
    matches = re.findall(r"(?<!\$)\$(?!\$)([^\$\n]{1,60}?)\$(?!\$)", t)
    matches = [m for m in matches if re.search(r"[\\_^{}]|[A-Za-z]", m)]
    if matches:
        per_file[f] = len(matches)
        total += len(matches)
        for m in matches[:3]:
            samples[m.strip()[:30]] += 1

print(f"sections with inline $...$ prose math: {len(per_file)}")
print(f"total inline $...$ occurrences: {total}")
print("\ntop sample fragments:")
for frag, n in samples.most_common(20):
    print(f"  {n:4d}  ${frag}$")
print("\nworst 10 sections:")
for f, n in sorted(per_file.items(), key=lambda x: -x[1])[:10]:
    print(f"  {n:4d}  {f}")
