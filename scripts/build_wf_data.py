"""Pre-compute all workflow data into scripts/_wf_data.json for embedding in JS workflows."""
import json
import re

ROOT_SCRIPTS = __import__('pathlib').Path(__file__).parent

secidx = json.loads((ROOT_SCRIPTS / 'section_index.json').read_text(encoding='utf-8'))

# Short title map: "sec: short_title\n..."
short_map_lines = []
for s in secidx:
    t = re.sub(r'^Section \d+[.]\d+:\s*', '', s['title'])[:65]
    short_map_lines.append(s['sec'] + ': ' + t)
short_map = '\n'.join(short_map_lines)

# Path lookup: {sec: path}  (forward slashes)
sec_paths = {}
for s in secidx:
    sec_paths[s['sec']] = s['path'].replace('\\', '/')

def clean(lst):
    return [{'sec': x['sec'],
             'title': re.sub(r'^Section \d+[.]\d+:\s*', '', x['title'])[:70],
             'path': x['path'].replace('\\', '/')} for x in lst]

w5  = clean(json.loads((ROOT_SCRIPTS / 'wave5_targets.json').read_text(encoding='utf-8')))
w6  = clean(json.loads((ROOT_SCRIPTS / 'wave6_targets.json').read_text(encoding='utf-8')))
w7  = clean(json.loads((ROOT_SCRIPTS / 'wave7_targets.json').read_text(encoding='utf-8')))
w8a = clean(json.loads((ROOT_SCRIPTS / 'wave8_alg_targets.json').read_text(encoding='utf-8')))
w8b = clean(json.loads((ROOT_SCRIPTS / 'wave8_code_targets.json').read_text(encoding='utf-8')))

out = {
    'short_map': short_map,
    'sec_paths': sec_paths,
    'w5': w5, 'w6': w6, 'w7': w7, 'w8a': w8a, 'w8b': w8b,
}
(ROOT_SCRIPTS / '_wf_data.json').write_text(
    json.dumps(out, ensure_ascii=False, indent=None), encoding='utf-8'
)
print('short_map chars:', len(short_map))
print('sec_paths entries:', len(sec_paths))
print('w5:', len(w5), 'w6:', len(w6), 'w7:', len(w7), 'w8a:', len(w8a), 'w8b:', len(w8b))
total = len(json.dumps(out))
print('total _wf_data.json chars:', total)
