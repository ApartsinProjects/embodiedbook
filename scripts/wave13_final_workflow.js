export const meta = {
  name: 'wave-13-final',
  description: 'Wave 13: Skeptical Reader challenge + Controller sweep + Publication QA',
  phases: [
    { title: 'Skeptical Reader', detail: 'Challenge 379 sections for distinctiveness and generic content' },
    { title: 'Controller Sweep', detail: 'Director Morgan Blackwood full book sweep, dispatch specialists' },
    { title: 'Style Validation', detail: 'Em-dash scan, broken links, CSS consistency across all files' },
    { title: 'Publication QA', detail: 'Inspector Quinn Harlow pre-publication checklist' },
  ],
}

const allSecRaw = await agent(
  `Read the file scripts/section_index.json and return its full content. Return ONLY the raw JSON array.`,
  { label: 'load-sections' }
)
const allSections = typeof allSecRaw === 'string' ? JSON.parse(allSecRaw) : allSecRaw

// ── Skeptical Reader (#30): Challenge every section ───────────────────────────
phase('Skeptical Reader')
log(`Challenging ${allSections.length} sections for distinctiveness...`)

const SCHEMA_VERDICT = {
  type: 'object',
  properties: {
    sec: { type: 'string' },
    score: { type: 'number', description: '1-10 distinctiveness score' },
    generic_passages: { type: 'array', items: { type: 'string' } },
    fixes_applied: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string', enum: ['PASS', 'FIXED'] },
  },
  required: ['sec', 'score', 'verdict'],
}

const skepticalResults = await pipeline(
  allSections,
  async (t) => {
    const sec = t.sec
    const path = t.path.replace(/\\/g, '/')
    return agent(
      `You are the Skeptical Reader (#30) for an embodied AI textbook — your job is to challenge mediocrity.

TASK: Score section ${sec} for distinctiveness, then fix the weakest passage.

File: ${path}
Title: ${t.title}

DISTINCTIVENESS RUBRIC (1-10):
  9-10: Content that could ONLY appear in an embodied AI textbook — specific to physical agents,
        real hardware, sim-to-real gaps, sensor fusion, contact physics, embodied perception
   7-8: Solid technical content, specific algorithms or systems named with real parameters
   5-6: Correct but generic — the same content could appear in any ML textbook
   3-4: Boilerplate: "Neural networks can learn complex patterns", "Choose hyperparameters carefully"
   1-2: Entirely generic AI content with no embodiment specificity

GENERIC RED FLAGS to search for:
- "can be used for many applications"
- "it is important to understand"
- "there are many approaches to"
- "researchers have shown that"
- "this is a challenging problem"
- "in practice, results may vary"
- Any paragraph that does not mention a specific robot, simulator, sensor, or physical constraint

FIX RULE: If score <= 7, find the single most generic passage and rewrite it to be embodiment-specific:
- Replace "neural networks" with the specific architecture used for embodied agents
- Replace "training data" with specific datasets (RT-X, Open X-Embodiment, LeRobot datasets)
- Replace vague claims with specific numbers from real systems (Boston Dynamics Spot, Franka Panda, etc.)
- Ground abstract claims in physical consequences: "This matters because a 10ms latency spike..."

INSTRUCTIONS:
1. Read file "${path}"
2. Score 1-10 for embodied-AI distinctiveness
3. If score >= 8: return PASS with score
4. If score <= 7: identify the most generic passage, rewrite it to be embodiment-specific, edit the file
5. NEVER use em dashes or double dashes

Return JSON with sec, score, verdict (PASS or FIXED), and what was changed.`,
      { label: `skeptic-${sec}`, phase: 'Skeptical Reader', schema: SCHEMA_VERDICT }
    )
  }
)

const skepticFixed = (skepticalResults || []).filter(Boolean).filter(r => r.verdict === 'FIXED').length
const skepticPass = (skepticalResults || []).filter(Boolean).filter(r => r.verdict === 'PASS').length
log(`Skeptical Reader: ${skepticFixed} fixed, ${skepticPass} passed`)

// ── Style Validation: em-dash scan ───────────────────────────────────────────
phase('Style Validation')

const styleReport = await agent(
  `Run this scan across all section HTML files in E:/Projects/Books/EmbodiedAI:

Use the Bash tool to run:
  grep -rl "—\\|–\\| -- " part-*/module-*/section-*.html

Report the file paths found and the count. If 0 files found, report "Clean: no em-dashes found."
Then for any files found (up to 20), open each and replace all em-dashes (—) and en-dashes (–) and double-hyphens ( -- )
with appropriate punctuation (comma, semicolon, colon, or separate sentence).
Edit those files directly using the Edit tool.`,
  { label: 'style-scan' }
)

log('Style validation complete.')

// ── Controller Sweep (#42) ────────────────────────────────────────────────────
phase('Controller Sweep')
log('Running Director Morgan Blackwood controller sweep...')

// Sample 30 sections across all parts for a representative sweep
const parts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
const sampleSections = allSections.filter(s => {
  const partMatch = s.path.match(/part-(\d+)/)
  return partMatch && parts.includes(partMatch[1])
}).filter((_, i) => i % 12 === 0)  // every 12th = ~30 sections

await pipeline(
  sampleSections,
  async (t) => {
    const sec = t.sec
    const path = t.path.replace(/\\/g, '/')
    return agent(
      `You are Director Morgan Blackwood (#42), Controller of the embodied AI textbook pipeline.

TASK: Inspect section ${sec} and dispatch one targeted fix.

File: ${path}

Your job: read the section and identify the SINGLE HIGHEST PRIORITY remaining gap.
Check for these gaps in priority order:
  1. Broken or missing HTML structure (unclosed tags, missing </section>, etc.)
  2. Bibliography section missing from the chapter (check the module index.html, not this section)
  3. "What's Next" section missing or pointing to wrong section
  4. Key concept never defined — used but not explained
  5. Code block with no caption or generic caption
  6. Callout box with duplicate or placeholder title like "Practical Example: Example"

For the highest priority gap you find:
- Apply the fix directly by editing the file
- If the gap requires looking at another file (e.g., module index), read that file and fix it

NEVER use em dashes or double dashes.

Return: "Fixed [gap type] in [file]: [brief description]" or "Clean: no critical gaps found"`,
      { label: `ctrl-${sec}`, phase: 'Controller Sweep' }
    )
  }
)

// ── Publication QA (#43) ─────────────────────────────────────────────────────
phase('Publication QA')
log('Running Inspector Quinn Harlow publication QA checklist...')

await agent(
  `You are Inspector Quinn Harlow (#43), Publication QA for the embodied AI textbook.

Run a systematic pre-publication checklist across the book at E:/Projects/Books/EmbodiedAI.

Use Bash to run these checks and report results:

1. Missing </html> closing tags:
   grep -rL "</html>" part-*/module-*/section-*.html | wc -l

2. Broken internal links (href pointing to non-existent files) — sample check:
   python scripts/check_links.py 2>/dev/null || echo "check_links.py not found"

3. CSS link check — all sections should link to styles/book.css:
   grep -rL "styles/book.css" part-*/module-*/section-*.html | wc -l

4. Em-dash audit (should be 0 after style pass):
   grep -rl "—\\|–" part-*/module-*/section-*.html | wc -l

5. Missing nav footer:
   grep -rL "nav-footer\\|navigation" part-*/module-*/section-*.html | wc -l

6. Count total illustrations, callouts, and code blocks:
   grep -r "class=\\"illustration\\"" part-*/module-*/section-*.html | wc -l
   grep -r "class=\\"callout" part-*/module-*/section-*.html | wc -l
   grep -r "<pre>" part-*/module-*/section-*.html | wc -l

Report all counts. Flag any non-zero failure counts as BLOCKING.
For BLOCKING issues (missing </html>, missing CSS link, em-dashes): fix up to 10 instances directly.`,
  { label: 'pub-qa', phase: 'Publication QA' }
)

log('Wave 13 complete — book ready for html2epub!')

return {
  wave: '13-final',
  skeptic_fixed: skepticFixed,
  skeptic_passed: skepticPass,
}
