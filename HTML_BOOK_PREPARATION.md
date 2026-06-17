# EmbodiedAI HTML Book Preparation Brief

## Scope

Prepare **Building Embodied AI: From Perception to Autonomous Action** for HTML production in the exact style family of **Building Vision AI** and as part of the **Hands-On AI Science** series.

This pass does not produce the book. It prepares the assets, configuration, structure, and constraints for a later production pass.

## Reference Sources

Primary local source:

`E:\Projects\Books\VisionAI`

Public reference:

`https://visionbook.apartsin.com/`

Live series reference checked:

`https://visionbook.apartsin.com/front-matter/about-the-series.html`

Book plan source:

`E:\Projects\Books\EmbodiedAI\building_embodied_ai_book_plan.md`

## What Was Learned From VisionAI

The Vision book uses a stable web-book system that should be reused directly:

1. A single shared stylesheet at `styles/book.css`.
2. A Prism syntax highlighting layer for code.
3. A KaTeX layer for math.
4. A shared runtime script at `scripts/book.js`.
5. Pagefind hooks for local search.
6. A consistent chapter header with top navigation, part label, chapter label, and search.
7. A strong chapter opening pattern: epigraph, big-picture callout, key-insight callout, overview, prerequisites, roadmap.
8. A distinctive callout system with icon-backed classes.
9. Hands-on labs that close chapters with runnable projects.
10. Bibliography cards grouped by category, with annotations.
11. Previous, contents, and next navigation.
12. Footer language with title, copyright, contents link, and last updated line.

## Series Adaptation

VisionAI defines **Hands-On AI Science** as a series that pairs serious depth with serious building. EmbodiedAI should keep that exact promise but specialize it for physical and simulated agents.

EmbodiedAI should present itself as:

1. A self-contained graduate-depth book.
2. A hands-on builder text, not only a research survey.
3. A field bridge connecting robotics, control, simulation, reinforcement learning, imitation learning, VLA models, world models, humanoids, safety, and deployment.
4. The fifth Hands-On AI Science volume, following Language AI, Vision AI, Temporal AI, and Scalable AI.
5. A course-ready book for advanced undergraduate, graduate, self-study, and seminar use.

## Prepared Files

`BOOK_CONFIG.md`

Defines the book identity, series positioning, style source, required page skeleton, callout catalog, teaching rhythm, chapter map, appendices, and directory naming plan.

`CROSS_REFERENCE_MAP.md`

Defines recurring concepts that must be linked across chapters, including the perception-action loop, partial observability, geometry, control, simulation, reinforcement learning, imitation learning, action representation, VLA models, world models, humanoids, evaluation, safety, and deployment.

`CONFORMANCE_CHECKLIST.md`

Defines the production checklist for source assets, series identity, page structure, chapter openings, section patterns, callouts, code, math, bibliography, visuals, navigation, style, and production gates.

## Prepared Assets

The following were copied from VisionAI into EmbodiedAI:

1. `styles/book.css`
2. `styles/pygments.css`
3. `styles/icons/`
4. `scripts/book.js`
5. `templates/`
6. `vendor/katex/`
7. `vendor/prism/`

These are infrastructure assets only. No book chapters were generated.

## Production Rules For The Next Pass

1. Do not create a new visual identity. Reuse the VisionAI system.
2. Use `BOOK_CONFIG.md` as the structure source of truth.
3. Use `CROSS_REFERENCE_MAP.md` before writing cross-links.
4. Use `CONFORMANCE_CHECKLIST.md` after every generated chapter or section.
5. Keep the Hands-On AI Science promise visible in front matter and teaching design.
6. Include from-scratch mechanisms and then library shortcuts.
7. Keep EmbodiedAI current to the 2026 plan, including VLA models, LeRobot, GPU simulators, generative world models, humanoids, modern evaluation, and safety.
8. Run citation verification with `bibtest` before final publication text.
9. Generate Pagefind only after HTML content exists.
10. Build EPUB and KPF only after the HTML source passes the conformance checklist.

## Ready State

The project is now ready for a later HTML production pass. The next pass should start by generating front matter and the main index from the prepared configuration, then build one pilot chapter before scaling to the whole book.
