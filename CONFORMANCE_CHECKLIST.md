# Embodied AI HTML Book Conformance Checklist

This checklist prepares the EmbodiedAI book to use the same style, callout system, and format conventions as `E:\Projects\Books\VisionAI`.

Current mode: preparation only. Do not mark content chapters complete until HTML has been generated and audited.

## A. Source And Assets

- [x] `styles/book.css` copied from VisionAI.
- [x] `styles/pygments.css` copied from VisionAI.
- [x] `styles/icons/` copied from VisionAI.
- [x] `scripts/book.js` copied from VisionAI.
- [x] `templates/` copied from VisionAI.
- [x] `vendor/katex/` copied from VisionAI.
- [x] `vendor/prism/` copied from VisionAI.
- [ ] Pagefind assets generated after the HTML book exists.
- [ ] Analytics policy confirmed before adding the VisionAI analytics block.

## B. Series Identity

- [ ] Front matter includes **About the Hands-On AI Science Series**.
- [ ] Series description matches VisionAI in promise and tone, adapted to EmbodiedAI.
- [ ] Series list includes Language AI, Vision AI, Temporal AI, Scalable AI, and Embodied AI.
- [ ] EmbodiedAI is described as the fifth volume and the bridge into physical AI.
- [ ] Front matter avoids course-only framing when referring to the book itself.

## C. Page Structure

Every generated content page must include:

- [ ] `<!DOCTYPE html>`
- [ ] `<html lang="en">`
- [ ] `<meta charset="utf-8"/>`
- [ ] Responsive viewport meta tag.
- [ ] Meaningful meta description.
- [ ] `<title>` with chapter or section title and book name.
- [ ] `styles/book.css`.
- [ ] `styles/pygments.css` when code appears.
- [ ] KaTeX CSS and scripts when math appears.
- [ ] Prism CSS and scripts when code appears.
- [ ] `scripts/book.js`.
- [ ] Pagefind hooks after search is generated.
- [ ] `<a class="skip-link" href="#main-content">Skip to main content</a>`.
- [ ] `<header class="chapter-header">`.
- [ ] `<nav class="header-nav">`.
- [ ] `.book-title-link` pointing to the correct relative `index.html`.
- [ ] `.toc-link` pointing to the correct relative `toc.html`.
- [ ] `.header-search` with `<div id="search"></div>`.
- [ ] `.part-label`.
- [ ] `.chapter-label`.
- [ ] `<main class="content" id="main-content">`.
- [ ] `<nav class="chapter-nav">`.
- [ ] `<footer>`.

## D. Chapter Opening Pattern

Every chapter index page must include:

- [ ] Epigraph immediately after the header.
- [ ] One `.callout.big-picture`.
- [ ] One `.callout.key-insight` with a memorable chapter frame.
- [ ] `Chapter Overview`.
- [ ] `Prerequisites`.
- [ ] `Chapter Roadmap` with `.sections-list`.
- [ ] One `whats-next` block.
- [ ] One full hands-on lab.
- [ ] Bibliography and further reading.

## E. Section Pattern

Every section page must include:

- [ ] A focused opening paragraph that situates the section in the chapter.
- [ ] At least one key visual, table, callout, or code block before the fourth paragraph.
- [ ] Theory at the right depth for the chapter.
- [ ] A concrete worked example.
- [ ] A runnable code fragment when the section is practical.
- [ ] Code caption below every code block.
- [ ] A `library-shortcut` callout after any substantial from-scratch implementation.
- [ ] One `self-check` or exercise element.
- [ ] One `key-takeaway` near the end.
- [ ] Cross-links to prerequisites and future uses.

## F. Callouts

- [ ] All callouts use VisionAI classes from `styles/book.css`.
- [ ] Every callout has `.callout-title` unless using an established VisionAI exception.
- [ ] Callouts are referenced in nearby prose.
- [ ] No page has a long run of unbroken paragraphs without visual relief.
- [ ] `library-shortcut` callouts name the library, show the short code route, and explain what the library handles.
- [ ] `research-frontier` callouts distinguish peer-reviewed findings from vendor-reported claims.
- [ ] `warning` callouts are used for safety, deployment, simulation traps, or misleading evaluation.
- [ ] `postmortem` callouts are used for realistic production failures.

## G. Code And Math

- [ ] Code is runnable in the stated environment.
- [ ] Code blocks use Prism language classes.
- [ ] Every code block has a unique caption below it.
- [ ] Expected output is included for nontrivial code.
- [ ] Library versions or recency caveats are stated where needed.
- [ ] Math is rendered with KaTeX.
- [ ] Symbols are defined before use.
- [ ] Derivations include intuition, not only equations.

## H. Bibliography

- [ ] Bibliography uses VisionAI `bib-entry-card` style.
- [ ] Entries are grouped by category.
- [ ] Papers include venue, year, URL, and short annotation.
- [ ] Tools and libraries link to official docs or GitHub.
- [ ] Datasets and benchmarks include access or documentation links.
- [ ] Citations are verified with `bibtest` before publication.
- [ ] Vendor-only claims are labeled as such.

## I. Visuals

- [ ] Every figure has alt text.
- [ ] Every figure has a caption.
- [ ] Every figure is referenced in prose.
- [ ] Technical diagrams are fact checked.
- [ ] Generated illustrations are pedagogical, not decorative filler.
- [ ] SVGs and images pass Kindle compatibility checks before EPUB or KPF production.

## J. Navigation And Linking

- [ ] Main index links to all parts.
- [ ] TOC links to all front matter, parts, chapters, appendices, and capstone material.
- [ ] Part index pages link to all chapters in that part.
- [ ] Chapter pages link to section pages.
- [ ] Section pages link to previous, chapter home, and next.
- [ ] Cross-references use correct relative paths.
- [ ] No broken internal links.
- [ ] No stale chapter numbers after renumbering.

## K. Style Rules

- [ ] No em dashes.
- [ ] No double hyphens.
- [ ] No forbidden candor phrase group from `AGENTS.md`.
- [ ] Text uses plain, direct explanations.
- [ ] The book says "reader", "chapter", "section", and "part" when discussing the book itself.
- [ ] Course language is reserved for the teaching appendix and instructor materials.
- [ ] Claims are supported by explanation, citation, or explicit frontier caveat.

## L. Production Gates

- [ ] `BOOK_CONFIG.md` is current.
- [ ] `CROSS_REFERENCE_MAP.md` is current.
- [ ] This checklist is current.
- [ ] HTML generation has explicit approval.
- [ ] Whole-book or whole-part generation states the Batch API decision before launch.
- [ ] Post-generation quality pass runs before any chapter is called complete.
- [ ] Pagefind is generated after content exists.
- [ ] EPUB build uses the relevant publishing skill after HTML source passes checks.
- [ ] KPF build uses the relevant publishing skill after EPUB validation.
