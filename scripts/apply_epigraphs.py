"""
Inject missing epigraph quote text into section HTML files.

Each target file has:
  <blockquote class="epigraph"><cite>Attribution</cite></blockquote>

This script turns it into:
  <blockquote class="epigraph"><p>"Quote text"</p><cite>Attribution</cite></blockquote>

Input: scripts/epigraph_results.json  (list of {path, quote, attribution})
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'epigraph_results.json')

EPIGRAPH_PAT = re.compile(
    r'<blockquote class="epigraph">\s*<cite>(.*?)</cite>\s*</blockquote>',
    re.DOTALL
)


def apply_epigraph(content, quote, attribution):
    """Replace broken epigraph (cite-only) with full quote + cite."""
    def replacer(m):
        return f'<blockquote class="epigraph"><p>"{quote}"</p><cite>{attribution}</cite></blockquote>'

    new_content, n = EPIGRAPH_PAT.subn(replacer, content, count=1)
    return new_content, n


def main():
    with open(RESULTS_FILE, encoding='utf-8') as f:
        epigraphs = json.load(f)

    applied = 0
    skipped = 0
    errors = []

    for item in epigraphs:
        rel_path = item['path']
        quote = item['quote']
        attribution = item['attribution']

        abs_path = os.path.join(ROOT, rel_path)
        if not os.path.exists(abs_path):
            errors.append(f'NOT FOUND: {rel_path}')
            skipped += 1
            continue

        with open(abs_path, encoding='utf-8') as f:
            content = f.read()

        # Check if this file actually has the broken pattern
        if not EPIGRAPH_PAT.search(content):
            # Already fixed or different structure
            skipped += 1
            continue

        new_content, n = apply_epigraph(content, quote, attribution)
        if n == 0:
            errors.append(f'NO MATCH: {rel_path}')
            skipped += 1
            continue

        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        applied += 1

    print(f'Applied: {applied}')
    print(f'Skipped (already fixed or not found): {skipped}')
    if errors:
        print('Errors:')
        for e in errors:
            print(f'  {e}')


if __name__ == '__main__':
    main()
