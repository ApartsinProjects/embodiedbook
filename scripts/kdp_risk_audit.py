"""
kdp_risk_audit.py — Scan the book for KDP-publishing risks and automated-flag signals.
Categories: placeholders, AI-fluff phrases, em-dashes/banned hedges, repeated openings,
inline cross-ref validity, terminology inconsistencies, citation-format anomalies,
broken image sources. Writes KDP/output/kdp_risk_report.txt (+ .json).
"""
import re, glob, json, html, collections
from pathlib import Path

SECTIONS = sorted(glob.glob('part-*/module-*/section-*.html'))
FM = sorted(glob.glob('front-matter/*.html'))
ALL = SECTIONS + FM

def text_of(f):
    t = open(f, encoding='utf-8').read()
    t = re.sub(r'<(pre|code|script|style|svg)\b.*?</\1>', ' ', t, flags=re.DOTALL | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return html.unescape(t)

report = {}

# 1. PLACEHOLDERS / incomplete markers
ph_pat = re.compile(r'\b(TODO|FIXME|TBD|XXX|lorem ipsum|placeholder|coming soon|\[insert[^\]]*\]|\bWIP\b|fill in|to be written|to be added)\b', re.I)
placeholders = []
for f in ALL:
    for m in ph_pat.finditer(text_of(f)):
        placeholders.append((f, m.group(0)[:40]))
report['placeholders'] = placeholders

# 2. AI-FLUFF phrases
FLUFF = [
    r'delve into', r'in today\'?s world', r'it is important to note', r"it's important to note",
    r'navigat\w+ the (?:complex )?landscape', r'realm of', r'tapestry', r'testament to',
    r'ever-(?:evolving|changing)', r'at the end of the day', r'needless to say',
    r'plays? a (?:crucial|vital|pivotal|key) role', r'a wide (?:range|array) of',
    r'when it comes to', r'in the world of', r'unlock(?:ing)? the (?:power|potential)',
    r'harness(?:ing)? the (?:power|potential)', r'in conclusion,', r'first and foremost',
    r'it is worth noting', r'as (?:we|you) can see', r'the fact that',
]
fluff_pat = re.compile('|'.join(f'({p})' for p in FLUFF), re.I)
fluff = collections.Counter()
fluff_files = collections.Counter()
for f in ALL:
    hits = fluff_pat.findall(text_of(f))
    for h in hits:
        phrase = next(x for x in h if x)
        fluff[phrase.lower()] += 1
        fluff_files[f] += 1
report['ai_fluff_by_phrase'] = fluff.most_common(30)
report['ai_fluff_total'] = sum(fluff.values())

# 3. EM-DASHES + banned hedges (style + AI signal)
emdash = 0; hedge = 0
for f in ALL:
    tx = text_of(f)
    emdash += tx.count('—') + len(re.findall(r'\S--\S', tx))
    hedge += len(re.findall(r'\b(honestly|frankly|candidly|to be honest|in truth)\b', tx, re.I))
report['em_dashes'] = emdash
report['banned_hedges'] = hedge

# 4. REPEATED SECTION OPENINGS (first sentence of body prose)
openings = collections.Counter()
for f in SECTIONS:
    tx = text_of(f)
    # first 60 chars of first substantial sentence
    m = re.search(r'([A-Z][^.!?]{30,120}[.!?])', tx)
    if m:
        openings[m.group(1)[:60].strip().lower()] += 1
report['repeated_openings'] = [(k, v) for k, v in openings.most_common(15) if v >= 2]

# 5. INLINE "Section X.Y" cross-ref validity
existing = set()
for f in SECTIONS:
    m = re.search(r'section-(\d+\.\d+)', f)
    if m: existing.add(m.group(1))
bad_refs = []
for f in SECTIONS:
    for m in re.finditer(r'\bSection\s+(\d+\.\d+)\b', text_of(f)):
        if m.group(1) not in existing:
            bad_refs.append((f, m.group(1)))
report['bad_inline_section_refs'] = bad_refs

# 6. CITATION anomalies: arXiv id format, duplicate-year mismatches for same title
arxiv_bad = []
for f in ALL:
    tx = text_of(f)
    for m in re.finditer(r'arXiv[:\s]*([0-9]{4}\.[0-9]{4,5})', tx):
        pass  # valid form
    for m in re.finditer(r'arXiv[:\s]*(\d{1,3}\.\d{1,3}[^0-9])', tx):
        arxiv_bad.append((f, m.group(0)[:30]))
report['arxiv_format_anomalies'] = arxiv_bad
# same reference title cited with different years
title_years = collections.defaultdict(set)
for f in ALL:
    tx = text_of(f)
    for m in re.finditer(r'"([^"]{15,80})"[^.]{0,40}?\(?((?:19|20)\d\d)\)?', tx):
        title_years[m.group(1).strip().lower()].add(m.group(2))
year_conflicts = {t: sorted(y) for t, y in title_years.items() if len(y) > 1}
report['citation_year_conflicts'] = list(year_conflicts.items())[:20]

# 7. TERMINOLOGY inconsistency (known variant pairs)
VARIANTS = [
    ('sim-to-real', 'sim2real'), ('reinforcement learning', 'reinforcement-learning'),
    ('vision-language-action', 'vision language action'), ('model-based', 'model based'),
    ('behavior cloning', 'behaviour cloning'), ('imitation learning', 'imitation-learning'),
    ('end-to-end', 'end to end'), ('real-time', 'realtime'), ('offline RL', 'offline reinforcement learning'),
]
term_counts = {}
allbody = ' '.join(text_of(f).lower() for f in SECTIONS)
for a, b in VARIANTS:
    ca, cb = allbody.count(a.lower()), allbody.count(b.lower())
    if ca and cb:
        term_counts[f'{a} ({ca}) vs {b} ({cb})'] = (ca, cb)
report['terminology_variants'] = term_counts

# 8. BROKEN image src
broken_img = []
for f in SECTIONS:
    base = Path(f).parent
    for m in re.finditer(r'<img[^>]*\bsrc="([^"]+)"', open(f, encoding='utf-8').read()):
        src = m.group(1)
        if src.startswith(('http', 'data:')): continue
        if not (base / src).exists():
            broken_img.append((f, src))
report['broken_img_src'] = broken_img

# ---- write reports ----
Path('KDP/output').mkdir(parents=True, exist_ok=True)
json.dump(report, open('KDP/output/kdp_risk_report.json', 'w', encoding='utf-8'), indent=2, default=str)

lines = ["=== KDP RISK AUDIT ===\n"]
lines.append(f"Sections scanned: {len(SECTIONS)} (+{len(FM)} front-matter)\n")
lines.append(f"[Tier B] Placeholders/incomplete markers: {len(placeholders)}")
for f, s in placeholders[:15]: lines.append(f"    {s!r}  in {f.split('module-')[-1][:40]}")
lines.append(f"\n[Tier C] AI-fluff phrase hits: {report['ai_fluff_total']}")
for p, c in fluff.most_common(15): lines.append(f"    {c:4d}x  {p}")
lines.append(f"\n[Tier C] Em-dashes / double-dashes: {emdash}   Banned hedges: {hedge}")
lines.append(f"\n[Tier C] Repeated section openings (>=2x): {len(report['repeated_openings'])}")
for k, v in report['repeated_openings'][:8]: lines.append(f"    {v}x  {k}...")
lines.append(f"\n[Tier B] Inline 'Section X.Y' refs to nonexistent sections: {len(bad_refs)}")
for f, r in bad_refs[:12]: lines.append(f"    Section {r}  in {f.split('module-')[-1][:40]}")
lines.append(f"\n[Tier B] Citation year conflicts (same title, different years): {len(year_conflicts)}")
for t, y in list(year_conflicts.items())[:10]: lines.append(f"    {y}  \"{t[:50]}\"")
lines.append(f"\n[Tier B] arXiv format anomalies: {len(arxiv_bad)}")
lines.append(f"\n[Tier C] Terminology variant clashes: {len(term_counts)}")
for k in term_counts: lines.append(f"    {k}")
lines.append(f"\n[Tier A] Broken image src: {len(broken_img)}")
for f, s in broken_img[:10]: lines.append(f"    {s}  in {f.split('module-')[-1][:40]}")
open('KDP/output/kdp_risk_report.txt', 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines))
