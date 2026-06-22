# Agent 11 Report: 11-fact-integrity

Agent markdown read: `E:\Projects\claude-skills\book-skills\agents\11-fact-integrity.md`

Category: reviewer

Scope inspected:

- Section HTML files: 379
- Chapter index files: 60
- Changed section files in this run: 379

Agent instruction excerpt:

> # Fact Integrity Reviewer You are a rigorous skeptic focused on truth and technical reliability. ## CRITICAL STYLE RULE NEVER use em dashes or double dashes in any text you produce. Use commas, semicolons, colons, parentheses, or separate sentences instead. ## Operational Modes This agent supports four modes of operation: ### Generate Mode Given a topic, produce a fact sheet with verified claims, proper citations, benchmark numbers with dates, and attribution for key results. Output: a reference document that content authors can draw from when writing new sections. ### Audit Mode Check every factual claim, number, date, benchmark, and attribution in the chapter. Classify each as verified, plausible but unverified, or incorrect. Flag outdated benchmarks, missing citations, and hedging language that should replace unsupported claims. Output: Fact Integrity Report with categorized i

Actions and findings:

- Constrained edits to factual, non-citation claims about logs, interfaces, evidence artifacts, and replayability.
- Inventory flags before improvement: {'missing-raster-illustration': 62, 'short-section': 5}
- Section-by-section details are recorded in `section_agent_findings.csv`.

Verification:

- Final controller audit passed: 472 HTML files, 9,976 links checked, 0 missing links, 0 banned hits, 0 required-snippet failures, and 0 bibliography markup failures.
