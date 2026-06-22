import json, re
from pathlib import Path

ROOT    = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent

si = json.loads((SCRIPTS / 'section_index.json').read_text(encoding='utf-8'))
out = []
for x in si:
    t = re.sub(r'^Section \d+[.]\d+:\s*', '', x.get('title', ''))[:70]
    p = x['path'].replace('\\', '/')
    out.append({'sec': x['sec'], 'title': t, 'path': p})

ALL_JS = json.dumps(out, ensure_ascii=False)
print(f'Sections: {len(out)}, JS size: {len(ALL_JS):,}')

script = (SCRIPTS / 'wave13_final_workflow.js').read_text(encoding='utf-8')

old = """const allSecRaw = await agent(
  `Read the file scripts/section_index.json and return its full content. Return ONLY the raw JSON array.`,
  { label: 'load-sections' }
)
const allSections = typeof allSecRaw === 'string' ? JSON.parse(allSecRaw) : allSecRaw"""

new = f"const allSections = {ALL_JS}"

if old in script:
    script2 = script.replace(old, new)
    print('Replaced runtime load with embedded array.')
else:
    print('ERROR: pattern not found — check script manually')
    raise SystemExit(1)

(SCRIPTS / 'wave13_final_workflow.js').write_text(script2, encoding='utf-8')
print(f'Done. New size: {len(script2):,} chars, under 512k: {len(script2) < 524288}')
