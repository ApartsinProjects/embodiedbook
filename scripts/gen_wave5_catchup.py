"""Find wave-5 targets still missing cross-refs, generate wave5_catchup_workflow.js."""
import json, re
from pathlib import Path

ROOT   = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent

targets = json.loads((SCRIPTS / 'wave5_targets.json').read_text(encoding='utf-8'))
short_map = (SCRIPTS / '_section_map.txt').read_text(encoding='utf-8')

XREF_RE = re.compile(r'<a\s+href="\.\.\/\.\.\/')

remaining = []
for t in targets:
    path = ROOT / t['path'].replace('/', '\\')
    if not path.exists():
        remaining.append(t)
        continue
    html = path.read_text(encoding='utf-8', errors='replace')
    n = len(XREF_RE.findall(html))
    if n < 3:
        remaining.append(t)

print(f"Targets: {len(targets)}, Already done: {len(targets)-len(remaining)}, Remaining: {len(remaining)}")

# Embed as JS array
def clean(lst):
    out = []
    for x in lst:
        p = x['path'].replace('\\', '/')
        t2 = re.sub(r'^Section \d+[.]\d+:\s*', '', x.get('title',''))[:70]
        out.append({'sec': x['sec'], 'title': t2, 'path': p})
    return out

TARGETS_JS = json.dumps(clean(remaining), ensure_ascii=False)

SCRIPT = (
    "export const meta = {\n"
    "  name: 'wave-5-catchup',\n"
    "  description: 'Wave 5 catch-up: cross-reference links for sections missed by compaction',\n"
    "  phases: [{ title: 'Cross-refs catchup', detail: 'Remaining sections get 3-6 inline cross-ref links' }],\n"
    "}\n\n"
    "const SHORT_MAP = `" + short_map.replace('`', r'\`') + "`\n\n"
    "const TARGETS = " + TARGETS_JS + "\n\n"
    r"""
phase('Cross-refs catchup')
log(`Inserting cross-refs into ${TARGETS.length} remaining sections...`)

await pipeline(TARGETS, async (t) => agent(
  `You are the Cross-Reference Architect (#13) for an embodied AI textbook.

TASK: Insert 3 to 6 inline cross-reference links into section ${t.sec}.
File: ${t.path}

SECTION MAP (number: short title):
${SHORT_MAP}

INSTRUCTIONS:
1. Read file "${t.path}"
2. Count any existing <a href="../../ links — if already 3 or more, return "SKIP: already has links" and stop.
3. Identify 3-6 concepts that are covered in OTHER sections.
4. For each, wrap a natural phrase in: <a href="../../{target_path}">{phrase}</a>
   Path format: ../../part-N-name/module-MM-name/section-X.Y.html
5. Spread links across different paragraphs (max 2 per paragraph).
6. Skip: code blocks, headings, nav footer, epigraph, figure captions.
7. Edit the file directly with the Edit tool.
8. NEVER use em dashes or double dashes.

Return: "Added N links to: [list of target sections]" or "SKIP: [reason]"`,
  { label: `xref-catchup-${t.sec}`, phase: 'Cross-refs catchup' }
))

log('Wave 5 catch-up complete!')
return { wave: '5-catchup', sections_processed: TARGETS.length }
"""
)

out = SCRIPTS / 'wave5_catchup_workflow.js'
out.write_text(SCRIPT, encoding='utf-8')
print(f'wave5_catchup_workflow.js: {len(SCRIPT):,} chars')
