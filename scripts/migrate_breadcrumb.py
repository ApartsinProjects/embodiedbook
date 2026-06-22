"""
Migrate all HTML headers from old .part-label/.chapter-label two-row stack
to new .page-breadcrumb single-row design (Wave D, May 2026).

CSS is already written; this script updates all HTML.
"""
import re
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pattern 1: linked part-label + chapter-label + h1 (section & chapter index files)
LINKED_PAT = re.compile(
    r'<div class="part-label"><a href="([^"]+)">([^<]+)</a></div>\n'
    r'<div class="chapter-label"><a href="([^"]+)">([^<]+)</a></div>\n'
    r'<h1>([^<]+)</h1>'
)

# Pattern 2: unlinked part-label + chapter-label + h1 (front-matter files)
UNLINKED_PAT = re.compile(
    r'<div class="part-label">([^<]+)</div>\n'
    r'<div class="chapter-label">([^<]+)</div>\n'
    r'<h1>([^<]+)</h1>'
)

# Pattern 3: only part-label (template files, no chapter-label)
PART_ONLY_PAT = re.compile(
    r'<div class="part-label"><a href="([^"]+)">([^<]+)</a></div>\n'
    r'(?!<div class="chapter-label">)'
)


def migrate(content, basename):
    changed = False

    def replace_linked(m):
        part_href = m.group(1)
        part_text = m.group(2)
        ch_href = m.group(3)
        ch_text = m.group(4)
        h1_text = m.group(5)
        # Chapter index: h1 begins with Chapter; just show Part in breadcrumb
        if h1_text.startswith('Chapter'):
            new = (
                f'<div class="page-breadcrumb">'
                f'<a href="{part_href}">{part_text}</a>'
                f'</div>\n'
                f'<h1>{h1_text}</h1>'
            )
        else:
            # Section (or appendix section): show Part › Chapter
            new = (
                f'<div class="page-breadcrumb">'
                f'<a href="{part_href}">{part_text}</a>'
                f'<span class="bc-sep">›</span>'
                f'<a href="{ch_href}">{ch_text}</a>'
                f'</div>\n'
                f'<h1>{h1_text}</h1>'
            )
        return new

    def replace_unlinked(m):
        part_text = m.group(1)
        # ch_text ignored; h1 is the actual page title
        h1_text = m.group(3)
        return (
            f'<div class="page-breadcrumb">'
            f'<span class="bc-current">{part_text}</span>'
            f'</div>\n'
            f'<h1>{h1_text}</h1>'
        )

    def replace_part_only(m):
        part_href = m.group(1)
        part_text = m.group(2)
        return (
            f'<div class="page-breadcrumb">'
            f'<a href="{part_href}">{part_text}</a>'
            f'</div>\n'
        )

    new_content, n1 = LINKED_PAT.subn(replace_linked, content)
    if n1:
        return new_content, n1

    new_content, n2 = UNLINKED_PAT.subn(replace_unlinked, content)
    if n2:
        return new_content, n2

    new_content, n3 = PART_ONLY_PAT.subn(replace_part_only, content)
    if n3:
        return new_content, n3

    return content, 0


def main():
    html_files = sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True))
    changed = 0
    skipped = 0
    for path in html_files:
        if '.git' in path:
            continue
        try:
            with open(path, encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f'SKIP (read error): {path}: {e}')
            continue

        new_content, n = migrate(content, os.path.basename(path))
        if n:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changed += 1
        else:
            if '<div class="part-label">' in content:
                skipped += 1
                print(f'UNMATCHED: {os.path.relpath(path, ROOT)}')

    print(f'\nMigrated: {changed} files')
    print(f'Unmatched part-label files: {skipped}')


if __name__ == '__main__':
    main()
