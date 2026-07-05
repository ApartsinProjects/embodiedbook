# KDP Submission Guide: Building Embodied AI

Single source of truth for the Kindle Direct Publishing submission. Field values
mirror `KDP/metadata/metadata.yaml`, `KDP/metadata/description.html`, and
`html2epub.toml`.

## Deliverables

| Item | Path | Spec |
|---|---|---|
| Manuscript (EPUB 3, reflowable) | `KDP/output/building-embodied-ai-diagrams.epub` | EPUBCheck 0/0/0/0; 42 MB; diagrams rasterized (KFX-safe); KDP accepts EPUB directly |
| Cover | `KDP/cover/book-cover-kdp.jpg` | 1600 x 2560, baseline (non-progressive) sRGB JPEG |

Upload the **`-diagrams.epub`** (not `building-embodied-ai.epub`). Both pass
EPUBCheck, but the `-diagrams` copy has every inline SVG rasterized to an image,
which renders reliably after KDP's server-side KFX conversion; the plain EPUB keeps
crisp inline SVG that some Kindle renderers clip. A local `.kpf` is optional (build
via the `epub2kpf` skill) and only needed for offline Kindle Previewer validation;
it is NOT required for upload, and any older `.kpf` in `KDP/output/` predates the
current fixes, so do not upload it.

## Build commands

```bash
# reflowable EPUB with math rendered as MathML (NOT KaTeX-HTML): KaTeX draws
# \sqrt / stretchy delimiters as inline <svg width="400em">, which KDP's KFX
# converter rejects ("SVG specified in the content is not renderable"). MathML
# radicals are native (no SVG). html2epub auto-repairs KaTeX's over-arity MathML.
HTML2EPUB_KATEX_OUTPUT=mathml python -m html2epub build .   # -> KDP/output/building-embodied-ai.epub

# rasterize diagrams for the KFX-safe Kindle copy (epub2kpf skill)
EPUB2KPF_DIAGRAM_SCALE=1.5 EPUB2KPF_DIAGRAM_JPEG_QUALITY=82 EPUB2KPF_DIAGRAM_DECLUTTER=1 \
  python epub2kpf/scripts/kindle_build/rasterize_diagrams.py KDP/output/building-embodied-ai.epub
#   -> KDP/output/building-embodied-ai-diagrams.epub

# validate
java -jar epubcheck.jar KDP/output/building-embodied-ai-diagrams.epub   # expect 0/0/0/0
```

## KDP form fields

### Kindle eBook Details
- **Language:** English
- **Book Title:** Building Embodied AI
- **Subtitle:** From Perception to Autonomous Action
- **Series:** Hands-On AI Science (add as a series; this is a volume in it)
- **Edition number:** 2
- **Author:** Alexander Apartsin
- **Contributor:** Yehudit Aperstein (Author)
- **Description:** paste the contents of `KDP/metadata/description.html` (2,601 chars, well under the 4,000 limit; KDP accepts the `<h4>`, `<b>`, `<i>`, `<ul>`/`<li>` tags used)
- **Publishing rights:** "I own the copyright and I hold the necessary publishing rights."
- **Keywords (7):** from `metadata.yaml`:
  1. embodied AI robotics textbook
  2. robot learning reinforcement learning
  3. vision language action models VLA
  4. robot foundation models manipulation
  5. sim to real robotics MuJoCo Isaac
  6. imitation learning diffusion policy
  7. humanoid robot control deep learning
- **Categories (up to 3 BISAC):**
  - COMPUTERS / Artificial Intelligence / General (COM004000)
  - COMPUTERS / Robotics (COM021030)
  - TECHNOLOGY & ENGINEERING / Robotics (TEC037000)
- **Age range / Reading age:** not applicable (professional / scholarly)

### AI content disclosure (REQUIRED — do not skip)
KDP asks whether you used AI tools. Answer **Yes**, and disclose:
- **AI-generated text:** yes. The manuscript was drafted by a staged pipeline of AI
  writing agents under the authors' direction and review.
- **AI-generated images:** yes. The cover, chapter illustrations, and diagrams are
  AI-generated.
- **AI-generated translations:** none.

This disclosure is for KDP's records and is **not shown to customers**. AI-generated
content is permitted on KDP *when disclosed*; failing to disclose is what triggers
removal. The copyright page also states the book was AI-produced, so the listing,
the book, and the disclosure are consistent.

### Freely-available-content note (acceptance risk to pre-empt)
The same material may exist as a public website. KDP can block content that is
"freely available on the web" **unless you are the copyright holder** - which the
authors are (select the "I own the copyright" rights option). To avoid a false flag:
- Do **not** put the free website URL anywhere in the title, subtitle, description, or keywords.
- The Kindle edition is a distinct, formatted product (no site chrome, no nav bars,
  reflowable, rasterized figures); the copyright page no longer says "web edition".
- If KDP's review flags it, reply that you are the sole copyright holder and that the
  Kindle edition is your own work published with your permission.

### Kindle eBook Content
- **Manuscript:** upload `KDP/output/building-embodied-ai-diagrams.epub`
- **Cover:** upload `KDP/cover/book-cover-kdp.jpg`

### Kindle eBook Pricing
- **Territories:** All
- **Royalty & price:** author choice.
  - 70% royalty requires a list price of USD 2.99-9.99 and incurs a delivery fee of
    ~USD 0.15/MB (~USD 6.3 on this 42 MB file per sale).
  - 35% royalty has **no** delivery fee and no price-band restriction; for a large,
    image-heavy technical book this is often the better net at higher list prices.
- **DRM:** recommendation - do not enable.

## Pre-upload checklist
- [ ] `building-embodied-ai-diagrams.epub` present, EPUBCheck 0/0/0/0
- [ ] Cover is exactly 1600 x 2560, baseline JPEG, sRGB
- [ ] Description pasted from `KDP/metadata/description.html`
- [ ] Title/subtitle match the book exactly; no keyword stuffing in the title
- [ ] 7 keywords, 3 categories set
- [ ] AI-content disclosure answered (text + images = AI-generated)
- [ ] Rights = "I own the copyright"
- [ ] No web URLs in any metadata field
- [ ] Copyright page reads as an edition (not "web edition") - confirmed
- [ ] Spot-check the EPUB in Kindle Previewer 3 (math, code, figures, TOC, cross-reference links)
