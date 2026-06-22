export const meta = {
  name: 'wave-12-dedup',
  description: 'Wave 12: deduplicate and consolidate content across all 379 sections',
  phases: [
    { title: 'Detect', detail: 'Python scan for near-duplicate callouts and paragraphs' },
    { title: 'Fix Callouts', detail: 'Rewrite duplicate callout blocks to be section-specific' },
    { title: 'Fix Paragraphs', detail: 'Consolidate duplicate paragraph explanations with cross-refs' },
    { title: 'Concept Overlaps', detail: 'Fix sections with too-similar big-picture scope' },
  ],
}

// ── Phase 1: Run detection script ─────────────────────────────────────────────
phase('Detect')
log('Running duplicate detection script across all sections...')

await agent(
  `Run the Python detection script:
  C:/Python314/python scripts/detect_duplicates.py

  The working directory is E:/Projects/Books/EmbodiedAI. Run it from there.
  Report the stats output (how many duplicates found in each category).`,
  { label: 'run-detect-script' }
)

// ── Phase 2: Load report ──────────────────────────────────────────────────────
const reportRaw = await agent(
  `Read the file scripts/dedup_report.json and return its full content. Return ONLY the raw JSON, nothing else.`,
  { label: 'load-dedup-report' }
)
const report = typeof reportRaw === 'string' ? JSON.parse(reportRaw) : reportRaw

log(`Detection complete: ${report.stats.callout_dup_pairs} callout pairs, ${report.stats.para_dup_pairs} paragraph pairs, ${report.stats.concept_overlap_pairs} concept overlaps`)

// ── Phase 3: Fix duplicate callout blocks ────────────────────────────────────
phase('Fix Callouts')

const calloutDups = report.callout_duplicates || []
log(`Fixing ${calloutDups.length} duplicate callout pairs...`)

if (calloutDups.length > 0) {
  // Deduplicate: each section only appears once as the "fix" target
  // Pick the one to fix: prefer fixing sec_b (keep sec_a as canonical)
  const fixTargets = new Map()
  for (const dup of calloutDups) {
    // Track which section we're fixing — prefer fixing the one later in the book
    const fixSec = dup.sec_a > dup.sec_b ? dup.sec_a : dup.sec_b
    const fixPath = dup.sec_a > dup.sec_b ? dup.path_a : dup.path_b
    const keepSec = dup.sec_a > dup.sec_b ? dup.sec_b : dup.sec_a
    const keepPath = dup.sec_a > dup.sec_b ? dup.path_b : dup.path_a
    const key = `${dup.type}:${fixSec}`
    if (!fixTargets.has(key)) {
      fixTargets.set(key, { ...dup, fix_sec: fixSec, fix_path: fixPath, keep_sec: keepSec, keep_path: keepPath })
    }
  }

  const toFix = Array.from(fixTargets.values())
  log(`Unique fix targets: ${toFix.length}`)

  await pipeline(
    toFix,
    async (dup) => {
      return agent(
        `You are the Content Consolidation Editor for an embodied AI textbook.

TASK: Fix a duplicate ${dup.type} callout in section ${dup.fix_sec}.

Section to FIX: ${dup.fix_sec} at ${dup.fix_path}
Canonical version (KEEP AS-IS): section ${dup.keep_sec} at ${dup.keep_path}

The two callouts have ${Math.round(dup.similarity * 100)}% word overlap — too similar.

DUPLICATE CONTENT:
Section ${dup.fix_sec} text: "${dup.text_a.substring(0, 300)}"
Section ${dup.keep_sec} text: "${dup.text_b.substring(0, 300)}"

FIX STRATEGY — choose the best option:
  (A) REWRITE: Keep the ${dup.type} callout but make it specific to section ${dup.fix_sec}'s unique angle.
      The rewrite must cover a DIFFERENT aspect of the concept than section ${dup.keep_sec}.
  (B) REPLACE WITH CROSS-REF: Remove the duplicate callout body and replace with a brief callout
      pointing to section ${dup.keep_sec}:
      <div class="callout ${dup.type}">
      <p>See section ${dup.keep_sec} for a detailed treatment of [concept]. Here we focus on [what makes this section different].</p>
      </div>
  (C) DELETE: If the callout adds nothing unique to section ${dup.fix_sec}, remove it entirely.

DECISION RULE:
- If the concepts are identical and section ${dup.fix_sec} cannot say something meaningfully different → (B) or (C)
- If the same technique is applied differently in this section's context → (A)
- If it is a tip or algorithm that is section-specific → (A)

INSTRUCTIONS:
1. Read BOTH files
2. Decide: can section ${dup.fix_sec}'s callout be meaningfully differentiated?
3. Apply the chosen strategy
4. Edit ONLY file ${dup.fix_path}
5. NEVER use em dashes or double dashes

Return: "Strategy [A/B/C]: [what changed in section ${dup.fix_sec}]"`,
        { label: `dedup-callout-${dup.fix_sec}-${dup.type}`, phase: 'Fix Callouts' }
      )
    }
  )
}

// ── Phase 4: Fix duplicate paragraphs ────────────────────────────────────────
phase('Fix Paragraphs')

const paraDups = report.para_duplicates || []
log(`Fixing ${paraDups.length} duplicate paragraph pairs...`)

if (paraDups.length > 0) {
  const paraFixTargets = new Map()
  for (const dup of paraDups) {
    const fixSec = parseFloat(dup.sec_a) > parseFloat(dup.sec_b) ? dup.sec_a : dup.sec_b
    const fixPath = parseFloat(dup.sec_a) > parseFloat(dup.sec_b) ? dup.path_a : dup.path_b
    const keepSec = parseFloat(dup.sec_a) > parseFloat(dup.sec_b) ? dup.sec_b : dup.sec_a
    const key = `para:${fixSec}:${dup.text_a.substring(0, 40)}`
    if (!paraFixTargets.has(key)) {
      paraFixTargets.set(key, { ...dup, fix_sec: fixSec, fix_path: fixPath, keep_sec: keepSec })
    }
  }

  const toFix = Array.from(paraFixTargets.values())
  log(`Unique paragraph fix targets: ${toFix.length}`)

  await pipeline(
    toFix,
    async (dup) => {
      return agent(
        `You are the Content Consolidation Editor for an embodied AI textbook.

TASK: Fix a near-duplicate paragraph explanation in section ${dup.fix_sec}.

Section to FIX: ${dup.fix_sec} at ${dup.fix_path}
Canonical explanation: section ${dup.keep_sec}

The two paragraphs have ${Math.round(dup.similarity * 100)}% word overlap.

Section ${dup.fix_sec} paragraph:
"${dup.text_a.substring(0, 400)}"

Section ${dup.keep_sec} paragraph:
"${dup.text_b.substring(0, 400)}"

IMPORTANT CONTEXT: Some overlap is INTENTIONAL and CORRECT:
- Progressive depth: section ${dup.fix_sec} may revisit a concept from ${dup.keep_sec} at a deeper level
- Prerequisite recap: a brief reminder is fine (1-2 sentences max)
- Terminology definitions: a section may need to define a term even if another section defined it

DECISION:
1. Read BOTH paragraphs in context
2. If the overlap is intentional progressive depth or a necessary brief recap → SKIP (return "SKIP: intentional overlap")
3. If it is pure repetition of the same content at the same depth → SHORTEN the paragraph in section ${dup.fix_sec}:
   - Cut the repeated explanation to 1-2 reminder sentences
   - Add: "For a full derivation, see <a href='../../${dup.keep_sec === dup.path_b ? 'PATH' : dup.path_b}'>section ${dup.keep_sec}</a>."
   - Focus the rest of the paragraph on what is unique to section ${dup.fix_sec}'s context

4. Edit ONLY file ${dup.fix_path}
5. NEVER use em dashes or double dashes

Return: "FIXED: [what was shortened/removed]" or "SKIP: [reason overlap is intentional]"`,
        { label: `dedup-para-${dup.fix_sec}`, phase: 'Fix Paragraphs' }
      )
    }
  )
}

// ── Phase 5: Fix concept-level overlaps ──────────────────────────────────────
phase('Concept Overlaps')

const conceptOverlaps = report.concept_overlaps || []
log(`Reviewing ${conceptOverlaps.length} concept-scope overlap pairs...`)

if (conceptOverlaps.length > 0) {
  await pipeline(
    conceptOverlaps,
    async (dup) => {
      return agent(
        `You are the Structural Refactoring Architect (#19) reviewing concept-scope overlap.

Two sections have very similar big-picture scope (${Math.round(dup.similarity * 100)}% overlap in their big-picture callouts).

Section A (${dup.sec_a}): "${dup.text_a.substring(0, 300)}"
Section B (${dup.sec_b}): "${dup.text_b.substring(0, 300)}"

ASSESSMENT TASK:
1. Read BOTH sections fully
2. Decide: are these sections covering genuinely different aspects, or is there real scope duplication?
3. If DIFFERENT aspects (different depth, different application, different angle) → return "DISTINCT: [explanation of what each covers uniquely]"
4. If REAL OVERLAP → rewrite the big-picture callout of section ${dup.sec_b} (the later one) to:
   - Acknowledge that section ${dup.sec_a} covers [concept]
   - Clarify what section ${dup.sec_b} adds or approaches differently
   - Reference section ${dup.sec_a} explicitly

Only edit file ${dup.path_b} if there is real overlap.
NEVER use em dashes or double dashes.

Return: "DISTINCT: [reason]" or "FIXED: [what was differentiated]"`,
        { label: `overlap-${dup.sec_a}-${dup.sec_b}`, phase: 'Concept Overlaps' }
      )
    }
  )
}

log('Wave 12 deduplication complete!')
return {
  wave: '12-dedup',
  callout_pairs_fixed: calloutDups.length,
  para_pairs_fixed: paraDups.length,
  concept_overlaps_reviewed: conceptOverlaps.length,
}
