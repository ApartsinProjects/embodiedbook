# Depth Remediation Status

Date: 2026-06-18

## Completed

- Added technical-core expansions to the 78 sections previously marked `DEPTH-GAP`.
- Added technical-core expansions to the remaining Part VI perception, SLAM, and navigation sections so the perception and planning chapters now include formulas, algorithm callouts, block diagrams, evidence code, expected-output interpretation, and method-specific failure tests.
- Added local reference cards to sections that lacked section-level reference support.
- Added expected-output interpretation to code-heavy sections that previously printed traces without explaining what the output should mean.
- Removed repeated scaffold phrases that made sections read as templated rather than topic-native.
- Updated `scripts/audit_scientific_depth.py` so it recognizes dynamics-specific terms such as manipulator equation, Euler-Lagrange, Newton-Euler, mass matrix, Coriolis, contact Jacobian, friction cone, complementarity, semi-implicit Euler, Runge-Kutta, MJX, Isaac Gym, Brax, and contact solver.

## Current Gate Results

```text
audited=363
verdicts=COURSE-READY:363
review_or_gap=0
```

Structural audits also pass:

```text
html_files=455
chapter_files=60
section_files=363
links_checked=9602
missing_links=0
banned_hits=0
required_failures=0
bibliography_markup_failures=0
section_depth_gaps=0
chapter_depth_gaps=0
scaffold_phrase_hits=0
```

## Browser Spot Checks

Rendered with local Chrome through Playwright:

- `section-6.3.html`, contact, friction, and contact-rich simulation.
- `section-30.2.html`, BFS, Dijkstra, and A*.
- `section-59.4.html`, LeRobot VLA fine-tuning capstone.

All three rendered with:

- no page errors,
- no horizontal overflow at 1280 px,
- visible technical-core blocks,
- technical figures present,
- code captions present,
- bibliography cards present.
