export const meta = {
  name: 'waves-9-to-11',
  description: 'Waves 9-11: opening hooks, dense prose breaks, aha-moments and memorability',
  phases: [
    { title: 'Wave 9 - Hooks', detail: 'All 379 sections: score opening hook, rewrite if weak' },
    { title: 'Wave 10 - Prose', detail: '30 sections: break dense paragraphs, improve flow' },
    { title: 'Wave 11 - Aha', detail: '366 sections: add aha-moments and memorable phrases' },
  ],
}

// ── Wave 9: Opening Hook (#22) ────────────────────────────────────────────────
phase('Wave 9 - Hooks')

const allSecRaw = await agent(
  `Read the file scripts/section_index.json and return its full content. Return ONLY the raw JSON array.`,
  { label: 'load-all-sections' }
)
const allSections = typeof allSecRaw === 'string' ? JSON.parse(allSecRaw) : allSecRaw
log(`Wave 9: assessing opening hooks for ${allSections.length} sections`)

await pipeline(
  allSections,
  async (t) => {
    const sec = t.sec
    const path = t.path.replace(/\\/g, '/')
    return agent(
      `You are the Opening and Hook Designer (#22) for an embodied AI textbook.

TASK: Assess the opening hook of section ${sec} and rewrite it if weak.

File: ${path}
Title: ${t.title}

SCORING RUBRIC — score the big-picture callout 1-10:
  9-10: Vivid concrete scenario, strong "why this matters", creates genuine curiosity
   7-8: Clear motivation, specific, one concrete example
   5-6: Accurate but dry, tells what rather than why, no urgency
   3-4: Generic AI-textbook boilerplate, starts "This section covers...", no hook
   1-2: Missing or one vague sentence

REWRITE CRITERIA — only rewrite if score <= 6:
A strong big-picture hook:
- Opens with a concrete scene, number, or striking claim (not "In this section")
- Names why this topic matters RIGHT NOW (a real system, a real problem)
- Creates genuine curiosity or urgency in the reader
- Is 80-150 words — not a summary, a motivator
- NEVER starts with "This section" or "In this section"

HTML FORMAT for the big-picture callout:
<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>[Strong motivating opening: concrete scene or claim, then why it matters, then what the reader will learn to do]</p>
</div>

INSTRUCTIONS:
1. Read file "${path}"
2. Find the <div class="callout big-picture"> block
3. Score it 1-10 using the rubric
4. If score >= 7: return "PASS [score]/10: [reason]" — do NOT edit
5. If score <= 6: rewrite the callout body with a strong hook and edit the file
6. NEVER use em dashes or double dashes

Return: "PASS X/10: reason" or "FIXED X->9/10: what changed"`,
      { label: `hook-${sec}`, phase: 'Wave 9 - Hooks' }
    )
  }
)

log('Wave 9 complete.')

// ── Wave 10: Dense Prose (#31 + #32) ─────────────────────────────────────────
phase('Wave 10 - Prose')

const w10raw = await agent(
  `Read the file scripts/wave10_targets.json and return its full content. Return ONLY the raw JSON array.`,
  { label: 'load-w10-targets' }
)
const w10targets = typeof w10raw === 'string' ? JSON.parse(w10raw) : w10raw
log(`Wave 10: fixing dense paragraphs in ${w10targets.length} sections`)

await pipeline(
  w10targets,
  async (t) => {
    const sec = t.sec
    const path = t.path.replace(/\\/g, '/')
    return agent(
      `You are the Readability and Pacing Editor (#32) for an embodied AI textbook.

TASK: Find and break the densest paragraph(s) in section ${sec}.

File: ${path}
Title: ${t.title}

This section has at least one paragraph over 180 words — that is too dense for a technical textbook.

FIX STRATEGY for a long paragraph:
  Option A: Split into two paragraphs with a brief bridging sentence
  Option B: Extract 2-4 items into a <ul> or <ol> list
  Option C: Pull a key sub-concept into a key-insight or tip callout, shorten the paragraph
  Option D: Add a mini-heading (h3) to create breathing room

Choose the option that best fits the structure of the dense section. Apply the fix.

PACING RULES:
- No paragraph should exceed 120 words
- No more than 3 consecutive paragraphs without a visual break (callout, heading, code, or list)
- Prefer concrete over abstract: replace "the system" with the actual system name

INSTRUCTIONS:
1. Read file "${path}"
2. Find the paragraph(s) over 120 words
3. Apply the best fix (split, list, callout, or heading)
4. Also check: are there 4+ consecutive paragraphs without any visual break? If so, add a break
5. Edit the file directly
6. NEVER use em dashes or double dashes

Return: one-line summary of what was changed.`,
      { label: `prose-${sec}`, phase: 'Wave 10 - Prose' }
    )
  }
)

log('Wave 10 complete.')

// ── Wave 11: Aha-Moment + Memorability (#24 + #29) ────────────────────────────
phase('Wave 11 - Aha')

const w11raw = await agent(
  `Read the file scripts/wave11_targets.json and return its full content. Return ONLY the raw JSON array.`,
  { label: 'load-w11-targets' }
)
const w11targets = typeof w11raw === 'string' ? JSON.parse(w11raw) : w11raw
log(`Wave 11: adding aha-moments and memorable phrases to ${w11targets.length} sections`)

await pipeline(
  w11targets,
  async (t) => {
    const sec = t.sec
    const path = t.path.replace(/\\/g, '/')
    return agent(
      `You are the Aha-Moment Engineer (#24) and Memorability Designer (#29) for an embodied AI textbook.

TASK: Add ONE aha-moment and ONE memorable phrase to section ${sec}.

File: ${path}
Title: ${t.title}

PART 1 — AHA MOMENT:
Find the single most important concept where ONE striking example, contrast, or experiment could create instant understanding. Then check if the section already has a strong aha moment for that concept. If yes: SKIP Part 1. If no: add it.

An aha moment is:
- A concrete before/after comparison: "Without X, Y takes 1000 steps. With X, 10 steps."
- A surprising number: "A 6-DOF arm has 6 dimensions of freedom — but grasping a cup has 6 constraints, leaving exactly 0 degrees of freedom at contact."
- A physical analogy: "The Bellman backup is like GPS rerouting: it only needs to know the next junction, not the full route."
- A scale illustration: "Training on 1 GPU takes 3 months. Isaac Lab on 4000 parallel envs: 3 hours."

HTML FORMAT — inline (woven into a paragraph, NOT a callout box):
Rewrite the relevant sentence to include the aha moment naturally.

PART 2 — MEMORABLE PHRASE:
Identify the key concept of the section. Check if there is already a bolded memorable phrase in the prose (like <strong>key phrase</strong> mid-sentence). If yes: SKIP Part 2. If no: add a bold key phrase.

A memorable phrase is 3-7 words, bolded inline, that encapsulates the section's main insight:
- "the sim-to-real gap"
- "credit assignment over long horizons"
- "the curse of dimensionality"
- "privileged information in simulation"

HTML FORMAT — inline in an existing paragraph:
...this is called <strong>key concept phrase</strong>, and it...

INSTRUCTIONS:
1. Read file "${path}"
2. Apply aha-moment if the section lacks a strong "click" moment
3. Add or strengthen a bold key phrase
4. Make both changes inline — do NOT add new callout boxes for this
5. Edit the file directly (may be zero edits if both already present)
6. NEVER use em dashes or double dashes

Return: "AHA: [what you added or 'already present']; PHRASE: [what you bolded or 'already present']"`,
      { label: `aha-${sec}`, phase: 'Wave 11 - Aha' }
    )
  }
)

log('Waves 9-11 all complete!')
return { waves_complete: ['9-hooks', '10-prose', '11-aha-memorability'] }
