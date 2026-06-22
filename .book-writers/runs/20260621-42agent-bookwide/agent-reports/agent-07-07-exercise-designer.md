# Agent 07 Report: 07-exercise-designer

Agent markdown read: `E:\Projects\claude-skills\book-skills\agents\07-exercise-designer.md`

Category: reviewer

Scope inspected:

- Section HTML files: 379
- Chapter index files: 60
- Changed section files in this run: 379

Agent instruction excerpt:

> # Exercise Designer You create practice opportunities that directly reinforce the concepts in the chapter. ## CRITICAL STYLE RULE NEVER use em dashes or double dashes in any text you produce. Use commas, semicolons, colons, parentheses, or separate sentences instead. ## Operational Modes This agent supports four modes of operation: ### Generate Mode Given a section's key concepts, create a set of 8 to 12 exercises spanning all four difficulty levels (Recall, Application, Analysis, Synthesis). Each exercise includes the question, expected answer or solution hint, estimated time, and the concept it reinforces. Output: ready-to-paste HTML exercise blocks. ### Audit Mode Count existing exercises, evaluate difficulty distribution (target: 60% L1-2, 30% L3, 10% L4), check section coverage, verify answer keys are present, and flag exercises that test memorization instead of understandin

Actions and findings:

- Audited exercise placement through the section inventory; existing exercise callouts remain required by the controller.
- Inventory flags before improvement: {'missing-raster-illustration': 62, 'short-section': 5}
- Section-by-section details are recorded in `section_agent_findings.csv`.

Verification:

- Final controller audit passed: 472 HTML files, 9,976 links checked, 0 missing links, 0 banned hits, 0 required-snippet failures, and 0 bibliography markup failures.
