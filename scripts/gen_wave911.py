"""Generate waves9to11_fixed.js with all section data embedded."""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent

si   = json.loads((ROOT / 'section_index.json').read_text(encoding='utf-8'))
w10  = json.loads((ROOT / 'wave10_targets.json').read_text(encoding='utf-8'))

def clean(lst):
    out = []
    for x in lst:
        t = re.sub(r'^Section \d+[.]\d+:\s*', '', x.get('title', ''))[:70]
        p = x['path'].replace('\\', '/')
        out.append({'sec': x['sec'], 'title': t, 'path': p})
    return out

ALL_SEC_JS = json.dumps(clean(si), ensure_ascii=False)
W10_JS     = json.dumps(clean(w10), ensure_ascii=False)

SCRIPT = (
    "export const meta = {\n"
    "  name: 'waves-9-to-11',\n"
    "  description: 'Waves 9-11: opening hooks, dense prose breaks, aha-moments + memorability',\n"
    "  phases: [\n"
    "    { title: 'Wave 9 - Hooks', detail: 'Score and rewrite weak section openings' },\n"
    "    { title: 'Wave 10 - Prose', detail: 'Break dense paragraphs in 30 sections' },\n"
    "    { title: 'Wave 11 - Aha', detail: 'Add aha-moments and bold key phrases' },\n"
    "  ],\n"
    "}\n\n"
    "const ALL_SECTIONS = " + ALL_SEC_JS + "\n"
    "const W10_TARGETS  = " + W10_JS     + "\n\n"
    r"""
phase('Wave 9 - Hooks')
log(`Assessing opening hooks for ${ALL_SECTIONS.length} sections...`)
await pipeline(ALL_SECTIONS, async (t) => agent(
  `You are the Opening and Hook Designer (#22). Section ${t.sec}: ${t.title}
File: ${t.path}

Score the big-picture callout 1-10:
  9-10: Vivid concrete scene, strong "why NOW", genuine curiosity
  7-8: Clear motivation, one concrete example, no throat-clearing
  5-6: Dry, generic, tells what not why
  <=4: Starts "This section covers..." or missing big-picture callout

ONLY edit if score <= 6. Rewrite to: open with a concrete scene or striking claim,
explain why this matters for embodied AI right now, promise what reader will do.
80-150 words. NEVER start with "This section" or "In this section".
Edit the file directly only if rewriting. NEVER use em dashes or double dashes.
Return "PASS X/10" or "FIXED X->9/10: [what changed]".`,
  { label: `hook-${t.sec}`, phase: 'Wave 9 - Hooks' }
))
log('Wave 9 complete.')

phase('Wave 10 - Prose')
log(`Fixing dense paragraphs in ${W10_TARGETS.length} sections...`)
await pipeline(W10_TARGETS, async (t) => agent(
  `You are the Readability and Pacing Editor (#32). Section ${t.sec}: ${t.title}
File: ${t.path}

This section has paragraphs over 180 words. Fix using the best option:
  (A) Split into two paragraphs with a bridging sentence
  (B) Extract list items into <ul> or <ol>
  (C) Pull a sub-concept into a key-insight callout, shorten the paragraph
  (D) Add a mini h3 heading to create breathing room
Also: fix any 4+ consecutive paragraphs without a visual break.
Edit the file directly. Return one-line summary. No em dashes.`,
  { label: `prose-${t.sec}`, phase: 'Wave 10 - Prose' }
))
log('Wave 10 complete.')

phase('Wave 11 - Aha')
log(`Adding aha-moments and key phrases to ${ALL_SECTIONS.length} sections...`)
await pipeline(ALL_SECTIONS, async (t) => agent(
  `You are the Aha-Moment Engineer (#24) and Memorability Designer (#29). Section ${t.sec}: ${t.title}
File: ${t.path}

TWO inline tasks (NOT new callout boxes):

1. AHA MOMENT: If missing, add a striking inline comparison — concrete numbers, scale,
   or physical analogy. E.g.: "Without reward shaping: 10,000 episodes. With it: 200."
   Skip if a strong aha moment already exists.

2. MEMORABLE PHRASE: If no bolded key phrase exists mid-sentence, add one (3-7 words).
   E.g.: "...this is called <strong>the sim-to-real gap</strong>, and..."
   Skip if one already exists.

Edit directly (may be zero changes if both present). No em dashes.
Return: "AHA: [added/present]; PHRASE: [added/present]"`,
  { label: `aha-${t.sec}`, phase: 'Wave 11 - Aha' }
))
log('Waves 9-11 complete!')
return { waves_complete: ['9-hooks', '10-prose', '11-aha-memorability'] }
"""
)

out = ROOT / 'waves9to11_fixed.js'
out.write_text(SCRIPT, encoding='utf-8')
print(f'waves9to11_fixed.js: {len(SCRIPT):,} chars — under 512k: {len(SCRIPT) < 524288}')
