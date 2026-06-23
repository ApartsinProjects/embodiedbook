export const meta = {
  name: "pack-p7-publish",
  description: "Pack P7: Publish — structural review, epigraphs, bibliography, meta-audit, controller, pub-QA, dedup (#19 #32 #35 #36 #37 #38 #42)",
  phases: [{ title: "Publish" }],
}

const BOOK_ROOT = "E:/Projects/Books/EmbodiedAI"

phase("Publish")
await agent(
  `You are running the final publication pack for the book at ${BOOK_ROOT}.
This pack runs at BOOK LEVEL (not per-section). Perform all seven passes in order.
Do not use em dashes or double hyphens anywhere.

=== PASS 1: Deduplication (Agent #42) ===
Run: python scripts/detect_duplicates.py --book-root ${BOOK_ROOT}
Read scripts/dedup_report.json. For each pair with similarity >= 0.55, apply one of:
MERGE INTO (absorb unique sentences into canonical, delete duplicate),
CONSOLIDATE (merge both into canonical, replace duplicate with pointer callout),
DIFFERENTIATE (rewrite both to distinct angles), SKIP (intentional depth progression).
Prefer MERGE INTO for near-identical callouts. Prefer DIFFERENTIATE for same concept
from different angles.

=== PASS 2: Structural Review (Agent #19) ===
Sample the first section of every chapter. Verify: consistent section naming pattern,
no chapter with fewer than 3 sections, all What's Next sections link to a real next
chapter. Log and fix structural anomalies.

=== PASS 3: Epigraph (Agent #32) ===
For every chapter index page (module-*/index.html): verify it has an epigraph block
(<div class="epigraph">). If missing or using a placeholder, write a thematic quote
attributed to "A [Adjective] Embodied AI Agent" in the book's voice. Fix in-place.

=== PASS 4: Bibliography (Agent #35) ===
For every section that has a bibliography section: verify each entry has author(s),
year, title, and venue. Truncated entries (ending in "..." or missing fields) must be
completed. Remove duplicate entries. Ensure entries are sorted by year descending.

=== PASS 5: Controller Sweep (Agent #37) ===
Sample every 10th section. For each: verify conformance checklist items A-N, cross-
reference links resolve, all callout classes are valid, no em dashes, no syllabus
language. Log failures and fix them inline.

=== PASS 6: Publication QA (Agent #38) ===
For every section file: verify <title> matches section heading, all <img src> paths
resolve, no broken </html> tags, CSS link points to ../../styles/book.css, nav footer
links to correct prev/next. Log and fix failures.

=== PASS 7: Meta-Agent Audit (Agent #36) ===
Review this run's changes. Identify: (1) any agent that consistently underperformed
(patterns of missed tasks in the diff), (2) any pack prompt that should be sharpened
for the next book run. Write a brief audit to scripts/.pack_audit.md including:
- Pack with most skipped tasks
- Pack with most edits per section (potential over-engineering)
- Suggested prompt improvements for top 2 underperformers
`,
  { label: "pack-p7-publish" }
)

return { wave: "pack-p7-publish" }
