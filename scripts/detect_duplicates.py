"""
Deduplication detection: extract all callout blocks and paragraphs across 379 sections,
find near-duplicate pairs using word-overlap Jaccard similarity.

Output: scripts/dedup_report.json
  - callout_duplicates: list of {type, sec_a, path_a, text_a, sec_b, path_b, text_b, similarity}
  - para_duplicates: same structure for paragraph-level duplicates
  - concept_overlaps: sections whose big-picture callout texts are too similar
"""
import glob
import json
import re
from pathlib import Path
from itertools import combinations

ROOT = Path(__file__).parent.parent

CALLOUT_TYPES = [
    'tip', 'fun-note', 'algorithm', 'practical-example',
    'key-insight', 'pathway', 'big-picture', 'research-frontier',
]


def strip_html(html):
    return re.sub(r'<[^>]+>', ' ', html).strip()


def tokenize(text):
    return set(re.findall(r'\b[a-z]{3,}\b', text.lower()))


def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def extract_callouts(html, path, sec_num):
    """Extract all callout blocks with their type, text, and context."""
    results = []
    for ct in CALLOUT_TYPES:
        pat = re.compile(
            r'<div class="callout ' + re.escape(ct) + r'"[^>]*>(.*?)</div>',
            re.DOTALL
        )
        for m in pat.finditer(html):
            text = strip_html(m.group(1))
            if len(text.split()) < 8:
                continue
            results.append({
                'type': ct,
                'sec': sec_num,
                'path': str(path).replace('\\', '/'),
                'text': text[:400],
                'tokens': tokenize(text),
            })
    return results


def extract_paragraphs(html, path, sec_num):
    """Extract body paragraphs (skip short ones, skip nav/header)."""
    # Only grab paragraphs inside <main> or <section> (not nav footer)
    main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    body = main_m.group(1) if main_m else html
    results = []
    for m in re.finditer(r'<p>(.*?)</p>', body, re.DOTALL):
        text = strip_html(m.group(1))
        words = text.split()
        if len(words) < 30:
            continue
        results.append({
            'sec': sec_num,
            'path': str(path).replace('\\', '/'),
            'text': text[:300],
            'tokens': tokenize(text),
        })
    return results


def find_duplicates(items, threshold, key='type'):
    """Find pairs with Jaccard similarity above threshold."""
    dups = []
    # Group by type for callouts, or just do all-vs-all for paragraphs
    groups = {}
    for item in items:
        g = item.get(key, 'para')
        groups.setdefault(g, []).append(item)

    for gname, group in groups.items():
        for a, b in combinations(group, 2):
            if a['sec'] == b['sec']:
                continue  # same section, skip
            sim = jaccard(a['tokens'], b['tokens'])
            if sim >= threshold:
                dups.append({
                    'type': gname,
                    'sec_a': a['sec'],
                    'path_a': a['path'],
                    'text_a': a['text'],
                    'sec_b': b['sec'],
                    'path_b': b['path'],
                    'text_b': b['text'],
                    'similarity': round(sim, 3),
                })
    return sorted(dups, key=lambda x: -x['similarity'])


def main():
    sections = sorted(ROOT.glob('part-*/module-*/section-*.html'))
    print(f'Scanning {len(sections)} sections...')

    all_callouts = []
    all_paragraphs = []

    for path in sections:
        html = path.read_text(encoding='utf-8')
        sec_m = re.search(r'section-(\d+[.]\d+)', str(path))
        sec_num = sec_m.group(1) if sec_m else str(path)

        all_callouts.extend(extract_callouts(html, path, sec_num))
        all_paragraphs.extend(extract_paragraphs(html, path, sec_num))

    print(f'Extracted {len(all_callouts)} callout blocks, {len(all_paragraphs)} paragraphs')

    # Find duplicates
    callout_dups = find_duplicates(all_callouts, threshold=0.55, key='type')
    para_dups = find_duplicates(all_paragraphs, threshold=0.60, key='type')

    # Concept overlaps: big-picture callouts with high similarity
    bp_callouts = [c for c in all_callouts if c['type'] == 'big-picture']
    concept_overlaps = find_duplicates(bp_callouts, threshold=0.45, key='type')

    # Strip token sets (not JSON-serializable)
    def clean(lst):
        return [{k: v for k, v in d.items() if k != 'tokens'} for d in lst]

    report = {
        'callout_duplicates': clean(callout_dups),
        'para_duplicates': clean(para_dups[:50]),  # cap at 50 most similar
        'concept_overlaps': clean(concept_overlaps),
        'stats': {
            'total_sections': len(sections),
            'total_callouts': len(all_callouts),
            'total_paragraphs': len(all_paragraphs),
            'callout_dup_pairs': len(callout_dups),
            'para_dup_pairs': len(para_dups),
            'concept_overlap_pairs': len(concept_overlaps),
        }
    }

    out = ROOT / 'scripts' / 'dedup_report.json'
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False))

    print(f'\nResults:')
    for k, v in report['stats'].items():
        print(f'  {k}: {v}')
    print(f'\nSaved to scripts/dedup_report.json')

    # Print top 10 callout duplicates
    if callout_dups:
        print(f'\nTop callout duplicates (sim >= 0.55):')
        for d in callout_dups[:10]:
            print(f'  [{d["type"]}] sec {d["sec_a"]} <-> sec {d["sec_b"]}: sim={d["similarity"]}')
            print(f'    A: {d["text_a"][:80]}...')
            print(f'    B: {d["text_b"][:80]}...')


if __name__ == '__main__':
    main()
