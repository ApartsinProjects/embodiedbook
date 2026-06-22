"""
Generate wave 5 and waves 6-8 workflow JS scripts with all data embedded.
Run: C:/Python314/python scripts/build_wave_workflows.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent

d = json.loads((SCRIPTS / '_wf_data.json').read_text(encoding='utf-8'))

SHORT_MAP = d['short_map']
SEC_PATHS = json.dumps(d['sec_paths'], ensure_ascii=False)
W5 = json.dumps(d['w5'], ensure_ascii=False)
W6 = json.dumps(d['w6'], ensure_ascii=False)
W7 = json.dumps(d['w7'], ensure_ascii=False)
W8A = json.dumps(d['w8a'], ensure_ascii=False)
W8B = json.dumps(d['w8b'], ensure_ascii=False)

# ── Wave 5: Cross-References ──────────────────────────────────────────────────
wave5_script = r"""export const meta = {
  name: 'wave-5-cross-refs',
  description: 'Wave 5: insert 3-6 inline cross-reference links into 253 sections',
  phases: [{ title: 'Cross-refs', detail: '253 sections get inline hyperlinks to related sections' }],
}

const SHORT_MAP = `""" + SHORT_MAP.replace('`', r'\`') + r"""`

const SEC_PATHS = """ + SEC_PATHS + r"""

const W5_TARGETS = """ + W5 + r"""

phase('Cross-refs')
log(`Inserting cross-refs into ${W5_TARGETS.length} sections...`)

await pipeline(
  W5_TARGETS,
  async (t) => {
    const sec = t.sec
    const path = t.path
    return agent(
      `You are the Cross-Reference Architect (#13) for an embodied AI textbook.

TASK: Insert 3 to 6 inline cross-reference links into section ${sec}.

File: ${path}

SECTION MAP (number: short title):
${SHORT_MAP}

PATH LOOKUP — to get the full path of any section, use this rule:
  The href is always: ../../{full_path_from_book_root}
  You can derive paths: section X.Y is in module-0X-... under part-N-...
  Use the SHORT_MAP to identify related sections, then construct the path by looking at
  the pattern: section 1.x is in part-1.../module-01..., section 10.x is in part-3.../module-10-..., etc.

ACTUAL PATH EXAMPLES from the book:
  1.1 -> part-1-foundations-of-embodied-ai/module-01-from-static-ai-to-embodied-ai/section-1.1.html
  2.3 -> part-1-foundations-of-embodied-ai/module-02-the-agent-environment-interface/section-2.3.html
  10.3 -> part-3-simulation-tooling-and-the-modern-stack/module-10-environments-with-gymnasium-and-pettingzoo/section-10.3.html
  33.2 -> part-7-language-vision-and-action/module-33-llms-as-planners-and-controllers/section-33.2.html

INSTRUCTIONS:
1. Read file "${path}"
2. Identify 3-6 concepts in the prose that are covered in OTHER sections
3. For each, wrap a natural phrase in: <a href="../../{target_path}">{phrase}</a>
4. Spread links across different paragraphs (max 2 per paragraph)
5. Skip: code blocks, headings, nav footer, epigraph, figure captions
6. Look up the EXACT target path from the book's file structure (read a nearby file if needed to confirm)
7. Edit the file directly with Edit tool
8. NEVER use em dashes or double dashes

Return: "Added N links to: [list of sections]"`,
      { label: `xref-${sec}`, phase: 'Cross-refs' }
    )
  }
)

log('Wave 5 complete!')
return { wave: '5-cross-refs', sections_processed: W5_TARGETS.length }
"""

# ── Waves 6-8: Pathway, Tips, Algorithms, Code ───────────────────────────────
waves68_script = r"""export const meta = {
  name: 'waves-6-to-8',
  description: 'Waves 6-8: pathway callouts, tip callouts, algorithm boxes, missing code blocks',
  phases: [
    { title: 'Wave 6 - Pathway', detail: '365 sections get a learning-path signpost' },
    { title: 'Wave 7 - Tips', detail: '347 sections get a practical tip callout' },
    { title: 'Wave 8a - Algorithms', detail: '172 sections get an algorithm box' },
    { title: 'Wave 8b - Code', detail: '28 sections get their first code block' },
  ],
}

const W6 = """ + W6 + r"""
const W7 = """ + W7 + r"""
const W8A = """ + W8A + r"""
const W8B = """ + W8B + r"""

// ── Wave 6: Pathway callouts ─────────────────────────────────────────────────
phase('Wave 6 - Pathway')
log(`Adding pathway callouts to ${W6.length} sections...`)

await pipeline(W6, async (t) => {
  return agent(
    `You are the Teaching Flow Reviewer (#03) adding a "pathway" callout.

TASK: Add ONE pathway callout to section ${t.sec}.
File: ${t.path}
Title: ${t.title}

A pathway callout (2-4 sentences) does ONE of:
  (a) Prerequisites: "This section assumes familiarity with [specific concept] from section X.Y."
  (b) Skip path: "If you already know [concept], skip to section X.Y."
  (c) Forward: "The ideas here are extended in section X.Y and X.Z."
  (d) Connections: "This technique recurs in Part N alongside [related concept]."

Use real section numbers. Be specific — not "earlier chapters" but "section 2.3."

HTML (insert after <figure class="illustration"> or after epigraph, before first <h2>):
<div class="callout pathway">
<p>[2-4 sentences with specific section numbers]</p>
</div>

1. Read file "${t.path}"
2. Check prerequisites and what this section leads to
3. Write and insert the pathway callout
4. Edit the file directly — NOT a report
5. NEVER use em dashes or double dashes

Return: one-line summary.`,
    { label: `pathway-${t.sec}`, phase: 'Wave 6 - Pathway' }
  )
})

log('Wave 6 complete.')

// ── Wave 7: Tip callouts ──────────────────────────────────────────────────────
phase('Wave 7 - Tips')
log(`Adding tip callouts to ${W7.length} sections...`)

await pipeline(W7, async (t) => {
  return agent(
    `You are the Senior Developmental Editor (#17) adding a practical "tip" callout.

TASK: Add ONE tip callout to section ${t.sec}.
File: ${t.path}
Title: ${t.title}

A tip callout (2-5 sentences) must:
- Name a specific tool, library, parameter, or decision criterion
- Address a common gotcha, best practice, or non-obvious shortcut
- NOT restate the main text

Good tips name specifics: "Isaac Lab requires .contiguous()" not "use the right tensor format."

HTML (insert after the most relevant explanation):
<div class="callout tip">
<p>[2-5 sentences of concrete, specific, actionable advice]</p>
</div>

1. Read file "${t.path}"
2. Identify the most important practical gotcha or shortcut
3. Write a concrete, specific tip and insert it
4. Edit the file directly
5. NEVER use em dashes or double dashes

Return: one-line summary of tip added.`,
    { label: `tip-${t.sec}`, phase: 'Wave 7 - Tips' }
  )
})

log('Wave 7 complete.')

// ── Wave 8a: Algorithm callouts ───────────────────────────────────────────────
phase('Wave 8a - Algorithms')
log(`Adding algorithm callouts to ${W8A.length} sections...`)

await pipeline(W8A, async (t) => {
  return agent(
    `You are the Code Pedagogy Engineer (#08) adding an algorithm callout.

TASK: Add ONE algorithm callout to section ${t.sec}.
File: ${t.path}
Title: ${t.title}

An algorithm callout: specific title, 5-12 numbered steps, clear actions, math notation (θ, α, π, ∇).
Include INPUT/OUTPUT lines. For conceptual sections: use a Decision Checklist format.

HTML (near the key explanation):
<div class="callout algorithm">
<h4>Algorithm: [Specific name]</h4>
<p><strong>Input:</strong> [inputs]</p>
<p><strong>Output:</strong> [outputs]</p>
<ol>
<li>[Step 1 — concrete action]</li>
<li>[Step 2]</li>
</ol>
</div>

1. Read file "${t.path}"
2. Identify the main procedure
3. Write and insert the algorithm box
4. Edit the file directly
5. NEVER use em dashes or double dashes

Return: one-line summary.`,
    { label: `alg-${t.sec}`, phase: 'Wave 8a - Algorithms' }
  )
})

// ── Wave 8b: Missing code blocks ─────────────────────────────────────────────
log(`Adding first code block to ${W8B.length} zero-code sections...`)

await pipeline(W8B, async (t) => {
  return agent(
    `You are the Code Pedagogy Engineer (#08) adding the first code example.

TASK: Add ONE runnable code block to section ${t.sec} (currently has ZERO code).
File: ${t.path}
Title: ${t.title}

Requirements: runnable Python (PyTorch/NumPy/Gymnasium/MuJoCo/LeRobot), 20-60 lines,
specific opening comment, code-output div, code-caption BELOW (never above).

HTML:
<pre><code class="language-python"># [Specific description of what this demonstrates]
[code]
</code></pre>
<div class="code-output"><pre>[expected output]</pre></div>
<div class="code-caption">Code Fragment ${t.sec}.1: [Specific description]</div>

1. Read file "${t.path}"
2. Write a minimal runnable example for the core concept
3. Place in the most relevant location
4. Edit the file directly
5. NEVER use em dashes or double dashes

Return: one-line summary.`,
    { label: `code-${t.sec}`, phase: 'Wave 8a - Algorithms' }
  )
})

log('Waves 6-8 all complete!')
return { waves_complete: ['6-pathway', '7-tips', '8a-algorithms', '8b-code'] }
"""

out5 = ROOT / 'scripts' / 'wave5_workflow.js'
out68 = ROOT / 'scripts' / 'wave68_workflow.js'

out5.write_text(wave5_script, encoding='utf-8')
out68.write_text(waves68_script, encoding='utf-8')

print(f'wave5_workflow.js: {len(wave5_script):,} chars')
print(f'wave68_workflow.js: {len(waves68_script):,} chars')
print('Both under 524288 limit:', len(wave5_script) < 524288 and len(waves68_script) < 524288)
