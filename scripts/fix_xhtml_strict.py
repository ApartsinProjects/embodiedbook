r"""Fix KINDLE_STRICT_XHTML P0s:
 (a) escape raw < > & inside <pre>/<code> code blocks (raw < makes BeautifulSoup/KFX
     drop content, e.g. 'rng.random() < step_error_prob')
 (b) camelCase miscased SVG attributes (viewbox->viewBox, markerwidth->markerWidth, ...)
"""
import re, glob, sys, html

APPLY = "--apply" in sys.argv

SVG_ATTR = {
    'viewbox': 'viewBox', 'markerwidth': 'markerWidth', 'markerheight': 'markerHeight',
    'markerunits': 'markerUnits', 'refx': 'refX', 'refy': 'refY',
    'gradientunits': 'gradientUnits', 'gradienttransform': 'gradientTransform',
    'patternunits': 'patternUnits', 'patterntransform': 'patternTransform',
    'patterncontentunits': 'patternContentUnits', 'clippathunits': 'clipPathUnits',
    'spreadmethod': 'spreadMethod', 'startoffset': 'startOffset',
    'stddeviation': 'stdDeviation', 'preserveaspectratio': 'preserveAspectRatio',
    'textlength': 'textLength', 'lengthadjust': 'lengthAdjust', 'tablevalues': 'tableValues',
    'basefrequency': 'baseFrequency', 'numoctaves': 'numOctaves', 'stitchtiles': 'stitchTiles',
}


def escape_code_body(body):
    # body is the text between <code ...> and </code>; escape stray & < >
    # protect existing entities
    body = re.sub(r'&(?!(?:[a-zA-Z]+|#\d+|#x[0-9a-fA-F]+);)', '&amp;', body)
    body = body.replace('<', '&lt;').replace('>', '&gt;')
    return body


CODE = re.compile(r'(<code\b[^>]*>)(.*?)(</code>)', re.DOTALL)


def fix_file(t):
    changed = 0
    # (a) code blocks
    def code_repl(m):
        nonlocal changed
        open_t, body, close_t = m.group(1), m.group(2), m.group(3)
        if '<' in body or '>' in body or re.search(r'&(?!(?:[a-zA-Z]+|#\d+|#x[0-9a-fA-F]+);)', body):
            newbody = escape_code_body(body)
            if newbody != body:
                changed += 1
                return open_t + newbody + close_t
        return m.group(0)
    t = CODE.sub(code_repl, t)

    # (b) SVG miscased attributes (only inside svg contexts; safe because these attr
    #     names are SVG-specific and won't appear in HTML attributes)
    for bad, good in SVG_ATTR.items():
        t, n = re.subn(r'\b' + bad + r'=', good + '=', t)
        changed += n
    return t, changed


total_files = 0
total_fixes = 0
for f in sorted(glob.glob('part-*/module-*/section-*.html')) + sorted(glob.glob('front-matter/*.html')) + ['index.html', 'toc.html']:
    try:
        t = open(f, encoding='utf-8').read()
    except FileNotFoundError:
        continue
    t2, n = fix_file(t)
    if n:
        total_files += 1; total_fixes += n
        if APPLY:
            open(f, 'w', encoding='utf-8').write(t2)

print(f"{'APPLIED' if APPLY else 'DRY-RUN'}: {total_fixes} fixes across {total_files} files")
