# 42-Agent Bookwide Wave Plan

Run: `20260621-42agent-bookwide`

## Scope

- Section HTML files inspected: 379
- Chapter index files inspected: 60
- Agent markdown specs loaded: 42
- Section files changed in Wave 2: 379

## Wave 1: Inventory and Agent Reading

All numbered book-writer agent markdown files from `E:/Projects/claude-skills/book-skills/agents` were loaded into the run. Every section page and module index page was inventoried for callouts, code blocks, figures, links, word count, and conformance flags.

## Wave 2: Section-Level Improvements

The reviewer and editor findings converged on two high-value gaps: navigation of concepts and memorable retention hooks. The pass added 379 reader-pathway callouts and 285 memory-hook fun-note callouts. Existing fun notes were preserved.

## Wave 3: Controller and Publication QA

After the edits, run `scripts/audit_html_book.py`, scan for banned prose forms, update the ledger, and keep the run report with one report per agent.
