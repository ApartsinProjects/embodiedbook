# KDP Upload Metadata — Building Embodied AI (Second Edition)

Copy-paste sheet for the KDP dashboard. File-embedded fields (title, authors,
language, rights) already match the EPUB/KPF OPF; the fields below are the
ones you enter or select at upload.

Upload file: `KDP/output/kpf_final/KPF/building-embodied-ai-kindle-mz.kpf`
(upload the .kpf, not the EPUB, so KDP skips its server-side conversion.)

---

## Core fields

| Field | Value |
|---|---|
| **Title** | Building Embodied AI |
| **Subtitle** | From Perception to Autonomous Action |
| **Edition Number** | 2 |
| **Language** | English |
| **Authors** | Alexander Apartsin; Yehudit Aperstein |
| **Publisher** | Apartsin & Aperstein |
| **Publication date** | 2026 |
| **ISBN** | (leave blank — KDP assigns a free ASIN) |
| **Adult content** | No |

---

## Keywords (7 max — KDP counts these as 7 slots)

Phrase-style search strings (not single words), each targeting how buyers actually
search. Enter one per slot:

1. `embodied AI robotics textbook`
2. `robot learning reinforcement learning`
3. `vision language action models VLA`
4. `robot foundation models manipulation`
5. `sim to real robotics MuJoCo Isaac`
6. `imitation learning diffusion policy`
7. `humanoid robot control deep learning`

**Rationale:** each phrase blends a core topic with a high-intent qualifier
(textbook / models / control) so the listing matches both broad ("embodied AI")
and specific ("diffusion policy", "sim to real") queries. Avoid repeating words
already in the title/subtitle ("embodied", "perception") — KDP already indexes those.

### Alternate keyword pool (swap in if you want a different emphasis)
- `robotics deep learning practitioner guide`
- `world models model-based reinforcement learning`
- `SLAM localization mapping robotics`
- `robot perception sensor fusion`
- `multi-agent robotics human robot interaction`
- `autonomous robots AI engineering`
- `PPO policy gradient robotics`

---

## BISAC categories (choose up to 3 in the dashboard)

Primary and two supporting, ordered by fit:

1. **COM004000** — COMPUTERS / Artificial Intelligence / General
   *(primary; the book's umbrella subject)*
2. **COM021030** — COMPUTERS / Robotics *(closest robotics-specific code)*
3. **TEC037000** — TECHNOLOGY & ENGINEERING / Robotics
   *(engineering-shelf reach for the controls/hardware audience)*

### Alternates (if KDP's browsable category picker steers you elsewhere)
- **COM004030** — COMPUTERS / Artificial Intelligence / Neural Networks (deep learning)
- **COM014000** — COMPUTERS / Computer Science
- **TEC009000** — TECHNOLOGY & ENGINEERING / Engineering (General)
- **SCI079000** — SCIENCE / System Theory

> KDP's UI browses categories by name (not raw BISAC codes). Match the code above
> to its path: e.g. COM004000 = Computers ▸ Artificial Intelligence ▸ General.
> After publishing you can email KDP to add up to 10 categories total.

---

## Description (paste into the Description box; supports light HTML)

<p><strong>The complete, hands-on guide to building agents that perceive, reason, and act in the physical world.</strong></p>

<p>Embodied AI is where machine learning meets the real world: robots and agents that see, move, manipulate, and adapt. <em>Building Embodied AI</em> takes you from first principles to production systems across twelve parts, blending the mathematics of robotics and control with the modern deep-learning stack that powers today's robot foundation models.</p>

<p><strong>What you'll learn:</strong></p>
<ul>
<li>Foundations of embodied agents, the agent-environment interface, and system architectures</li>
<li>Robotics and control math: kinematics, dynamics, state estimation, and sensor fusion</li>
<li>The modern simulation stack: MuJoCo, MJX, Isaac Lab, and Genesis, plus sim-to-real transfer</li>
<li>Reinforcement learning for control: policy gradients, PPO, and reward design</li>
<li>Learning from demonstration: imitation learning, action chunking, and diffusion policies</li>
<li>Embodied perception: SLAM, localization, and mapping</li>
<li>Language, vision, and action: VLMs, vision-language-action (VLA) models, and cross-embodiment learning</li>
<li>World models and model-based control; manipulation, locomotion, and whole-body humanoid control</li>
<li>Multi-agent and human-centered embodiment, plus evaluation, safety, robustness, and deployment</li>
<li>Capstone projects and a full course-design guide for instructors</li>
</ul>

<p>Every concept pairs the underlying theory with runnable code and a "right tool" shortcut showing the same task in a few lines with a modern library. Written for engineers, researchers, and graduate students who want both the depth to understand how embodied systems work and the practical skill to build them.</p>

<p><em>Second Edition — fully revised and expanded.</em></p>

---

## Pre-upload checklist

- [ ] Upload `building-embodied-ai-kindle-mz.kpf` (91.7 MB, 0 errors / 0 quality issues)
- [ ] Set Edition Number = 2
- [ ] Enter the 7 keywords above
- [ ] Select up to 3 BISAC categories (COM004000, COM021030, TEC037000)
- [ ] Paste the description
- [ ] Confirm cover renders in the KDP previewer
- [ ] Royalty tier decision: 35% (no delivery fee, best for this 91.7 MB file) vs 70% (delivery fee ~$13.8/sale at this size)
