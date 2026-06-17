# Scientific and Technological Depth Audit, Round 2
This audit reads every section HTML file and applies the book-writers depth rubrics: deep explanation, code pedagogy, research grounding, self-containment, and publication QA. The automated pass is a triage tool, not a substitute for author judgment, so it deliberately flags polished but generic sections.
## Scope
- Section files audited: 363
- Machine-readable inventory: `audit/scientific_depth_round_2.csv` and `audit/scientific_depth_round_2.json`
- Rubric: mechanism depth, formal or algorithmic specificity, concrete tools and libraries, runnable evidence, self-contained definitions, local references, and scaffold reuse.
## Verdict Counts
- COURSE-READY: 39
- REVIEW: 246
- DEPTH-GAP: 78
## Most Common Issues
- code lacks explicit expected-output discussion: 258
- repeated scaffold language: 248
- missing local reference card: 143
- topic-specific names are sparse: 6
- weak mechanism and failure analysis: 1
## Chapter-Level Distribution
| Chapter | Course-ready | Review | Depth-gap |
|---:|---:|---:|---:|
| 1 | 1 | 7 | 0 |
| 2 | 3 | 5 | 0 |
| 3 | 0 | 8 | 0 |
| 4 | 0 | 7 | 0 |
| 5 | 0 | 0 | 8 |
| 6 | 0 | 0 | 6 |
| 7 | 0 | 0 | 7 |
| 8 | 0 | 0 | 8 |
| 9 | 0 | 5 | 0 |
| 10 | 0 | 7 | 0 |
| 11 | 1 | 7 | 0 |
| 12 | 0 | 6 | 0 |
| 13 | 0 | 6 | 0 |
| 14 | 0 | 5 | 0 |
| 15 | 0 | 6 | 0 |
| 16 | 0 | 5 | 0 |
| 17 | 0 | 6 | 0 |
| 18 | 0 | 6 | 0 |
| 19 | 0 | 4 | 0 |
| 20 | 0 | 5 | 0 |
| 21 | 0 | 5 | 0 |
| 22 | 0 | 7 | 0 |
| 23 | 0 | 6 | 0 |
| 24 | 0 | 5 | 0 |
| 25 | 0 | 5 | 0 |
| 26 | 0 | 5 | 0 |
| 27 | 0 | 6 | 1 |
| 28 | 0 | 7 | 0 |
| 29 | 0 | 7 | 0 |
| 30 | 0 | 5 | 1 |
| 31 | 0 | 6 | 0 |
| 32 | 0 | 6 | 0 |
| 33 | 0 | 8 | 0 |
| 34 | 2 | 6 | 0 |
| 35 | 0 | 7 | 0 |
| 36 | 5 | 0 | 0 |
| 37 | 5 | 0 | 0 |
| 38 | 6 | 0 | 0 |
| 39 | 7 | 0 | 0 |
| 40 | 4 | 0 | 0 |
| 41 | 5 | 0 | 0 |
| 42 | 0 | 6 | 0 |
| 43 | 0 | 5 | 0 |
| 44 | 0 | 5 | 0 |
| 45 | 0 | 5 | 0 |
| 46 | 0 | 7 | 0 |
| 47 | 0 | 5 | 0 |
| 48 | 0 | 6 | 0 |
| 49 | 0 | 0 | 5 |
| 50 | 0 | 0 | 6 |
| 51 | 0 | 0 | 5 |
| 52 | 0 | 6 | 0 |
| 53 | 0 | 4 | 0 |
| 54 | 0 | 6 | 0 |
| 55 | 0 | 5 | 0 |
| 56 | 0 | 0 | 4 |
| 57 | 0 | 0 | 4 |
| 58 | 0 | 0 | 6 |
| 59 | 0 | 0 | 11 |
| 60 | 0 | 0 | 6 |
## Weakest Sections To Fix First
| Score | Verdict | Section | Issues | Recommendation |
|---:|---|---|---|---|
| 21 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.5.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 21 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.1.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 21 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.3.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 21 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.4.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 22 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.2.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 22 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.5.html` | repeated scaffold language; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 22 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.2.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 22 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.5.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 23 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.3.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 23 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.3.html` | repeated scaffold language; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 23 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.4.html` | repeated scaffold language; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 23 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.6.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 23 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/section-56.2.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 23 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-56-embodied-agents-with-memory/section-56.4.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.1.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.5.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.1.html` | repeated scaffold language; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-51-open-world-and-lifelong-embodiment/section-51.2.html` | repeated scaffold language; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.6.html` | repeated scaffold language; topic-specific names are sparse; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-57-continual-and-lifelong-learning/section-57.2.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.10.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.11.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 24 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-60-teaching-with-this-book/section-60.1.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-49-multi-agent-embodied-ai/section-49.4.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.2.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-10-multi-agent-and-human-centered-embodiment/module-50-human-robot-interaction/section-50.3.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.1.html` | repeated scaffold language; topic-specific names are sparse; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.2.html` | repeated scaffold language; topic-specific names are sparse; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.3.html` | repeated scaffold language; topic-specific names are sparse; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.4.html` | repeated scaffold language; topic-specific names are sparse; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-2-mathematical-robotics-and-control-foundations/module-06-dynamics-and-simulation-math/section-6.5.html` | repeated scaffold language; topic-specific names are sparse; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-57-continual-and-lifelong-learning/section-57.3.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.4.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.1.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 25 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.2.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 26 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-58-frontier-and-open-problems/section-58.1.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 26 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.5.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 26 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.6.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 26 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.8.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
| 26 | DEPTH-GAP | `part-12-frontiers-capstones-and-course-design/module-59-capstone-projects/section-59.9.html` | repeated scaffold language; code lacks explicit expected-output discussion; missing local reference card | Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence. |
## Agent Rubric Notes
- Deep explanation gate: a section must answer what, why, how, and when it fails, not only define the topic.
- Code pedagogy gate: runnable fragments need a reason to exist, named inputs and outputs, and expected-output interpretation when output is nontrivial.
- Research scientist gate: a graduate section should name algorithms, assumptions, measurement artifacts, and credible tools rather than broad families only.
- Self-containment gate: sections should define variables, frames, metrics, and failure labels locally enough for a course reader to proceed without leaving the page.
- Publication QA gate: repeated scaffold language is treated as a defect even when links, images, and callouts are structurally valid.
## Remediation Policy
Fix depth gaps by replacing generic action-loop prose with topic-specific material: derivation or algorithm sketch, assumptions, implementation contract, tool-specific recipe, failure analysis, and one evidence artifact. Do not add decorative prose to pass the audit.
