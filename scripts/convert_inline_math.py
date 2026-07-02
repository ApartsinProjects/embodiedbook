r"""
convert_inline_math.py — Convert bare inline $...$ math to \(...\) so html2epub's
KaTeX renderer picks it up (it only extracts $$...$$, \(...\), \[...\], not bare $...$).

Safe by construction:
  - protects <pre>/<code>/<script>/<style> blocks and $$...$$ display math
  - the $...$ match cannot cross an HTML tag (charset excludes '<')
  - converts ONLY unambiguous math:
      A. content contains \ _ ^ or {   (LaTeX)
      B. content is a single/double letter variable (t, k, q, xy)
      C. content is a compact math token with NO spaces (o_t, z_t, 0.04, R(s))
    Anything with spaces + words, or currency-like phrases, is left as-is and reported.

Usage:
  python convert_inline_math.py            # dry-run: report only
  python convert_inline_math.py --apply    # write changes
"""
import re, glob, sys, html

APPLY = "--apply" in sys.argv
INLINE = re.compile(r'(?<!\$)\$(?!\$)([^$\n<]{1,400}?)\$(?!\$)')
TOKEN = re.compile(r"^[A-Za-z0-9_^{}()\\+\-*/=,.|\[\]'~<>]+$")  # compact, no spaces
SPACED_OK = re.compile(r"^[A-Za-z0-9_^{}()\\+\-*/=,.|\[\]'~<>\s]+$")
MATH_WORDS = {
    'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'log', 'ln', 'exp', 'max', 'min',
    'arg', 'det', 'diag', 'rank', 'dim', 'var', 'cov', 'std', 'mean', 'sup',
    'inf', 'lim', 'deg', 'mod', 'gcd', 'lcm', 'tr', 'sgn', 'abs', 'argmax',
    'argmin', 'softmax', 'relu', 'tanh', 'erf',
}
# common 2-letter English words that must NOT be treated as math (blocks currency
# ranges like "$5 to $10" and prose fragments)
ENGLISH_2 = {
    'to', 'of', 'is', 'as', 'at', 'an', 'or', 'if', 'so', 'in', 'by', 'we',
    'no', 'do', 'go', 'it', 'he', 'us', 'my', 'me', 'up', 'on', 'be', 'am',
    'the', 'and',
}


def _tok_ok(w):
    lw = w.lower()
    if len(w) == 1:
        return True
    if lw in MATH_WORDS:
        return True
    if len(w) == 2 and lw not in ENGLISH_2:
        return True                       # e.g. bK, IG, xy (matrix/fn/var names)
    return False


def is_math(s):
    s = html.unescape(s.strip())          # &lt; -> < so comparisons are detectable
    if not s:
        return False
    if r'\(' in s or r'\)' in s or r'\[' in s or r'\]' in s:
        return False                      # garbled mixed delimiters -> manual repair
    if re.search(r'[\\_^{}]', s):
        return True                       # A: LaTeX markers
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9]?', s):
        return True                       # B: single/double var
    if ' ' not in s and TOKEN.match(s):
        return True                       # C: compact math token, no spaces
    # D: spaced math (K = 0.4, a - bK, u < 0.85, r(s, a)) -- every alpha run must
    #    be a short variable / math word; rejects English prose & currency.
    if len(s) <= 45 and SPACED_OK.match(s):
        alpha = re.findall(r'[A-Za-z]+', s)
        if all(_tok_ok(w) for w in alpha):
            if alpha:
                return True
            if re.search(r'\d', s):
                return True               # pure numeric (= 0.420, 2.6 > 1.0)
    return False


def protect(text, pat, store, flags=re.DOTALL | re.I):
    def repl(m):
        store.append(m.group(0))
        return f"\x00{len(store)-1}\x00"
    return re.sub(pat, repl, text, flags=flags)


def restore(text, store):
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], text)


total_conv = 0
total_skip = 0
files_changed = 0
skip_samples = []

for f in sorted(glob.glob('part-*/module-*/section-*.html')) + sorted(glob.glob('front-matter/*.html')):
    src = open(f, encoding='utf-8').read()
    store = []
    t = protect(src, r'<pre\b.*?</pre>', store)
    t = protect(t, r'<code\b.*?</code>', store)
    t = protect(t, r'<script\b.*?</script>', store)
    t = protect(t, r'<style\b.*?</style>', store)
    t = protect(t, r'\$\$.*?\$\$', store)   # display math

    conv = [0]

    def repl(m):
        content = m.group(1)
        if is_math(content):
            conv[0] += 1
            return r'\(' + content + r'\)'
        else:
            global total_skip
            total_skip += 1
            if len(skip_samples) < 25:
                skip_samples.append(content.strip()[:40])
            return m.group(0)

    t = INLINE.sub(repl, t)
    t = restore(t, store)

    if conv[0]:
        total_conv += conv[0]
        files_changed += 1
        if APPLY:
            open(f, 'w', encoding='utf-8').write(t)

print(f"{'APPLIED' if APPLY else 'DRY-RUN'}")
print(f"  converted inline $...$ -> \\(...\\): {total_conv}  across {files_changed} files")
print(f"  skipped (ambiguous/currency, left as $): {total_skip}")
print(f"\n  skipped samples:")
for s in skip_samples:
    print(f"    ${s}$")
