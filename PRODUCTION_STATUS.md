# Building Embodied AI Production Status

Current date: 2026-06-17

## Source Of Truth

- Plan: `building_embodied_ai_book_plan.md`
- Archived old plan: `archive/building_embodied_ai_book_plan_v1_ARCHIVED.md`
- Book configuration: `BOOK_CONFIG.md`
- Cross-reference map: `CROSS_REFERENCE_MAP.md`
- Conformance checklist: `CONFORMANCE_CHECKLIST.md`
- Style source: copied Vision book assets in `styles/`, `scripts/`, `vendor/`, `templates/`, and `pagefind/`
- Skill source: `E:\Projects\claude-skills\book-skills`

## Current State

- Complete HTML book exists.
- Cover, table of contents, front matter, parts, chapters, section pages, and appendices exist.
- All twelve parts have now received returned 42-agent worker passes under the campaign documented in `ALL_AGENTS_CAMPAIGN.md`.
- Each part worker applied the `book-skills` agent checklist across its owned chapter indexes and section files.
- The Illustrator phase has now run from the main context with Gemini batch generation. It produced and embedded 295 module-local raster illustrations, covering all 60 chapters. See `ILLUSTRATOR_REPORT.md`.
- Current static QA is clean after all-agent integration.

## Audit Gates

Structural audit:

```powershell
C:\Python314\python.exe scripts\audit_html_book.py
```

Last result:

- `html_files=455`
- `chapter_files=60`
- `section_files=363`
- `links_checked=9307`
- `missing_links=0`
- `banned_hits=0`
- `required_failures=0`
- `bibliography_markup_failures=0`

Depth audit:

```powershell
C:\Python314\python.exe scripts\audit_book_depth.py
```

Last result:

- `section_depth_gaps=0`
- `chapter_depth_gaps=0`
- `scaffold_phrase_hits=0`

Depth audit now passes.

## Agent Wave

- All production agents from the all-agent campaign have completed and been closed.
- Useful worker edits were preserved and integrated.
- No active subagents remain.

## Protection Rules

- Do not run `scripts/generate_html_book.py` during production waves. It overwrites chapter files.
- Keep Chapter 11 and Chapter 34 stable unless a targeted QA fix is required.
- Run `scripts/audit_html_book.py` after every worker integration.
- Run `scripts/audit_book_depth.py` to track remaining scaffold-level pages.
- No em dashes, no double dashes, and no banned candor phrases in published HTML.

## Browser Verification Note

The in-app browser was open at `file:///E:/Projects/Books/EmbodiedAI/index.html`, but browser automation blocked programmatic navigation and read-only DOM inspection for `file://` URLs under its security policy. Verification therefore used local static audits, asset/link parsing, depth checks, and published-text scans.
