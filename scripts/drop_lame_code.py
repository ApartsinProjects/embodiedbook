"""
Drop lame code blocks (data-table-only, no real library/API/algorithm) that
have a nearby comparison table already presenting the same data.

Removes per block:
  - optional intro h2 that is code-specific
  - optional intro paragraph referencing the code label
  - <pre><code>...</code></pre>
  - optional <div class="code-output">...</div>
  - <div class="code-caption">...</div>

Updates exercises that reference the removed code label to say Table instead.
"""
import re
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── helpers ────────────────────────────────────────────────────────────────

def is_lame(code_text):
    has_import = bool(re.search(r'^import |^from ', code_text, re.MULTILINE))
    has_def    = bool(re.search(r'^def ',            code_text, re.MULTILINE))
    has_class  = bool(re.search(r'^class ',          code_text, re.MULTILINE))
    lines = [l.strip() for l in code_text.strip().split('\n')
             if l.strip() and not l.strip().startswith('#')]
    is_mostly_data = (
        sum(1 for l in lines if re.match(r'[\[({\"]|[A-Za-z_]+\s*=\s*[\[(]', l))
        > len(lines) * 0.4
    )
    return (not has_import and not has_def and not has_class
            and len(lines) <= 20 and is_mostly_data)

def has_nearby_comparison_table(content, end_pos):
    return 'comparison-table' in content[:end_pos + 1000]

CODE_LABEL_PAT = re.compile(
    r'Code(?:\s+Fragment)?\s+[\d]+\.[\d]+(?:\.[\d.A-Za-z]+)?'
)

def drop_lame_blocks(content):
    # We iterate over all pre/code blocks and collect removals
    removals = []  # list of (start, end) in content to delete
    blocks = list(re.finditer(r'<pre><code[^>]*>.*?</code></pre>', content, re.DOTALL))

    for m in blocks:
        if not is_lame(m.group()):
            continue
        if not has_nearby_comparison_table(content, m.end()):
            continue

        remove_start = m.start()
        remove_end   = m.end()

        # 1. Absorb code-output block immediately after (optional)
        co = re.match(r'\n<div class="code-output">.*?</div>', content[remove_end:remove_end+4000], re.DOTALL)
        if co:
            remove_end += co.end()

        # 2. Absorb code-caption block immediately after (required by contract)
        cc = re.match(r'\n<div class="code-caption">.*?</div>', content[remove_end:remove_end+2000], re.DOTALL)
        if cc:
            remove_end += cc.end()

        # 3. Absorb the intro paragraph that specifically mentions the code label
        # Look backwards from remove_start for up to 1000 chars
        lookback = content[max(0, remove_start - 1200):remove_start]
        # Find last <p>...</p> before the code block
        para_m = None
        for pm in re.finditer(r'<p>[^<]*(?:Code(?:\s+Fragment)?\s+[\d]+\.[\d]+|snippet|block|following code|table below)[^<]*(?:<[^/][^>]*>[^<]*</[^>]+>[^<]*)*</p>', lookback, re.IGNORECASE | re.DOTALL):
            para_m = pm  # keep the last one
        if para_m:
            abs_para_start = (remove_start - 1200 + max(0, remove_start - 1200 - (remove_start - 1200))) + para_m.start()
            abs_para_start = remove_start - len(lookback) + para_m.start()
            abs_para_end   = remove_start - len(lookback) + para_m.end()
            # Only remove if there's nothing between para end and code start except whitespace
            between = content[abs_para_end:remove_start]
            if between.strip() == '':
                remove_start = abs_para_start

        # 4. Absorb a code-specific <h2> right before (optional)
        lookback2 = content[max(0, remove_start - 300):remove_start]
        h2_m = re.search(r'<h2>(?:[^<]|\s)*(?:[Cc]ode|[Ii]n code|[Tt]abulating|[Ss]nippet|[Aa]udit)[^<]*</h2>\s*$', lookback2)
        if h2_m:
            abs_h2_start = remove_start - len(lookback2) + h2_m.start()
            # Only absorb if h2 is immediately before our remove_start (no content between)
            between = content[remove_start - len(lookback2) + h2_m.end():remove_start]
            if between.strip() == '':
                remove_start = abs_h2_start

        removals.append((remove_start, remove_end))

    # Apply removals in reverse order so positions stay valid
    for start, end in sorted(removals, reverse=True):
        content = content[:start] + content[end:]

    return content, len(removals)


def update_exercise_code_refs(content):
    """Change 'Code X.Y.Z' → 'Table X.Y.Z' inside exercise callouts only."""
    def fix_exercise(m):
        inner = re.sub(
            r'\bCode(?:\s+Fragment)?\s+([\d]+\.[\d]+(?:\.[\d.A-Za-z]+)?)\b',
            r'Table \1',
            m.group(0)
        )
        return inner

    new_content = re.sub(
        r'<div class="callout exercise">.*?</div>',
        fix_exercise,
        content,
        flags=re.DOTALL
    )
    return new_content


def process_file(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    new_content, n_dropped = drop_lame_blocks(content)
    if n_dropped:
        new_content = update_exercise_code_refs(new_content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return n_dropped


def main():
    total_dropped = 0
    files_changed = 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'part-*', 'module-*', 'section-*.html'))):
        n = process_file(path)
        if n:
            files_changed += 1
            total_dropped += n

    print(f'Files modified: {files_changed}')
    print(f'Lame code blocks dropped: {total_dropped}')


if __name__ == '__main__':
    main()
