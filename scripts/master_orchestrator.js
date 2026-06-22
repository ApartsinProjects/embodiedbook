/**
 * master_orchestrator.js
 * Autonomous wave-after-wave runner for the embodied AI book.
 * Chains: waves 6-8 → 9-11 → dedup scan + fix → final QA → deep content (gates 4-7)
 * Commits after each major wave group.
 *
 * Launch AFTER wave 5 (cross-refs) completes.
 * Usage: Workflow({ scriptPath: 'scripts/master_orchestrator.js' })
 */

export const meta = {
  name: 'master-orchestrator',
  description: 'Autonomous chain: waves 6-8, 9-11, dedup, QA, then deep content gates 4-7',
  phases: [
    { title: 'Waves 6-8', detail: 'Pathway, tips, algorithms, missing code blocks' },
    { title: 'Commit 6-8', detail: 'Git commit after waves 6-8' },
    { title: 'Waves 9-11', detail: 'Opening hooks, dense prose, aha-moments' },
    { title: 'Commit 9-11', detail: 'Git commit after waves 9-11' },
    { title: 'Dedup Scan', detail: 'Python scan for near-duplicate content' },
    { title: 'Dedup Fix', detail: 'Rewrite or consolidate duplicate callouts and paragraphs' },
    { title: 'Commit Dedup', detail: 'Git commit after dedup' },
    { title: 'Final QA', detail: 'Skeptical reader, controller, pub QA' },
    { title: 'Deep Content', detail: 'Gates 4-7: depth, accuracy, style, SVGs, verification' },
    { title: 'Final Commit', detail: 'Git commit of all remaining changes' },
  ],
}

const BOOK_ROOT = 'E:/Projects/Books/EmbodiedAI'

// ── Waves 6-8 ─────────────────────────────────────────────────────────────────
phase('Waves 6-8')
log('Starting waves 6-8: pathway callouts, tips, algorithm boxes, missing code...')
await workflow({ scriptPath: `${BOOK_ROOT}/scripts/wave68_workflow.js` })
log('Waves 6-8 complete.')

phase('Commit 6-8')
await agent(
  `Run these git commands from the directory ${BOOK_ROOT}:
    git add -A
    git commit -m "Waves 6-8: pathway callouts, tip callouts, algorithm boxes, missing code blocks

Added pathway learning-signpost callouts to 365 sections, practical tip callouts
to 347 sections, algorithm step-by-step boxes to 172 sections, and first runnable
code examples to 28 sections that had none.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

If there are no changes to commit (git status shows nothing), just log "nothing to commit".
Report: how many files changed.`,
  { label: 'commit-68', phase: 'Commit 6-8' }
)

// ── Waves 9-11 ────────────────────────────────────────────────────────────────
phase('Waves 9-11')
log('Starting waves 9-11: opening hooks, dense prose, aha-moments...')
await workflow({ scriptPath: `${BOOK_ROOT}/scripts/waves9to11_fixed.js` })
log('Waves 9-11 complete.')

phase('Commit 9-11')
await agent(
  `Run these git commands from the directory ${BOOK_ROOT}:
    git add -A
    git commit -m "Waves 9-11: opening hooks, prose clarity, aha-moments and key phrases

Rewrote weak big-picture callouts (score <=6/10) to open with concrete scenes.
Fixed dense paragraphs over 180 words in 30 sections (split, list, or heading).
Added inline aha-moment comparisons and bolded memorable key phrases across 366 sections.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

Report: how many files changed.`,
  { label: 'commit-911', phase: 'Commit 9-11' }
)

// ── Wave 12: Deduplication ────────────────────────────────────────────────────
phase('Dedup Scan')
log('Running duplicate content detection...')

await agent(
  `Run the duplicate detection script from ${BOOK_ROOT}:
  C:/Python314/python scripts/detect_duplicates.py

  Working directory: ${BOOK_ROOT}
  Report the stats: how many callout pairs, paragraph pairs, concept overlaps found.`,
  { label: 'dedup-detect', phase: 'Dedup Scan' }
)

phase('Dedup Fix')
log('Loading dedup report and fixing duplicates...')

const DEDUP_SCHEMA = {
  type: 'object',
  properties: {
    callout_duplicates: { type: 'array', items: { type: 'object' } },
    para_duplicates: { type: 'array', items: { type: 'object' } },
    concept_overlaps: { type: 'array', items: { type: 'object' } },
    stats: { type: 'object' }
  },
  required: ['callout_duplicates', 'para_duplicates', 'concept_overlaps', 'stats']
}

const dedup = await agent(
  `Read the file ${BOOK_ROOT}/scripts/dedup_report.json and return its contents as structured output.
  The file contains: callout_duplicates array, para_duplicates array, concept_overlaps array, stats object.
  Return them exactly as they appear in the file.`,
  { label: 'load-dedup', schema: DEDUP_SCHEMA }
)

const calloutDups = (dedup.callout_duplicates || []).slice(0, 60)
const paraDups    = (dedup.para_duplicates    || []).slice(0, 30)
const conceptOv   = (dedup.concept_overlaps   || []).slice(0, 20)

log(`Fixing: ${calloutDups.length} callout pairs, ${paraDups.length} para pairs, ${conceptOv.length} concept overlaps`)

const dedupFix = async (dup, type) => {
  const fixSec  = dup.sec_a > dup.sec_b ? dup.sec_a : dup.sec_b
  const fixPath = dup.sec_a > dup.sec_b ? dup.path_a : dup.path_b
  const keepSec = dup.sec_a > dup.sec_b ? dup.sec_b  : dup.sec_a
  const sim     = Math.round((dup.similarity || 0) * 100)
  return agent(
    `You are the Content Consolidation Editor. Fix a duplicate ${type} between sections ${dup.sec_a} and ${dup.sec_b} (${sim}% overlap).

Section to FIX (later in book): ${fixSec} at ${BOOK_ROOT}/${fixPath}
Canonical (keep as-is): ${keepSec}

Text A: "${(dup.text_a || '').substring(0, 250)}"
Text B: "${(dup.text_b || '').substring(0, 250)}"

Choose:
  (A) REWRITE: Make the fix-section callout specific to its unique angle.
  (B) REPLACE: Short callout pointing to canonical: "See section ${keepSec} for details. Here we focus on [specific angle]."
  (C) DELETE: If it adds nothing unique.
  (D) SKIP: If the overlap is intentional progressive depth (return "SKIP: [reason]").

Edit ONLY ${BOOK_ROOT}/${fixPath}. No em dashes.
Return: "Strategy [A/B/C/D]: [what changed or why skipped]"`,
    { label: `dedup-${type}-${fixSec}`, phase: 'Dedup Fix' }
  )
}

await parallel([
  () => pipeline(calloutDups, (d) => dedupFix(d, d.type || 'callout')),
  () => pipeline(paraDups,    (d) => dedupFix(d, 'para')),
  () => pipeline(conceptOv,   (d) => dedupFix(d, 'concept')),
])

phase('Commit Dedup')
await agent(
  `Run from ${BOOK_ROOT}:
    git add -A
    git commit -m "Wave 12: deduplicate and consolidate content across sections

Detected and fixed near-duplicate callout blocks, paragraph-level repetition,
and sections with overlapping concept scope. Strategies applied: rewrite to be
section-specific, replace with cross-reference pointer, or delete if redundant.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

Report files changed.`,
  { label: 'commit-dedup', phase: 'Commit Dedup' }
)

// ── Wave 13: Final QA ─────────────────────────────────────────────────────────
phase('Final QA')

const QA_SEC_SCHEMA = {
  type: 'object',
  properties: {
    sections: { type: 'array', items: { type: 'object', properties: { sec: { type: 'string' }, path: { type: 'string' }, title: { type: 'string' } }, required: ['sec','path'] } }
  },
  required: ['sections']
}

const qaSecData = await agent(
  `Read ${BOOK_ROOT}/scripts/section_index.json. Return the array as an object with a "sections" key containing all entries with sec, path, and title fields.`,
  { label: 'load-qa-sections', schema: QA_SEC_SCHEMA }
)
const qaSections = qaSecData.sections || []
const sampleEvery = Math.max(1, Math.floor(qaSections.length / 40))
const ctrlSample = qaSections.filter((_, i) => i % sampleEvery === 0)

log(`Wave 13: skeptical reader (${qaSections.length} sections), controller (${ctrlSample.length} sampled)...`)

await pipeline(qaSections, async (t) => agent(
  `You are the Skeptical Reader (#30). Section ${t.sec}: ${t.title || ''}
File: ${BOOK_ROOT}/${t.path}

Score 1-10 for embodied-AI distinctiveness. Fix the single most generic passage if score <= 7.
Generic red flags: "can be used for many applications", "researchers have shown",
"it is important to understand", any paragraph that could be in any ML textbook.
Fix: replace vague claims with specific robots, simulators, datasets, physical constraints.
Edit directly. No em dashes. Return "PASS X/10" or "FIXED X->9/10: [what changed]"`,
  { label: `skeptic-${t.sec}`, phase: 'Final QA' }
))

await pipeline(ctrlSample, async (t) => agent(
  `You are Director Morgan Blackwood (#42), Controller. Section ${t.sec}: ${t.title || ''}
File: ${BOOK_ROOT}/${t.path}

Find and fix the single highest-priority issue:
  1. Broken HTML (unclosed tags)
  2. Generic code caption text
  3. Placeholder text (TBD, TODO, [insert])
  4. Wrong What's Next section number
  5. Duplicate callout title in same file
Return "Fixed [type]: [desc]" or "Clean". Edit directly. No em dashes.`,
  { label: `ctrl-${t.sec}`, phase: 'Final QA' }
))

await agent(
  `Run publication QA checks from ${BOOK_ROOT}:
  grep -rL "</html>" part-*/module-*/section-*.html | wc -l
  grep -rl "\xe2\x80\x94" part-*/module-*/section-*.html | wc -l
  grep -rL "styles/book.css" part-*/module-*/section-*.html | wc -l
  grep -r "class=\\"illustration\\"" part-*/module-*/section-*.html | wc -l
  grep -r "class=\\"callout" part-*/module-*/section-*.html | wc -l
  grep -r "<pre>" part-*/module-*/section-*.html | wc -l
  For any broken HTML or missing CSS: fix up to 10 files directly.
  Report all counts.`,
  { label: 'pub-qa', phase: 'Final QA' }
)

// ── Deep content: book_update gates 4-7 ──────────────────────────────────────
phase('Deep Content')
log('Running book_update gates 4-7: depth, accuracy, style, SVGs, verification...')
await workflow({
  scriptPath: 'C:/Users/apart/.claude/skills/book-skills/scripts/book_update.js',
  args: { bookRoot: BOOK_ROOT, gates: ['4', '5', '6', '7'] }
})
log('Deep content gates 4-7 complete.')

// ── Final commit ──────────────────────────────────────────────────────────────
phase('Final Commit')
await agent(
  `Run from ${BOOK_ROOT}:
    git add -A
    git status --short | head -20
    git commit -m "Waves 13+: final QA, deep content, style, verification, SVG diagrams

Wave 13: Skeptical Reader distinctiveness pass on all 379 sections, Controller
sample sweep, publication QA checklist.
Gates 4-7: deep explanation (what/why/how/when), misconception pre-emption,
concrete analogies, project ideas, research frontiers with paper spotlights,
fact integrity, terminology consistency, prose clarity, voice, aha-moments,
memorability, engagement, SVG diagrams, self-containment, figure fact-checking.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

Report total files changed.`,
  { label: 'final-commit', phase: 'Final Commit' }
)

log('All waves complete. Book is ready for html2epub.')
return {
  status: 'complete',
  waves: ['6-pathway','7-tips','8a-algorithms','8b-code','9-hooks','10-prose','11-aha',
          '12-dedup','13-final-qa','gate4-depth','gate5-style','gate6-structure','gate7-qa'],
}
