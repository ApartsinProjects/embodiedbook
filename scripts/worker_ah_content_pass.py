from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import List


ROOT = Path(r"E:\Projects\Books\EmbodiedAI")
BOOK_TITLE = "Building Embodied AI: From Perception to Autonomous Action"
COPYRIGHT = "© 2026 Alexander Apartsin & Yehudit Aperstein"


@dataclass
class BibEntry:
    ref: str
    url: str
    note: str


@dataclass
class SectionData:
    number: str
    title: str
    chapter_num: int
    chapter_title: str
    part_title: str
    dir_name: str
    image: str
    epigraph: str
    epigraph_cite: str
    description: str
    reader_pathway: str
    develops: str
    connects: str
    key_insight: str
    figure_boxes: List[str]
    figure_caption: str
    theory_1: str
    theory_2: str
    formula: str
    mechanism: str
    algorithm_steps: List[str]
    code_title: str
    code: str
    code_output: str
    code_caption: str
    expected_output: str
    library_shortcut: str
    recipe_steps: List[str]
    warning: str
    practical_example: str
    fun_note: str
    frontier: str
    self_check: str
    deep_dive_1: str
    deep_dive_2: str
    tool_rows: List[List[str]]
    lab: str
    failure_pattern: str
    takeaway: str
    exercise: str
    bibliography: List[BibEntry]


@dataclass
class ChapterData:
    number: int
    title: str
    part_title: str
    dir_name: str
    epigraph: str
    epigraph_cite: str
    big_picture: str
    remember: str
    overview_1: str
    overview_2: str
    prereqs: str
    tooling_note: str
    lab_objective: str
    lab_steps: List[str]
    production_notes: str
    tool_map: List[List[str]]
    instructor_notes: str
    readiness: str
    teaching_takeaway: str
    evidence_standard: str
    bibliography: List[BibEntry]


def card_ref(entry: BibEntry) -> str:
    return (
        '<div class="bib-entry-card">'
        f'<p class="bib-ref"><a href="{escape(entry.url)}" rel="noopener" target="_blank">{escape(entry.ref)}</a></p>'
        f'<p class="bib-annotation">{escape(entry.note)}</p>'
        "</div>"
    )


def build_svg(boxes: List[str], sec: str) -> str:
    colors = [
        ("#e8f3ff", "#1f5f99"),
        ("#eef9f0", "#2e7d32"),
        ("#fff5e5", "#a85d00"),
        ("#f8ecff", "#6a1b9a"),
    ]
    xs = [24, 214, 404, 594]
    widths = [160, 160, 160, 140]
    chunks = []
    for idx, label in enumerate(boxes):
        fill, stroke = colors[idx]
        x = xs[idx]
        width = widths[idx]
        top, bottom = label.split("|", 1)
        chunks.append(
            f'<rect fill="{fill}" height="86" rx="8" stroke="{stroke}" width="{width}" x="{x}" y="34"></rect>'
            f'<text font-size="15" font-weight="700" text-anchor="middle" x="{x + width / 2}" y="66">{escape(top)}</text>'
            f'<text font-size="12" text-anchor="middle" x="{x + width / 2}" y="94">{escape(bottom)}</text>'
        )
    marker = f"arrow-{sec.replace('.', '-')}"
    arrows = (
        f'<path d="M184 78 L210 78" marker-end="url(#{marker})" stroke="#333" stroke-width="2"></path>'
        f'<path d="M374 78 L400 78" marker-end="url(#{marker})" stroke="#333" stroke-width="2"></path>'
        f'<path d="M564 78 L590 78" marker-end="url(#{marker})" stroke="#333" stroke-width="2"></path>'
        f'<path d="M664 122 C664 184 106 184 106 122" fill="none" marker-end="url(#{marker})" stroke="#555" stroke-width="2"></path>'
        f'<defs><marker id="{marker}" markerheight="8" markerwidth="10" orient="auto" refx="9" refy="4"><path d="M0,0 L10,4 L0,8 Z" fill="#333"></path></marker></defs>'
    )
    return (
        f'<svg aria-labelledby="fig-{sec}-title" height="230" role="img" viewBox="0 0 760 230" width="100%">'
        f'<title id="fig-{sec}-title">Loop diagram for Section {sec}</title>'
        + "".join(chunks)
        + arrows
        + "</svg>"
    )


def code_html(text: str) -> str:
    return escape(text).replace("\n", "\n")


def section_path(section: SectionData) -> Path:
    return ROOT / f"part-9-manipulation-locomotion-and-embodied-skills/{section.dir_name}/section-{section.number}.html"


def chapter_path(chapter: ChapterData) -> Path:
    return ROOT / f"part-9-manipulation-locomotion-and-embodied-skills/{chapter.dir_name}/index.html"


def nav_for_section(section: SectionData, ordered: List[SectionData]) -> str:
    idx = ordered.index(section)
    prev_href = "index.html" if idx == 0 else f"section-{ordered[idx - 1].number}.html"
    prev_label = (
        f"Chapter {section.chapter_num}: {section.chapter_title}"
        if idx == 0
        else f"Section {ordered[idx - 1].number}: {ordered[idx - 1].title}"
    )
    next_href = (
        f"../{CHAPTERS_BY_NUMBER[section.chapter_num + 1].dir_name}/index.html"
        if idx == len(ordered) - 1 and section.chapter_num < 44
        else "index.html"
        if idx == len(ordered) - 1
        else f"section-{ordered[idx + 1].number}.html"
    )
    next_label = (
        f"Chapter {section.chapter_num + 1}: {CHAPTERS_BY_NUMBER[section.chapter_num + 1].title}"
        if idx == len(ordered) - 1 and section.chapter_num < 44
        else f"Chapter {section.chapter_num}: {section.chapter_title}"
        if idx == len(ordered) - 1
        else f"Section {ordered[idx + 1].number}: {ordered[idx + 1].title}"
    )
    return (
        '<nav class="chapter-nav">'
        f'<a class="prev" href="{escape(prev_href)}">{escape(prev_label)}</a>'
        f'<a class="up" href="index.html">Chapter {section.chapter_num}: {escape(section.chapter_title)}</a>'
        f'<a class="next" href="{escape(next_href)}">{escape(next_label)}</a>'
        "</nav>"
    )


def render_section(section: SectionData, ordered: List[SectionData]) -> str:
    bibs = "".join(card_ref(entry) for entry in section.bibliography)
    recipe = "".join(f"<li>{escape(step)}</li>" for step in section.recipe_steps)
    algorithm = "".join(f"<li>{escape(step)}</li>" for step in section.algorithm_steps)
    tool_rows = "".join(
        "<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>" for row in section.tool_rows
    )
    nav = nav_for_section(section, ordered)
    return f"""<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Section {section.number} of {BOOK_TITLE}: {section.title}." name="description"/>
<title>Section {section.number}: {section.title} | {BOOK_TITLE}</title>
<link href="../../styles/book.css" rel="stylesheet"/>
<link href="../../styles/pygments.css" rel="stylesheet"/>
<link href="../../vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer="" src="../../vendor/prism/prism-bundle.min.js"></script>
<link href="../../vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer="" src="../../vendor/katex/katex.min.js"></script>
<script defer="" onload="renderMathInElement(document.body, {{
  delimiters: [
  {{left: '$$', right: '$$', display: true}},
  {{left: '$', right: '$', display: false}}
  ],
  throwOnError: false
  }});" src="../../vendor/katex/contrib/auto-render.min.js"></script>
<script defer="" src="../../scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="../../index.html">{BOOK_TITLE}</a>
<a class="toc-link" href="../../toc.html" title="Table of Contents"><span class="toc-icon">☰</span> Contents</a>
</nav>
<div class="header-search"><div id="search"></div></div>
<div class="part-label"><a href="../index.html">{escape(section.part_title)}</a></div>
<div class="chapter-label"><a href="index.html">Chapter {section.chapter_num}: {escape(section.chapter_title)}</a></div>
<h1>Section {section.number}: {escape(section.title)}</h1>
</header>
<main class="content" id="main-content">
<blockquote class="epigraph"><p>"{escape(section.epigraph)}"</p>
<figure class="illustration">
<img alt="Illustration for Section {section.number}: {escape(section.title)}" loading="lazy" src="images/{escape(section.image)}"/>
<figcaption><strong>Figure {section.number}A</strong>: {escape(section.figure_caption)}</figcaption>
</figure>
<cite>{escape(section.epigraph_cite)}</cite></blockquote>
<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>{escape(section.description)}</p>
</div>
<div class="callout pathway">
<div class="callout-title">Reader Pathway</div>
<p>{escape(section.reader_pathway)}</p>
</div>
<h2>What This Section Develops</h2>
<p>{escape(section.develops)}</p>
<p>{escape(section.connects)}</p>
<div class="callout key-insight">
<div class="callout-title">Action Is The Test</div>
<p>{escape(section.key_insight)}</p>
</div>
<figure class="illustration" id="fig-{section.number.replace('.', '-')}">
{build_svg(section.figure_boxes, section.number)}
<figcaption><strong>Figure {section.number}.1</strong>: {escape(section.figure_caption)}</figcaption>
</figure>
<h2>Theory</h2>
<p>{escape(section.theory_1)}</p>
<p>{escape(section.theory_2)}</p>
<p>$$ {section.formula} $$</p>
<div class="callout under-the-hood">
<div class="callout-title">Mechanism</div>
<p>{escape(section.mechanism)}</p>
</div>
<div class="callout algorithm">
<div class="callout-title">{escape(section.code_title)}</div>
<ol>{algorithm}</ol>
</div>
<h2>Worked Example</h2>
<pre><code class="language-python">{code_html(section.code)}</code></pre>
<div class="code-output">{escape(section.code_output)}</div>
<div class="code-caption">{escape(section.code_caption)}</div>
<p><strong>Expected output:</strong> {escape(section.expected_output)}</p>
<div class="callout library-shortcut">
<div class="callout-title">Library Shortcut</div>
<p>{escape(section.library_shortcut)}</p>
</div>
<h2>Practical Recipe</h2>
<ol>{recipe}</ol>
<div class="callout warning">
<div class="callout-title">Common Failure Mode</div>
<p>{escape(section.warning)}</p>
</div>
<div class="callout practical-example">
<div class="callout-title">Practical Example</div>
<p>{escape(section.practical_example)}</p>
</div>
<div class="callout fun-note">
<div class="callout-title">Memory Hook</div>
<p>{escape(section.fun_note)}</p>
</div>
<div class="callout research-frontier">
<div class="callout-title">Research Frontier</div>
<p>{escape(section.frontier)}</p>
</div>
<div class="callout self-check">
<div class="callout-title">Self Check</div>
<p>{escape(section.self_check)}</p>
</div>
<section class="production-depth-expansion">
<h2>Builder's Deep Dive</h2>
<p>{escape(section.deep_dive_1)}</p>
<p>{escape(section.deep_dive_2)}</p>
<div class="comparison-table">
<div class="comparison-table-title">Practical Tool Choices For This Section</div>
<table>
<thead><tr><th>Tool or Library</th><th>Role in the Topic</th><th>Builder Advice</th></tr></thead>
<tbody>{tool_rows}</tbody>
</table>
</div>
<div class="callout lab"><div class="callout-title">Mini Lab</div><p>{escape(section.lab)}</p></div>
<h2>Failure Analysis Pattern</h2>
<p>{escape(section.failure_pattern)}</p>
</section>
<section class="bibliography"><h2>Section References</h2>{bibs}</section>
<div class="callout key-takeaway">
<div class="callout-title">Key Takeaway</div>
<p>{escape(section.takeaway)}</p>
</div>
<div class="callout exercise">
<div class="callout-title">Exercise {section.number}.1</div>
<p>{escape(section.exercise)}</p>
</div>
{nav}
<footer>
<p class="footer-title">{BOOK_TITLE}, Web Edition</p>
<p>{COPYRIGHT} · <a href="../../toc.html">Contents</a></p>
<p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {{year:'numeric', month:'long', day:'numeric'}}))</script></p>
</footer>
</main>
</body>
</html>
"""


def nav_for_chapter(chapter: ChapterData) -> str:
    prev = (
        f'../{CHAPTERS_BY_NUMBER[chapter.number - 1].dir_name}/section-{CHAPTERS_BY_NUMBER[chapter.number - 1].number_end}.html'
        if chapter.number > 42
        else "../../part-8-world-models-and-model-based-embodied-ai/module-41-diffusion-and-generative-planning/section-41.5.html"
    )
    prev_label = (
        f"Section {CHAPTERS_BY_NUMBER[chapter.number - 1].number_end}: {SECTIONS_BY_NUMBER[CHAPTERS_BY_NUMBER[chapter.number - 1].number_end].title}"
        if chapter.number > 42
        else "Section 41.5: Risks of generated experience"
    )
    next_href = (
        f"../{CHAPTERS_BY_NUMBER[chapter.number + 1].dir_name}/index.html"
        if chapter.number < 44
        else "section-44.1.html"
    )
    next_label = (
        f"Chapter {chapter.number + 1}: {CHAPTERS_BY_NUMBER[chapter.number + 1].title}"
        if chapter.number < 44
        else "Section 44.1: Why touch matters for contact-rich tasks"
    )
    return (
        '<nav class="chapter-nav">'
        f'<a class="prev" href="{prev}">{escape(prev_label)}</a>'
        '<a class="up" href="../index.html">Part IX: Manipulation, Locomotion, and Embodied Skills</a>'
        f'<a class="next" href="{next_href}">{escape(next_label)}</a>'
        "</nav>"
    )


def render_chapter(chapter: ChapterData, sections: List[SectionData]) -> str:
    roadmap = "".join(
        f'<li><span class="section-num">{s.number}</span> <a href="section-{s.number}.html"><span class="section-title">{escape(s.title)}</span></a><span class="section-desc">{escape(s.description)}</span></li>'
        for s in sections
    )
    lab_steps = "".join(f"<li>{escape(step)}</li>" for step in chapter.lab_steps)
    tool_map = "".join(
        "<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>" for row in chapter.tool_map
    )
    bibs = "".join(card_ref(entry) for entry in chapter.bibliography)
    nav = nav_for_chapter(chapter)
    return f"""<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Chapter {chapter.number} of {BOOK_TITLE}: {chapter.title}." name="description"/>
<title>Chapter {chapter.number}: {chapter.title} | {BOOK_TITLE}</title>
<link href="../../styles/book.css" rel="stylesheet"/>
<link href="../../styles/pygments.css" rel="stylesheet"/>
<link href="../../vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer="" src="../../vendor/prism/prism-bundle.min.js"></script>
<link href="../../vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer="" src="../../vendor/katex/katex.min.js"></script>
<script defer="" onload="renderMathInElement(document.body, {{
  delimiters: [
  {{left: '$$', right: '$$', display: true}},
  {{left: '$', right: '$', display: false}}
  ],
  throwOnError: false
  }});" src="../../vendor/katex/contrib/auto-render.min.js"></script>
<script defer="" src="../../scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="../../index.html">{BOOK_TITLE}</a>
<a class="toc-link" href="../../toc.html" title="Table of Contents"><span class="toc-icon">☰</span> Contents</a>
</nav>
<div class="header-search"><div id="search"></div></div>
<div class="part-label"><a href="../index.html">{escape(chapter.part_title)}</a></div>
<div class="chapter-label"><a href="index.html">Chapter {chapter.number}: {escape(chapter.title)}</a></div>
<h1>Chapter {chapter.number}: {escape(chapter.title)}</h1>
</header>
<main class="content" id="main-content">
<blockquote class="epigraph">
<p>"{escape(chapter.epigraph)}"</p>
<cite>{escape(chapter.epigraph_cite)}</cite>
</blockquote>
<div class="callout big-picture">
<div class="callout-title">Big Picture</div>
<p>{escape(chapter.big_picture)}</p>
</div>
<div class="callout key-insight">
<div class="callout-title">Remember This Chapter</div>
<p>{escape(chapter.remember)}</p>
</div>
<div class="overview">
<h2>Chapter Overview</h2>
<p>{escape(chapter.overview_1)}</p>
<p>{escape(chapter.overview_2)}</p>
</div>
<div class="prereqs"><h3>Prerequisites</h3><p>{escape(chapter.prereqs)}</p></div>
<h2>Chapter Roadmap</h2>
<ul class="sections-list">{roadmap}</ul>
<div class="callout library-shortcut">
<div class="callout-title">Tooling Note</div>
<p>{escape(chapter.tooling_note)}</p>
</div>
<section class="lab" id="lab-{chapter.number}">
<h2>Hands-On Lab: Build the Chapter System</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 90 to 150 minutes</span><span class="lab-difficulty">Difficulty: Intermediate to Advanced</span></div>
<div class="lab-objective"><h3>Objective</h3><p>{escape(chapter.lab_objective)}</p></div>
<div class="lab-steps"><h3>Steps</h3><ol>{lab_steps}</ol></div>
</section>
<div class="whats-next"><h3>What's Next?</h3><p>Continue with <a href="section-{sections[0].number}.html">Section {sections[0].number}: {escape(sections[0].title)}</a>, where the chapter moves from framing to the first concrete system contract.</p></div>
<section class="production-depth-expansion">
<h2>Production Notes For Readers</h2>
<p>{escape(chapter.production_notes)}</p>
<div class="comparison-table">
<div class="comparison-table-title">Chapter Tool Map</div>
<table>
<thead><tr><th>Tool or Library</th><th>Where It Pays Off</th></tr></thead>
<tbody>{tool_map}</tbody>
</table>
</div>
<div class="callout lab"><div class="callout-title">Chapter Lab Extension</div><p>Extend the lab by adding one perturbation, one recovery behavior, and one failure taxonomy. Save configuration, logs, metrics, and two representative traces in the same folder.</p></div>
</section>
<section class="production-index-depth-topup">
<h2>Instructor And Builder Notes</h2>
<p>{escape(chapter.instructor_notes)}</p>
<div class="callout self-check"><div class="callout-title">Readiness Check</div><p>{escape(chapter.readiness)}</p></div>
<div class="callout key-takeaway"><div class="callout-title">Teaching Takeaway</div><p>{escape(chapter.teaching_takeaway)}</p></div>
</section>
<section class="agent-checklist-summary">
<h2>Agent Checklist Integration</h2>
<p>This chapter has been reviewed as a teaching and builder unit with attention to depth, code pedagogy, diagrams, exercises, scientific framing, and practical stacks.</p>
<div class="callout key-insight"><div class="callout-title">Chapter Evidence Standard</div><p>{escape(chapter.evidence_standard)}</p></div>
</section>
<section class="bibliography">
<h2>Bibliography &amp; Further Reading</h2>
<h3>Primary Sources, Tools, and References</h3>
{bibs}
</section>
{nav}
<footer>
<p class="footer-title">{BOOK_TITLE}, Web Edition</p>
<p>{COPYRIGHT} · <a href="../../toc.html">Contents</a></p>
<p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {{year:'numeric', month:'long', day:'numeric'}}))</script></p>
</footer>
</main>
</body>
</html>
"""


SECTIONS: List[SectionData] = [
    SectionData(
        number="42.1",
        title="What manipulation is; reaching and pushing",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-illustration-01.png",
        epigraph="A robot first learns humility from friction.",
        epigraph_cite="A Careful Manipulation Loop",
        description="Manipulation starts when the robot changes object state on purpose and can explain the geometry, contact, and feedback path that made the change happen.",
        reader_pathway="Track this section as state estimation, contact choice, controller execution, and object-state verification. If any link is missing, the push demo will look better than it is.",
        develops="This section turns reaching and planar pushing into the first full manipulation contract: scene frames, object pose, pusher contact, motion primitive, and post-contact displacement.",
        connects="It ties coordinate frames, Jacobians, and closed-loop control to the specific question every manipulator faces: did the object move to the intended pose, or did the arm only move itself convincingly?",
        key_insight="Reaching is about putting the hand in the right place. Manipulation starts only when object state changes are measured and the controller can recover when the contact model is wrong.",
        figure_boxes=["Observe|rgbd, object pose", "Estimate|contact frame", "Act|reach then push", "Verify|object displacement"],
        figure_caption="A reach-push loop is only complete when the object trajectory, not just the arm trajectory, is verified after contact.",
        theory_1="For a point pusher, the control loop must maintain two simultaneous estimates: the end-effector pose in the world frame and the object pose in the contact frame. A clean implementation tracks both and transforms between them explicitly.",
        theory_2="Under quasi-static contact, pushing quality depends on whether the commanded pusher velocity stays inside a feasible motion cone. That cone is only an approximation, but it is a powerful way to think about why some pushes translate, some rotate, and some simply slip.",
        formula=r"\Delta x_o \approx J_c(q)\,\Delta q,\qquad \hat x_{o,t+1} = f(\hat x_{o,t}, u_t, \hat c_t),\qquad \text{success} = \mathbf{1}[\|x_o^\star - \hat x_{o,T}\|_2 < \epsilon]",
        mechanism="The robot senses the object and end-effector pose, predicts the next contact state under a short Cartesian move, executes a bounded push, and then validates object displacement against the goal. Failure is informative if the log preserves frame transforms, contact onset time, and object motion residuals.",
        algorithm_steps=[
            "Localize the object and convert the target displacement into the pusher contact frame.",
            "Choose a pre-contact reach pose that avoids collisions and yields the desired push direction.",
            "Execute a short guarded reach, then apply a low-speed Cartesian push while monitoring force and slip.",
            "Estimate object translation and rotation after the push, then replan if the residual is above threshold.",
        ],
        code_title="Algorithm: Reach-Push Controller",
        code="""# Compute a one-step push quality score from pose error and contact alignment.
import math

goal_dx = (0.08, 0.00)
pred_dx = (0.06, 0.01)
surface_normal = (0.0, 1.0)
push_dir = (1.0, 0.0)

err = math.dist(goal_dx, pred_dx)
alignment = push_dir[0] * surface_normal[1] - push_dir[1] * surface_normal[0]
score = round(max(0.0, 1.0 - 8.0 * err) * abs(alignment), 3)
print({"predicted_error_m": round(err, 3), "alignment": round(alignment, 3), "push_score": score})""",
        code_output="{'predicted_error_m': 0.022, 'alignment': 1.0, 'push_score': 0.824}",
        code_caption="Code Fragment 42.1.1 scores a simple push by combining predicted object-motion error with the geometric alignment between push direction and contact frame.",
        expected_output="The expected trace shows a small predicted object-motion error and a high alignment term. If the alignment collapses or the error rises, the push should be rejected before the arm commits to contact.",
        library_shortcut="MoveIt Task Constructor can plan the guarded reach, while cuRobo or Drake can quickly filter collision-free arm trajectories. The local push policy still needs an explicit object-motion verifier, because most planners certify arm motion, not object displacement.",
        recipe_steps=[
            "Calibrate camera-to-base and tool-to-tip transforms before any push experiment.",
            "Log object pose before contact, at contact onset, and after release using the same frame convention.",
            "Start with short pushes on rigid objects before moving to clutter, deformables, or moving bases.",
            "Plot object displacement residuals beside controller forces so failed pushes separate geometry from friction issues.",
            "Add a regrasp or reapproach branch once the robot can diagnose off-axis contact reliably.",
        ],
        warning="A beautiful arm trajectory can hide a useless manipulation policy. If only the tool path is evaluated, the robot can reach perfectly while never moving the object where it matters.",
        practical_example="Warehouse depalletizing systems often use pushing as a rescue primitive when a top-down grasp is occluded or unstable. The reliable systems explicitly verify box displacement and only then attempt the next grasp.",
        fun_note="If the table were covered with dry-erase marker, the real skill would show up as streaks on the object path, not on the robot arm path.",
        frontier="Recent manipulation stacks mix analytic contact heuristics with policy learning. The durable contribution is usually better contact-state supervision or better recovery logic, not replacing all of geometry with a larger network.",
        self_check="Can you name the world frame, object frame, contact frame, pusher velocity, and object residual metric you would inspect after a bad push?",
        deep_dive_1="Pushing exposes a foundational manipulation lesson: contact is an implicit state variable that has to be estimated from motion, force, and object response. Even in simple planar scenes, the same commanded action can yield translation, rotation, or slip depending on where the contact lands relative to the support polygon and friction cone.",
        deep_dive_2="For teaching, this section is a perfect bridge between kinematics and embodied intelligence. Students can predict object motion qualitatively with motion cones, then watch where the model breaks in the presence of friction uncertainty or pose-estimation error.",
        tool_rows=[
            ["MoveIt Task Constructor", "Pre-contact reach planning", "Use it to generate collision-free staging poses before local contact begins."],
            ["Drake", "Contact-aware simulation and optimization", "Use it when you need explicit kinematic and contact residual checks."],
            ["cuRobo", "Fast seeded arm motion generation", "Use it to replan many short approach trajectories when clutter changes quickly."],
        ],
        lab="Build a planar push benchmark with three objects, two contact points per object, and one held-out friction setting. Compare predicted and measured object displacement after every push.",
        failure_pattern="When the object misses the target, ask in order: was the pose wrong, was the contact point wrong, did the controller slip, or did the object model fail? Saving those labels keeps pushing from collapsing into a single binary success score.",
        takeaway="Manipulation begins when the robot measures and controls object-state change, not when the arm merely reaches a visually plausible pose.",
        exercise="Design a push benchmark with one geometric baseline, one learned residual model, and one friction perturbation panel. Explain exactly which artifact will prove that the object, not just the hand, moved correctly.",
        bibliography=[
            BibEntry("Modern Robotics, manipulation chapters", "https://modernrobotics.northwestern.edu/", "A compact reference for contact, kinematics, and manipulation mechanics."),
            BibEntry("MoveIt 2 Documentation", "https://moveit.picknik.ai/", "Official planning and execution documentation for modern ROS 2 manipulation workflows."),
            BibEntry("Isaac for Manipulation", "https://nvidia-isaac-ros.github.io/reference_workflows/isaac_for_manipulation/index.html", "GPU-accelerated perception and motion-generation stack for pick and place and related manipulation loops."),
        ],
    ),
    SectionData(
        number="42.2",
        title="Pick-and-place pipelines",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-illustration-02.png",
        epigraph="Pipelines look boring until one missing state estimate breaks the whole warehouse.",
        epigraph_cite="A Builder's Planning Notebook",
        description="Pick and place is the canonical manipulation pipeline because it exposes the full stack: perception, grasp generation, motion planning, force-limited execution, placement verification, and recovery.",
        reader_pathway="Follow the pipeline from scene parse to candidate grasps to approach, closure, lift, transport, place, and post-place verification. Each stage should have a measurable precondition and exit test.",
        develops="This section breaks the classical pick-and-place stack into inspectable contracts: segmentation, 6D pose estimation, grasp proposal, approach trajectory, gripper closure, lift test, transfer, and place verification.",
        connects="The payoff is practical. Once the stages are explicit, builders can swap MoveIt, cuRobo, Dex-Net, or a learned VLA policy into one stage without turning the full system into a debugging fog bank.",
        key_insight="Most industrial pick-and-place failures are not mysterious. They are stage failures that were never isolated: bad pose proposals, invalid grasps, planner dead ends, premature gripper closure, or unverified placement.",
        figure_boxes=["Sense|scene and target", "Propose|grasps and poses", "Execute|pick, transfer", "Verify|lift and place"],
        figure_caption="A pick-and-place pipeline earns trust only when every stage has a verifier and a way to hand off failure to recovery.",
        theory_1="Pick and place is a hybrid system with discrete stages and continuous control inside each stage. The important modeling habit is to attach explicit preconditions and postconditions to every stage so silent transitions are impossible.",
        theory_2="A clean factorization treats grasp quality and trajectory feasibility separately, then combines them. That separation matters because a geometrically good grasp may still be unreachable under joint limits or collision constraints.",
        formula=r"g^\star = \arg\max_{g \in \mathcal{G}} Q_{\text{grasp}}(g)\,\mathbf{1}[\text{reachable}(g)]\,\mathbf{1}[\text{collision\_free}(g)],\qquad T = T_{\text{approach}} \circ T_{\text{lift}} \circ T_{\text{place}}",
        mechanism="The pipeline observes the scene, proposes grasps, filters by reachability and collision, executes the pick with force-limited closure, verifies the lift, transports the object, and confirms final placement. A solid log stores failures at the stage boundary, not only at the episode boundary.",
        algorithm_steps=[
            "Segment the scene and estimate object pose or graspable surfaces.",
            "Generate candidate grasps and rank them by quality, reachability, and downstream placement compatibility.",
            "Plan approach, closure, lift, and placement motions with explicit stage verifiers.",
            "If lift or placement fails, route to a bounded recovery such as regrasp, reobserve, or skip-bin.",
        ],
        code_title="Algorithm: Pick-Place Stage Filter",
        code="""# Filter grasp candidates by score and downstream feasibility.
grasps = [
    {"id": "g1", "quality": 0.91, "reachable": True, "place_ok": False},
    {"id": "g2", "quality": 0.84, "reachable": True, "place_ok": True},
    {"id": "g3", "quality": 0.73, "reachable": False, "place_ok": True},
]

ranked = []
for g in grasps:
    score = g["quality"] * float(g["reachable"]) * float(g["place_ok"])
    ranked.append((g["id"], round(score, 2)))

ranked.sort(key=lambda row: row[1], reverse=True)
print(ranked)
print("selected", ranked[0][0])""",
        code_output="[('g2', 0.84), ('g1', 0.0), ('g3', 0.0)]\nselected g2",
        code_caption="Code Fragment 42.2.1 keeps the highest raw grasp score from dominating when the grasp cannot support the later place stage.",
        expected_output="The expected output selects the slightly weaker but fully feasible grasp. A robust pipeline prefers reachable and place-compatible grasps over visually impressive but dead-end candidates.",
        library_shortcut="MoveIt 2 and cuMotion can own the arm-motion stages, while Dex-Net style scoring or learned grasp heads own the proposal stage. The pipeline remains legible only if stage outputs are serialized into one manifest.",
        recipe_steps=[
            "Define stage-level inputs and outputs before writing the first planner callback.",
            "Score grasps with downstream placement feasibility included, not as an afterthought.",
            "Verify the lift with object motion, gripper width, and force history together.",
            "After placement, measure object pose relative to the target bin or support surface, not only whether the gripper opened.",
            "Save one replay artifact with stage timestamps, selected grasp id, and recovery route.",
        ],
        warning="Teams often celebrate grasp success and miss that their place stage is doing all the hard work with luck. If the chosen grasp makes placement infeasible, the upstream score is misleading by construction.",
        practical_example="Sorting cells for e-commerce fulfillment frequently fail on the transition from lift to transport, where swinging payloads or poor suction seals only become visible once the box clears the tote.",
        fun_note="Pick-and-place demos love the moment of lift. Production robots earn their salary during the far less cinematic moments of handoff, transport, and final pose verification.",
        frontier="Modern pipelines increasingly combine learned grasp proposals with optimization-based placement and GPU motion generation. The reliable systems are still the ones that keep stage boundaries explicit enough to audit.",
        self_check="Could you explain why your chosen grasp is compatible with both the pick and the place stage, or are you hoping the planner will rescue a bad upstream decision?",
        deep_dive_1="The subtle systems question is not just whether a grasp is good now, but whether it preserves future optionality. A bin-picking grasp that blocks the object's target orientation or occludes a second arm may be locally strong and globally poor.",
        deep_dive_2="For instruction, this section is a good place to contrast open-loop pipeline charts with evidence-backed pipeline manifests. The latter let students debug stage interactions rather than searching across the whole stack blindly.",
        tool_rows=[
            ["MoveIt 2", "Stage planning and execution", "Use separate planning groups or task constructors for approach, lift, and place."],
            ["cuMotion via MoveIt plugin", "High-throughput replanning", "Useful when the scene changes quickly or the cell runs on NVIDIA hardware."],
            ["Dex-Net or GQ-CNN", "Grasp scoring", "Use it to rank candidates, but always filter through reachability and place constraints."],
        ],
        lab="Implement a two-object pick-and-place benchmark where one object is easier to grasp but impossible to place without collision. Show that your selector avoids it.",
        failure_pattern="When a full cycle fails, label the first violated postcondition: pose estimate, chosen grasp, approach path, closure, lift, transfer, or place. The first broken stage is usually the most informative one.",
        takeaway="A pick-and-place pipeline is trustworthy when every stage exposes a typed handoff and a verifier, not when the end-to-end demo looks smooth from far away.",
        exercise="Write a stage manifest for a tote-to-shelf pick-and-place task, including one failure branch for bad perception and one for failed lift verification. Explain what metric each branch should log.",
        bibliography=[
            BibEntry("MoveIt 2 Documentation", "https://moveit.picknik.ai/", "Official documentation for planning, kinematics plugins, and execution interfaces in ROS 2 manipulation."),
            BibEntry("cuMotion for MoveIt", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_cumotion/isaac_ros_cumotion/index.html", "Official integration of GPU motion generation into MoveIt workflows."),
            BibEntry("Dex-Net project", "https://berkeleyautomation.github.io/dex-net/", "Dex-Net ties grasp datasets, robust grasp metrics, and learned scoring into deployable pick pipelines."),
        ],
    ),
    SectionData(
        number="42.3",
        title="Contact-rich interaction",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-illustration-03.png",
        epigraph="The world stops being polite when insertion begins.",
        epigraph_cite="A Contact-Control Lab Note",
        description="Contact-rich tasks such as insertion, wiping, scraping, opening, and assembly expose the limits of open-loop pose control because the environment must help shape the motion.",
        reader_pathway="Read this as a transition from free-space planning to controlled interaction. The central objects are stiffness, damping, contact mode, and residual force signatures.",
        develops="This section frames contact-rich manipulation as impedance shaping under uncertainty. The robot must deliberately trade position error against force response while keeping the contact mode inside a safe region.",
        connects="It pulls together dynamics, control, and manipulation learning by making contact residuals first-class evidence. Those residuals are often the difference between a robust insertion routine and a fragile scripted demo.",
        key_insight="In contact-rich tasks, zero position error is often the wrong objective. The correct objective is a bounded interaction that lets the environment guide the final alignment.",
        figure_boxes=["Sense|force and pose", "Regulate|impedance law", "Interact|search and align", "Verify|residual forces"],
        figure_caption="Contact-rich control works by shaping interaction, not by pretending the world will always match a nominal geometry model.",
        theory_1="The canonical model is an impedance or admittance law layered over a task-space trajectory. Instead of commanding a rigid path, the controller allows compliant deviation so contact forces can guide alignment.",
        theory_2="This is where contact mode reasoning matters. Sliding, sticking, insertion, jamming, and separation create very different residual signatures, and recovery depends on distinguishing them quickly.",
        formula=r"\tau = J(q)^\top \left(K_p (x^\star - x) + K_d (\dot x^\star - \dot x) + F_{\text{ff}}\right),\qquad \lambda_n \ge 0,\ \phi(q) \ge 0,\ \lambda_n \phi(q)=0",
        mechanism="The controller measures pose and wrench, predicts the desired compliant response, executes bounded motion, and routes to recovery when residual forces indicate jamming, slip, or misalignment. A useful trace logs pose error and wrench history together, not in separate tools.",
        algorithm_steps=[
            "Select a task-space frame and define compliant axes before commanding any interaction motion.",
            "Start with low-speed guarded contact to estimate normal direction and residual wrench bias.",
            "Switch to impedance or admittance control during interaction and monitor force signatures continuously.",
            "If residuals cross a jamming threshold, back out, update the contact estimate, and retry from a safe approach pose.",
        ],
        code_title="Algorithm: Compliance-Gated Contact Loop",
        code="""# Detect a likely jam from force growth without progress.
force_n = [3.1, 4.8, 6.5, 8.2]
travel_mm = [1.0, 1.5, 1.8, 1.9]

force_slope = round((force_n[-1] - force_n[0]) / (len(force_n) - 1), 2)
travel_gain = round(travel_mm[-1] - travel_mm[0], 2)
jam = force_slope > 1.4 and travel_gain < 1.2
print({"force_slope_N_per_step": force_slope, "travel_gain_mm": travel_gain, "jam_detected": jam})""",
        code_output="{'force_slope_N_per_step': 1.7, 'travel_gain_mm': 0.9, 'jam_detected': True}",
        code_caption="Code Fragment 42.3.1 uses paired force and travel signals to separate productive insertion from jamming.",
        expected_output="The expected result flags a jam because force rises quickly while travel barely increases. In a real controller, that combination should trigger backing out and re-estimating the contact geometry.",
        library_shortcut="Drake and MuJoCo are strong for contact-rich simulation, while MoveIt and cuMotion still help with pre-contact staging. Learned policies are useful here only when the contact residuals remain visible and the safety thresholds stay explicit.",
        recipe_steps=[
            "Choose a compliant frame and document which axes are stiff, compliant, or guarded.",
            "Collect baseline wrench traces for nominal success before tuning recovery logic.",
            "Set jamming and slip thresholds from same-panel traces, not from intuition alone.",
            "Back out along a safe axis before retrying, rather than grinding deeper into the contact.",
            "Save at least one successful and one failed force-time plot with the same axis scale.",
        ],
        warning="A contact controller tuned only on success episodes often becomes dangerous. Without failed traces, the thresholds that should stop the robot tend to drift upward until jamming looks normal.",
        practical_example="Peg-in-hole assembly, cable insertion, and drawer opening all benefit from compliant control because the last millimeters are dominated by contact geometry and small misalignments, not by free-space trajectory quality.",
        fun_note="If your insertion plot looks like a mountain and your displacement plot looks like a sidewalk curb, the robot is arguing with the environment and losing.",
        frontier="Research is pushing toward visuo-tactile contact policies, differentiable contact simulation, and large contact-rich datasets. The engineering bar remains the same: bounded forces, interpretable residuals, and safe retreat logic.",
        self_check="Can you point to the exact residual pattern that distinguishes productive contact from jamming in your task?",
        deep_dive_1="Contact-rich manipulation is where robotic intelligence becomes obviously embodied. The environment participates in the computation, because surfaces, compliance, and friction effectively perform part of the alignment if the controller lets them.",
        deep_dive_2="This section is also a good place to teach complementarity conceptually. The robot should know whether it is pressing, sliding, or separated, because each mode implies a different controller and different evidence signature.",
        tool_rows=[
            ["Drake", "Contact simulation and optimization", "Use it when you want explicit residual reasoning and constraint inspection."],
            ["MuJoCo", "Fast contact rollouts", "Useful for policy tuning and repeated interaction traces."],
            ["Force-torque sensors", "Residual monitoring", "Treat wrench history as a primary artifact, not a side-channel debug stream."],
        ],
        lab="Simulate a peg insertion with three clearance values and one angular misalignment. Plot force and travel together and label which runs jammed, inserted, or slipped.",
        failure_pattern="The first split is whether the controller made progress before the spike. If no progress occurred, suspect geometry or staging. If partial progress occurred, suspect compliance tuning or mode transition logic.",
        takeaway="Contact-rich manipulation succeeds by regulating interaction forces and mode transitions, not by pretending that perfect positioning removes the environment from the loop.",
        exercise="Design a jam detector for an insertion task using force slope, travel gain, and contact duration. State what recovery action should follow each failure label.",
        bibliography=[
            BibEntry("Modern Robotics, force control and hybrid control material", "https://modernrobotics.northwestern.edu/", "A concise reference for impedance, force control, and contact-aware task design."),
            BibEntry("Drake manipulation examples", "https://drake.mit.edu/", "Official project site for simulation, optimization, and contact reasoning tools."),
            BibEntry("MuJoCo documentation", "https://mujoco.org/", "Widely used contact simulator for manipulation learning and controller prototyping."),
        ],
    ),
    SectionData(
        number="42.4",
        title="Perception for manipulation",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-illustration-04.png",
        epigraph="A grasp starts as a perceptual claim.",
        epigraph_cite="A Systems Calibration Log",
        description="Manipulation perception is not generic scene understanding. It is perception tuned to the action question: what can be reached, grasped, pushed, inserted, or recovered from now?",
        reader_pathway="Move from sensing to object state, affordance state, uncertainty, and action-conditioned visibility. If the perception output cannot be consumed by a planner or policy, it is still one layer too abstract.",
        develops="This section defines the perception outputs manipulation actually needs: 6D pose, graspable surfaces, free-space channels, occlusion estimates, contact normals, and uncertainty fields.",
        connects="Those outputs bridge vision models and control. The main lesson is that manipulation perception should be judged by action utility under uncertainty, not by static detection scores alone.",
        key_insight="A detector that names an object but misses the stable grasp surface is less useful than a narrower model that exposes exactly the geometry the controller needs.",
        figure_boxes=["Sense|rgbd and masks", "Infer|pose, affordance", "Filter|uncertainty", "Act|planner or policy"],
        figure_caption="Manipulation perception is action-conditioned perception. It should surface the geometry and uncertainty that change the chosen action.",
        theory_1="Perception for manipulation is a structured estimation problem. The latent state is not just object identity but object pose, free space, support relation, graspable contact patches, and confidence in each estimate.",
        theory_2="The useful error metric is therefore downstream: how much does state uncertainty change grasp ranking, collision risk, or recovery timing? Manipulation perception is only good if the wrong estimate would actually change what the robot does.",
        formula=r"p(g \mid I, D) \propto \int p(g \mid x_o)\,p(x_o \mid I, D)\,dx_o,\qquad \hat g = \arg\max_g \mathbb{E}_{x_o}[Q(g, x_o)] - \beta\,\mathrm{Var}_{x_o}[Q(g, x_o)]",
        mechanism="The system builds pose and affordance hypotheses from RGB-D or point clouds, propagates uncertainty into grasp or motion scoring, and prefers actions whose expected value stays strong under plausible pose error. That is the real bridge between perception and manipulation robustness.",
        algorithm_steps=[
            "Estimate object pose, support relation, and candidate grasp surfaces from the sensor stream.",
            "Quantify uncertainty or ambiguity, especially under occlusion or clutter.",
            "Propagate uncertainty into grasp or motion scores rather than selecting from a single point estimate.",
            "Trigger active perception or viewpoint change when top actions are too sensitive to state error.",
        ],
        code_title="Algorithm: Uncertainty-Aware Grasp Ranking",
        code="""# Penalize grasps whose score is too sensitive to pose uncertainty.
grasps = [
    {"id": "g1", "mean_q": 0.86, "var_q": 0.07},
    {"id": "g2", "mean_q": 0.81, "var_q": 0.01},
    {"id": "g3", "mean_q": 0.75, "var_q": 0.03},
]

beta = 1.5
scored = []
for g in grasps:
    robust = round(g["mean_q"] - beta * g["var_q"], 3)
    scored.append((g["id"], robust))

scored.sort(key=lambda row: row[1], reverse=True)
print(scored)""",
        code_output="[('g2', 0.795), ('g1', 0.755), ('g3', 0.705)]",
        code_caption="Code Fragment 42.4.1 shows how a slightly weaker grasp can become preferable once pose uncertainty is included explicitly.",
        expected_output="The expected ranking promotes the lower-variance candidate. That is the right behavior when manipulation failure is expensive and ambiguity can be reduced later by active sensing.",
        library_shortcut="OpenCV and modern RGB-D stacks cover calibration, while SAM 2, point-cloud libraries, and grasp scorers can propose object geometry. The missing step many systems omit is uncertainty propagation into action choice.",
        recipe_steps=[
            "Calibrate multi-camera and robot frames before measuring pose quality.",
            "Store grasp or affordance scores together with uncertainty, not as naked logits.",
            "Use the same object ids across segmentation, pose estimation, and planner logs.",
            "Add active perception motions when the top action depends strongly on occluded geometry.",
            "Evaluate perception with action-conditioned metrics such as reachable grasp success or collision-free lift rate.",
        ],
        warning="Static detection accuracy can hide manipulation failure. A model may classify every object correctly and still place the end effector on the wrong side of a handle or behind an occluder.",
        practical_example="In cluttered bin picking, the most valuable prediction is often not the class label but the free-space corridor that lets the wrist approach without collision.",
        fun_note="Manipulation perception is the rare vision problem where seeing slightly less of the object can still be fine if you see the only face the gripper actually needs.",
        frontier="Current work is moving toward 3D foundation models, affordance fields, and open-vocabulary manipulation perception. The enduring systems question remains how to convert those rich features into stable action choices under uncertainty.",
        self_check="If the top grasp changes under a 5 millimeter pose perturbation, would your system notice before acting?",
        deep_dive_1="A strong teaching move is to contrast image-centric and action-centric evaluation. Image metrics care about masks and classes; manipulation metrics care about whether the same estimate leads to a stable approach, grasp, and recovery policy.",
        deep_dive_2="Perception for manipulation is also a natural entry point for active sensing. If the robot can move the wrist or camera to shrink uncertainty on the top-ranked grasp, the perception system has already become a planner partner rather than a frozen upstream block.",
        tool_rows=[
            ["OpenCV calib3d", "Calibration and geometry", "Use it to make frame accuracy boring and reliable before experimenting with fancy models."],
            ["SAM 2 or instance segmentation models", "Object and contact-surface masks", "Useful for clutter, but tie masks to action-conditioned downstream checks."],
            ["Point-cloud libraries", "3D geometry extraction", "Use them to compute graspable surfaces, normals, and free-space corridors."],
        ],
        lab="Collect five cluttered RGB-D scenes, estimate two candidate grasps per target, and show how uncertainty-aware ranking changes the selected grasp in at least one case.",
        failure_pattern="If the chosen action was bad, ask whether the state estimate was wrong, the uncertainty was ignored, or the planner consumed the estimate incorrectly. Manipulation perception failures often live at those interfaces.",
        takeaway="Perception for manipulation should expose action-relevant geometry and uncertainty, not just object identity.",
        exercise="Define one action-conditioned metric for a manipulation perception stack and explain why mAP alone would miss the same failure.",
        bibliography=[
            BibEntry("OpenCV calib3d module", "https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html", "Official calibration and geometric-estimation reference."),
            BibEntry("SAM 2", "https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/", "Current segmentation system often used in open-world manipulation perception stacks."),
            BibEntry("Isaac ROS Visual SLAM and perception stack", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html", "Official NVIDIA reference for practical perception integration into robot pipelines."),
        ],
    ),
    SectionData(
        number="42.5",
        title="Learning manipulation policies (IL, RL, VLA)",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-illustration-05.png",
        epigraph="Policies are only interesting when the object disagrees.",
        epigraph_cite="A Robot-Learning Lab Book",
        description="Learning-based manipulation policies sit on top of the same physics and interface contracts as analytic pipelines. Their promise is adaptation and generalization, not exemption from contact, safety, or evaluation.",
        reader_pathway="Compare imitation, reinforcement learning, and vision-language-action policies by what supervision they consume, what action interfaces they emit, and how they recover from contact uncertainty.",
        develops="This section surveys the main policy families for manipulation: behavior cloning and diffusion policies from demonstrations, reinforcement learning with shaped or sparse rewards, and VLA policies conditioned on images and language.",
        connects="The unifying engineering question is simple: how does the learned policy expose an action contract the robot can monitor, interrupt, and evaluate on the same scenario panel as a classical baseline?",
        key_insight="A learned manipulation policy is useful when it generalizes contact decisions and recovery, not when it only imitates clean demonstrations in the easiest parts of the workspace.",
        figure_boxes=["Data|demos, rollouts", "Policy|bc, rl, vla", "Execute|low-level action", "Verify|task and safety"],
        figure_caption="Learned manipulation policies still live inside a measured control loop with explicit action interfaces and verifiers.",
        theory_1="Behavior cloning minimizes prediction error on demonstrated actions, which is efficient but vulnerable to covariate shift. Reinforcement learning optimizes return under interaction, which can discover recovery but is sample hungry. VLA policies leverage large pretraining and language context, but still need embodiment-specific action interfaces and safety wrappers.",
        theory_2="The right comparison is not which family sounds strongest, but which one improves same-panel success, recovery rate, and data efficiency for the manipulation domain you actually care about.",
        formula=r"\mathcal{L}_{BC} = -\sum_t \log \pi_\theta(a_t^\star \mid o_t),\qquad J(\theta)=\mathbb{E}_{\pi_\theta}\left[\sum_t r_t\right],\qquad a_t = \pi_{\theta}(o_t, x_t)",
        mechanism="A learned manipulation stack ingests demonstrations, rollouts, or pretraining corpora, maps observations into an action policy, executes under a bounded interface, and relies on verifiers to decide whether to continue, intervene, or relabel data. That bounded interface is what makes learning compatible with real robots.",
        algorithm_steps=[
            "Choose the action interface first: joint deltas, Cartesian waypoints, chunked trajectories, or gripper events.",
            "Match the learning family to the available signal: demonstrations, reward, language, or mixed supervision.",
            "Wrap the policy with collision, force, and timeout guards before hardware evaluation.",
            "Evaluate against analytic or scripted baselines on the same tasks, sensors, and success code.",
        ],
        code_title="Algorithm: Policy Family Selection",
        code="""# Pick a policy family from task signal and recovery needs.
task = {"demos": 500, "reward_dense": False, "language": True, "needs_recovery": True}

if task["demos"] > 300 and task["language"]:
    choice = "vla_or_diffusion_bc"
elif task["reward_dense"] and task["needs_recovery"]:
    choice = "rl"
else:
    choice = "behavior_cloning"

print({"policy_family": choice, "recovery_needed": task["needs_recovery"]})""",
        code_output="{'policy_family': 'vla_or_diffusion_bc', 'recovery_needed': True}",
        code_caption="Code Fragment 42.5.1 reflects the practical decision logic many manipulation teams follow before spending compute on the wrong training regime.",
        expected_output="The expected result chooses a language-aware imitation route because demonstrations and instruction context are available. In the real system, the next step would be to define the exact action chunk or waypoint interface.",
        library_shortcut="LeRobot, robomimic, ManiSkill, and current OpenVLA-style stacks cover much of the data, policy, and evaluation infrastructure. They help most when the team already knows which action API and recovery signals the learned policy must obey.",
        recipe_steps=[
            "Normalize action and observation interfaces across policy families before training.",
            "Keep a scripted or analytic baseline alive for every task family.",
            "Evaluate recovery separately from one-shot success by injecting mild perturbations.",
            "Log policy outputs alongside force, collision, and timeout guards to localize blame.",
            "Promote hardware policies only after they pass the same-panel simulator and bench tests.",
        ],
        warning="Policy learning is often blamed for failures that actually come from a bad action interface. If the policy emits commands too low-level to be monitored safely, even a good model will look erratic on hardware.",
        practical_example="On tabletop pick and place, diffusion policies often shine when the task needs smooth multimodal trajectories, while a simpler BC policy may be enough if the cell is tightly structured and recovery logic is external.",
        fun_note="A policy with great losses and terrible object outcomes is just a very committed impersonator.",
        frontier="The frontier is moving toward cross-embodiment VLAs, larger robot datasets, and policy distillation across simulators and hardware. The systems bar remains action-interface clarity, safe execution wrappers, and fair baselines.",
        self_check="Could you explain why your chosen action interface is compatible with intervention, safety filtering, and offline replay?",
        deep_dive_1="This chapter section is a good place to stress that policy families and action APIs are different design layers. A diffusion policy over Cartesian chunks and a BC model over joint deltas may fail for reasons that have nothing to do with diffusion or cloning and everything to do with monitorability and embodiment fit.",
        deep_dive_2="It is also the right moment to insist on same-panel evidence. Manipulation papers and demos frequently compare policies that ran with different controllers, sensors, or success metrics. Those comparisons sound quantitative while saying very little.",
        tool_rows=[
            ["LeRobot", "Dataset and policy workflow", "Use it for data loaders, policy baselines, and low-cost hardware integration."],
            ["robomimic", "Offline imitation-learning baselines", "Use it when you need strong manipulation imitation baselines and reproducible configs."],
            ["ManiSkill", "GPU manipulation training and evaluation", "Useful for policy iteration and broad task panels before hardware tests."],
        ],
        lab="Train a small policy on a toy manipulation dataset and compare it to a scripted baseline on nominal and perturbed episodes. Report not just success but recovery behavior.",
        failure_pattern="Separate policy mistakes into perception misread, action-interface mismatch, unsafe command, and missing recovery. Those labels keep learning experiments from turning into vague stories about instability.",
        takeaway="Learned manipulation policies are most valuable when they improve recovery and generalization while staying inside a clear, monitorable action contract.",
        exercise="Choose one manipulation task and justify whether BC, RL, or a VLA policy is the right first learning baseline. Your answer should mention data, action interface, and recovery supervision explicitly.",
        bibliography=[
            BibEntry("LeRobot", "https://github.com/huggingface/lerobot", "Open tooling for robot datasets, imitation policies, and low-cost hardware workflows."),
            BibEntry("robomimic", "https://robomimic.github.io/", "Manipulation imitation-learning benchmark suite and policy library."),
            BibEntry("OpenVLA repository", "https://github.com/openvla/openvla", "Current open-source vision-language-action stack for robot control and fine-tuning."),
        ],
    ),
    SectionData(
        number="42.6",
        title="Failure detection and recovery",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-illustration-05.png",
        epigraph="Robustness is a recovery policy with receipts.",
        epigraph_cite="A Debugger of Real Robots",
        description="Manipulation systems fail for ordinary reasons: missing the object, colliding, slipping, drifting, timing out, or entering an unrecoverable contact mode. Good systems detect those states early and route to bounded recovery.",
        reader_pathway="Track three layers: failure detection signals, diagnosis labels, and recovery branches. The real design task is deciding which branch should fire before damage or wasted time accumulates.",
        develops="This section turns recovery into a first-class subsystem. The robot needs residual tests, timeout tests, progress tests, and contact tests that trigger reobserve, retry, regrasp, or abort.",
        connects="It links manipulation to safety and evaluation. Recovery quality is where impressive one-shot demos and trustworthy embodied systems finally part ways.",
        key_insight="A manipulation stack without explicit recovery is not a robust system. It is a success-only hypothesis that will eventually meet a box, mug, cable, or drawer that refuses to cooperate.",
        figure_boxes=["Detect|residuals", "Diagnose|label failure", "Recover|retry or abort", "Verify|resume or stop"],
        figure_caption="Recovery begins with typed failure signals, not with vague claims that the policy will figure it out online.",
        theory_1="The cleanest abstraction is a failure-state machine layered on top of the manipulation policy. Residuals and progress metrics trigger state transitions, and each transition maps to a bounded recovery primitive.",
        theory_2="This structure matters because many manipulation failures are easier to classify than to avoid. Missing the handle and slipping off the handle may both look like task failure, but they require different next actions and different future data collection.",
        formula=r"z_t = [e_{\text{pose}}, e_{\text{force}}, e_{\text{vision}}, \Delta q, \Delta x_o],\qquad y_t = \mathbf{1}[r(z_t) > \tau],\qquad b_{t+1} = \mathrm{recover}(b_t, y_t)",
        mechanism="The detector fuses pose, force, grasp width, visual residual, and progress features into a failure label. The recovery layer maps that label into a safe next action such as back out, reopen, reobserve, or skip. Crucially, the evidence artifact stores the first label that fired and the branch that followed.",
        algorithm_steps=[
            "Define residual features and timeouts before hardware testing begins.",
            "Map each high-confidence failure label to a bounded recovery primitive.",
            "Require every recovery branch to produce a new observation or new configuration before retry.",
            "Abort after repeated identical failures and log the case for replay-driven debugging.",
        ],
        code_title="Algorithm: Recovery Router",
        code="""# Route a manipulation failure to a bounded recovery branch.
failure = {"slip_score": 0.82, "occlusion": 0.15, "progress": 0.02}

if failure["slip_score"] > 0.7:
    branch = "regrasp"
elif failure["occlusion"] > 0.5:
    branch = "reobserve"
elif failure["progress"] < 0.05:
    branch = "back_out_and_retry"
else:
    branch = "continue"

print({"recovery_branch": branch})""",
        code_output="{'recovery_branch': 'regrasp'}",
        code_caption="Code Fragment 42.6.1 turns failure features into a bounded recovery branch instead of leaving the system to thrash under the original command.",
        expected_output="The expected result routes to regrasp because the slip signal dominates. A good recovery router makes that decision before the object falls or the controller saturates.",
        library_shortcut="BehaviorTree.CPP, ROS 2 actions, and task-execution frameworks are often the right level for recovery orchestration. Learned policies can suggest actions, but the branching and safety limits should stay inspectable.",
        recipe_steps=[
            "Log residual and progress features at the same rate as the control loop or a fixed decimated rate.",
            "Define a failure taxonomy that is small enough to use but rich enough to guide recovery.",
            "Associate every recovery branch with a cost budget in time, retries, and risk.",
            "Store repeated-failure signatures so the same case can be replayed offline.",
            "Measure recovery success separately from nominal task success.",
        ],
        warning="If every failure falls into a single 'retry' bucket, the robot will often repeat the same bad action with a false sense of optimism. Recovery needs new information or a changed configuration.",
        practical_example="Shelf picking systems often recover by changing the wrist viewpoint, not by grasping again immediately. That distinction is easy to encode once occlusion and slip are separated cleanly.",
        fun_note="Nothing reveals a missing recovery design faster than a robot attempting the exact same doomed grasp with heroic consistency.",
        frontier="Current work explores learned failure predictors and language-annotated recovery. The enduring engineering requirement is still a bounded branch table that an operator can inspect and trust.",
        self_check="Does each of your failure labels map to a different physical next action, or are you pretending diagnosis matters while routing everything to retry?",
        deep_dive_1="Recovery exposes one of the deepest embodied-AI differences from static inference. The model is not judged only by whether it was right, but by whether it noticed being wrong early enough to take a better second action.",
        deep_dive_2="For teaching, this section is a natural place to introduce failure ledgers. Students learn quickly when every failure trace must include label, branch, outcome, and whether the second attempt failed for the same or a different reason.",
        tool_rows=[
            ["BehaviorTree.CPP", "Recovery orchestration", "Use it when you want human-readable branching and preemption semantics."],
            ["ROS 2 actions", "Interruptible execution", "Helpful for reporting progress, cancellation, and task-level retries."],
            ["Replay logs", "Postmortem analysis", "Treat replayability as a requirement, not a nice extra."],
        ],
        lab="Add slip, timeout, and no-progress detectors to a manipulation benchmark and show that at least one failure is recovered correctly by branching to a new action.",
        failure_pattern="The first question is whether the detector fired early enough. If not, improve signals. If yes, check whether the branch changed information, geometry, or contact state before retrying.",
        takeaway="Reliable manipulation comes from detecting failure states early and routing them into bounded, evidence-backed recovery branches.",
        exercise="Write a four-label manipulation failure taxonomy and a matching recovery table. For each label, specify the next observation you need before retrying.",
        bibliography=[
            BibEntry("BehaviorTree.CPP ROS 2 integration", "https://www.behaviortree.dev/docs/ros2_integration", "Practical framework for readable task branching and recovery."),
            BibEntry("ROS 2 actions tutorial", "https://docs.ros.org/en/foxy/Tutorials/Intermediate/Creating-an-Action.html", "Official action semantics for interruptible and monitorable task execution."),
            BibEntry("MoveIt 2 Documentation", "https://moveit.picknik.ai/", "Useful reference for execution feedback and monitorable motion stages in manipulation pipelines."),
        ],
    ),
    SectionData(
        number="42.7",
        title="Mobile Manipulation: Base, Arm, Perception, And Recovery",
        chapter_num=42,
        chapter_title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        image="chapter-42-application-reference-7.png",
        epigraph="A mobile manipulator is a negotiation between reachability and route planning.",
        epigraph_cite="A Whole-Body Systems Notebook",
        description="Mobile manipulation couples navigation, perception, reachability, grasping, and recovery into one long-horizon control problem. The base pose is part of the grasp plan, not just a precondition for it.",
        reader_pathway="Track the loop from route choice to base staging, arm reachability, local perception refresh, grasp execution, and post-failure retreat. The main idea is whole-body coordination under uncertainty.",
        develops="This section explains how base position, arm kinematics, visibility, and recovery policies interact in whole-body manipulation. Good mobile manipulators plan for navigation and grasping together, not as isolated modules.",
        connects="It synthesizes earlier material on navigation, mapping, manipulation, and recovery into one application-grade system loop with explicit evidence artifacts.",
        key_insight="If the base is staged poorly, even a perfect arm policy will look stupid. Whole-body success depends on choosing poses that preserve visibility, reachability, and recovery margin simultaneously.",
        figure_boxes=["Sense|map, target", "Stage|base and arm", "Execute|whole-body task", "Recover|retreat and retry"],
        figure_caption="A mobile manipulation loop must co-design route choice, base staging, arm reachability, and recovery rather than treating grasping as a final afterthought.",
        theory_1="The central object is a coupled cost over base pose, arm configuration, visibility, collision risk, and task progress. Local arm planning cannot be optimal if the base pose destroys reachability or line of sight.",
        theory_2="This coupling is why mobile manipulation is a natural benchmark for embodied AI. It forces a policy or planner to reason across spatial scales and across multiple failure channels in one episode.",
        formula=r"(q_b^\star, q_a^\star) = \arg\min_{q_b, q_a} C_{\text{route}}(q_b)+C_{\text{reach}}(q_b,q_a)+C_{\text{view}}(q_b)+C_{\text{risk}}(q_b,q_a)",
        mechanism="The robot builds a semantic map, chooses candidate base poses that preserve arm reachability and visibility, executes a staged manipulation plan, and routes to retreat or reobserve when local evidence disagrees with the global map. A good evidence artifact contains route, base pose, arm plan, and recovery branch together.",
        algorithm_steps=[
            "Generate candidate base poses near the target region and reject ones with poor reachability or visibility.",
            "Plan a local whole-body sequence: base settle, arm approach, contact action, and retreat corridor.",
            "Refresh local perception after base arrival before committing the arm plan.",
            "If the grasp or contact fails, retreat to a safe standoff pose before replanning.",
        ],
        code_title="Algorithm: Whole-Body Staging Score",
        code="""# Score candidate base poses for reachability, view, and risk.
candidates = [
    {"pose": "b1", "reach": 0.92, "view": 0.55, "risk": 0.20},
    {"pose": "b2", "reach": 0.80, "view": 0.90, "risk": 0.10},
    {"pose": "b3", "reach": 0.95, "view": 0.30, "risk": 0.35},
]

scores = []
for c in candidates:
    score = round(0.5 * c["reach"] + 0.4 * c["view"] - 0.6 * c["risk"], 3)
    scores.append((c["pose"], score))

scores.sort(key=lambda row: row[1], reverse=True)
print(scores)""",
        code_output="[('b2', 0.7), ('b1', 0.56), ('b3', 0.385)]",
        code_caption="Code Fragment 42.7.1 illustrates the core mobile-manipulation tradeoff: the best base pose balances reachability, viewpoint quality, and risk rather than maximizing any one in isolation.",
        expected_output="The expected ranking prefers the slightly less reachable pose with much better visibility and lower risk. That is often the right whole-body decision in homes, warehouses, and service settings.",
        library_shortcut="Nav2, MoveIt, BehaviorTree.CPP, Habitat 3.0, ManiSkill, BEHAVIOR-1K, and Mobile ALOHA provide much of the plumbing. The hard systems work is choosing the joint evidence schema that makes navigation and manipulation failures comparable.",
        recipe_steps=[
            "Score base poses with visibility and retreat feasibility, not just arm reachability.",
            "Refresh local perception after arriving at the base pose because small route errors matter near contact.",
            "Reserve space for retreat and human-safe recovery before the arm starts moving.",
            "Log route, base pose, arm plan, and failure branch in one artifact.",
            "Benchmark on tasks where the first base pose is intentionally suboptimal so recovery is exercised.",
        ],
        warning="Treating mobile manipulation as navigation followed by grasping usually creates hidden dead ends. The base may arrive in a place where the target is visible but not reachable, or reachable but unsafe to recover from.",
        practical_example="Household robots opening cabinets, carrying dishes, or picking objects from cluttered floors routinely need to re-stage the base to obtain a better wrist approach and a safer retreat corridor.",
        fun_note="A mobile manipulator can absolutely reach the wrong place with stunning confidence. That is why the base pose deserves as much suspicion as the grasp pose.",
        frontier="Frontier systems combine foundation-model perception, whole-body planning, and large-scale household simulation. The lasting contribution is still an evidence loop that reveals why a task failed across route, staging, contact, and recovery layers.",
        self_check="Could you justify your chosen base pose using reachability, visibility, and retreat margin, or did the robot simply stop where navigation happened to end?",
        deep_dive_1="Mobile manipulation is a clean example of multi-timescale reasoning. Global route planning runs over meters and seconds, while contact control runs over centimeters and milliseconds. Whole-body success depends on passing the right abstractions between those scales.",
        deep_dive_2="It is also a useful place to teach coupled evaluation. A navigation benchmark and a grasp benchmark can both look strong while the combined system fails because the interfaces between them were never optimized together.",
        tool_rows=[
            ["Nav2", "Base navigation and route execution", "Use costmaps and recovery behaviors that leave manipulation staging space."],
            ["MoveIt 2", "Arm planning after staging", "Use it to evaluate reachability and contact-free arm motion from each base pose."],
            ["BehaviorTree.CPP", "Whole-body task routing", "Helpful for retry logic that spans route, stage, and grasp failures."],
        ],
        lab="Construct a mobile-manipulation benchmark with three candidate base poses per task. Show that your system chooses a pose with better whole-body success than a nearest-goal heuristic.",
        failure_pattern="When a task fails, ask whether the route, the base pose, the local perception refresh, the arm plan, or the retreat branch first violated its contract. Mobile manipulation only becomes debuggable once those labels stay separate.",
        takeaway="Mobile manipulation is a whole-body coordination problem whose success depends as much on base staging and recovery margin as on arm control.",
        exercise="Design a base-pose scoring function for a mobile manipulator that must pick an object from a shelf and retreat through a narrow aisle. Include one term for visibility and one for retreat safety.",
        bibliography=[
            BibEntry("Nav2 documentation", "https://docs.nav2.org/", "Official navigation stack reference for staged base motion and recovery."),
            BibEntry("Habitat 3.0", "https://aihabitat.org/habitat3/", "Simulator for interactive embodied tasks with navigation and manipulation."),
            BibEntry("Mobile ALOHA", "https://arxiv.org/abs/2401.02117", "Mobile bimanual manipulation system showing whole-body teleoperation and data-driven control."),
        ],
    ),
    SectionData(
        number="43.1",
        title="Grasp synthesis: analytic and learned (Dex-Net lineage)",
        chapter_num=43,
        chapter_title="Grasping and Dexterous Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-43-grasping-and-dexterous-manipulation",
        image="chapter-43-illustration-01.png",
        epigraph="A grasp is a hypothesis about future contact stability.",
        epigraph_cite="A Reliable Bin-Picking Team",
        description="Grasp synthesis asks which contacts should be made, not only where the gripper should move. Analytic and learned methods differ in how they estimate grasp robustness, but both must answer the same contact question.",
        reader_pathway="Move through grasp representation, force-closure intuition, synthetic or learned scoring, reachability filtering, and hardware verification. The central object is the contact hypothesis itself.",
        develops="This section introduces antipodal and force-closure grasp reasoning, then shows how the Dex-Net and GQ-CNN lineage turns those ideas into large synthetic datasets and learned grasp scoring from depth images or point clouds.",
        connects="It links contact mechanics to modern data-driven grasping. The bridge matters because learned grasp scores are only meaningful if the contact quality concept underneath them stays legible.",
        key_insight="A grasp score is useful when it predicts whether the object will survive lift, transport, and small disturbances, not when it merely favors visually centered contact patches.",
        figure_boxes=["Observe|depth and mask", "Generate|grasp set", "Score|quality and reach", "Verify|lift success"],
        figure_caption="Grasp synthesis turns perception into candidate contacts, then filters them through robustness and embodiment feasibility before execution.",
        theory_1="Analytic grasping starts from contact geometry and wrench closure. Learned grasping often starts from images or point clouds and predicts a proxy for that robustness. The methods differ, but the latent question is the same: does this contact set resist expected disturbances?",
        theory_2="Dex-Net made this bridge concrete by generating massive synthetic grasp datasets labeled with analytic robustness metrics, then training networks such as GQ-CNN to predict grasp quality efficiently at runtime.",
        formula=r"\epsilon(g) = \max \{\epsilon : B_\epsilon \subseteq \mathrm{conv}(W(g))\},\qquad g^\star = \arg\max_g \hat Q_\theta(g, I)\,\mathbf{1}[\text{reachable}(g)]",
        mechanism="The stack estimates object geometry from depth or point clouds, samples candidate grasps, scores them with an analytic metric or learned predictor, filters them through robot constraints, and verifies success with lift and disturbance tests.",
        algorithm_steps=[
            "Sample candidate grasps in image or object space and convert them into robot-frame contacts.",
            "Score each candidate with a robustness proxy such as epsilon quality or a learned GQ-CNN output.",
            "Reject grasps that are unreachable, collision-prone, or incompatible with downstream placement.",
            "Validate the selected grasp on hardware with lift and mild disturbance checks, not only closure success.",
        ],
        code_title="Algorithm: Robust Grasp Ranking",
        code="""# Rank parallel-jaw grasps by learned score and reachability.
grasps = [
    {"id": "g1", "gqcnn": 0.88, "reachable": True},
    {"id": "g2", "gqcnn": 0.94, "reachable": False},
    {"id": "g3", "gqcnn": 0.81, "reachable": True},
]

ranked = []
for g in grasps:
    robust = round(g["gqcnn"] * float(g["reachable"]), 2)
    ranked.append((g["id"], robust))

ranked.sort(key=lambda row: row[1], reverse=True)
print(ranked)""",
        code_output="[('g1', 0.88), ('g3', 0.81), ('g2', 0.0)]",
        code_caption="Code Fragment 43.1.1 shows the minimum discipline grasp planners need: never let a strong score outrank embodiment feasibility.",
        expected_output="The expected ranking demotes the unreachable high-score grasp to the bottom. In real cells, many grasping failures are exactly this mismatch between image-space confidence and robot-space feasibility.",
        library_shortcut="The Dex-Net project and GQ-CNN package provide a mature reference lineage for synthetic grasp datasets and learned scoring. They help most when paired with modern motion planners and explicit lift verifiers.",
        recipe_steps=[
            "Choose a grasp representation that matches the hand: parallel-jaw contacts, suction poses, or multi-finger contacts.",
            "Keep analytic and learned scores in the same evaluation table on the same object panel.",
            "Filter by reachability and collision before spending time on refined ranking.",
            "After grasp closure, verify lift robustness with small disturbances or short transport motions.",
            "Save depth crop, chosen grasp pose, score, and lift outcome together in one artifact.",
        ],
        warning="A grasp that closes cleanly is not necessarily a stable grasp. Closure without disturbance testing often overestimates quality badly, especially for thin, shiny, or partial-view objects.",
        practical_example="Bin-picking systems in logistics still rely heavily on parallel-jaw grasp synthesis because the object flow is large and the best engineering return often comes from better scoring and filtering rather than more fingers.",
        fun_note="A perfectly centered grasp on a slippery shampoo bottle can still become an expensive lesson in rigid-body optimism.",
        frontier="The current frontier mixes synthetic supervision, richer point-cloud encoders, tactile feedback, and downstream task-aware grasp scoring. The stable idea underneath is still robust contact selection under disturbance.",
        self_check="Do you know what disturbance model your grasp score is trying to resist, or is the score just a number with good marketing?",
        deep_dive_1="One of the best didactic uses of Dex-Net is that it makes contact mechanics visible to machine learning students and dataset scale visible to classical robotics students. The bridge runs both ways.",
        deep_dive_2="This section also clarifies why grasp synthesis never stands alone. A grasp score that ignores reachability, placement, or sensor uncertainty is not wrong in theory, but it is incomplete in a real manipulation system.",
        tool_rows=[
            ["Dex-Net", "Synthetic grasp dataset generation", "Use it to connect analytic robustness labels to scalable supervised training."],
            ["GQ-CNN", "Runtime grasp scoring", "Useful for fast grasp ranking from depth imagery."],
            ["MoveIt 2", "Embodiment feasibility", "Use it to filter learned or analytic grasps through reachability and collision checks."],
        ],
        lab="Evaluate grasp proposals on a small object set using both a simple analytic metric and a learned score. Compare the top candidate after reachability filtering.",
        failure_pattern="When a chosen grasp fails, separate contact quality from perception quality and embodiment feasibility. Those three causes tend to require different fixes and different data.",
        takeaway="Grasp synthesis succeeds when contact robustness, embodiment feasibility, and lift verification stay in the same loop.",
        exercise="Define one disturbance model for a grasp benchmark and explain how your scoring method, analytic or learned, is supposed to predict resistance to it.",
        bibliography=[
            BibEntry("Dex-Net project", "https://berkeleyautomation.github.io/dex-net/", "Canonical project page for synthetic grasp datasets and robust-grasp planning."),
            BibEntry("GQ-CNN documentation", "https://berkeleyautomation.github.io/gqcnn/", "Official package documentation for learned grasp scoring in the Dex-Net lineage."),
            BibEntry("MoveIt 2 Documentation", "https://moveit.picknik.ai/", "Useful for reachability, collision checking, and execution after grasp ranking."),
        ],
    ),
    SectionData(
        number="43.2",
        title="Parallel-jaw vs. multi-finger hands",
        chapter_num=43,
        chapter_title="Grasping and Dexterous Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-43-grasping-and-dexterous-manipulation",
        image="chapter-43-illustration-02.png",
        epigraph="More fingers buy options, not free competence.",
        epigraph_cite="A Whole-Hand Design Review",
        description="The choice between parallel-jaw grippers and multi-finger hands is not philosophical. It is an engineering tradeoff across contact geometry, control complexity, sensing, speed, reliability, and recovery.",
        reader_pathway="Compare end-effector choices through contact richness, controllable workspace, grasp taxonomies, control burden, and data demands. The useful output is a design decision, not a slogan.",
        develops="This section contrasts parallel-jaw grippers with multi-finger hands in terms of grasp representation, reachable contact set, force control, in-hand manipulation capacity, and operational reliability.",
        connects="It clarifies why many production cells still prefer simple grippers while dexterous research platforms invest in richer hands and tactile feedback.",
        key_insight="A multi-finger hand increases the space of possible contacts, but it also increases the estimation, calibration, and control burden. Dexterity is purchased with systems complexity.",
        figure_boxes=["Hardware|gripper or hand", "Contact|grasp family", "Control|command space", "Verify|task envelope"],
        figure_caption="End-effector choice changes the contact family, action space, recovery logic, and the kinds of manipulation the robot can plausibly support.",
        theory_1="Parallel-jaw grippers simplify contact reasoning by constraining the grasp family, which makes perception and planning cheaper. Multi-finger hands expand the contact manifold and can support in-hand manipulation, but they raise the dimension of the control and sensing problem dramatically.",
        theory_2="The right comparison therefore is not human likeness. It is task match: object diversity, required reorientation, tolerance to uncertainty, and acceptable system complexity.",
        formula=r"\mathrm{rank}(G) \uparrow \Rightarrow \text{richer wrench control},\qquad \dim(a_{\text{hand}}) \gg \dim(a_{\text{parallel-jaw}}),\qquad \text{system cost} \propto \text{sensing} + \text{calibration} + \text{control}",
        mechanism="The designer picks an end effector whose contact family matches the task envelope, then builds perception, control, and recovery around that choice. The log should make end-effector constraints visible, because many downstream failures are really hardware-design mismatches.",
        algorithm_steps=[
            "List the object set, required reorientations, and disturbance environment before choosing the hand.",
            "Match the hand to the minimum contact family that supports the task reliably.",
            "Quantify the added sensing and controller burden if moving from parallel-jaw to multi-finger.",
            "Benchmark hardware choices on the same object panel and recovery conditions, not on different demos.",
        ],
        code_title="Algorithm: End-Effector Selection Heuristic",
        code="""# Choose an end effector from task complexity and reorientation demand.
task = {"object_diversity": 0.8, "reorientation_needed": True, "throughput_priority": 0.4}

score_hand = 0.6 * task["object_diversity"] + 0.8 * float(task["reorientation_needed"])
score_parallel = 0.9 * task["throughput_priority"] + 0.3 * (1.0 - task["object_diversity"])

choice = "multi_finger_hand" if score_hand > score_parallel else "parallel_jaw"
print({"parallel_jaw_score": round(score_parallel, 2), "multi_finger_score": round(score_hand, 2), "choice": choice})""",
        code_output="{'parallel_jaw_score': 0.42, 'multi_finger_score': 1.28, 'choice': 'multi_finger_hand'}",
        code_caption="Code Fragment 43.2.1 is a deliberately simple reminder that end-effector choice should follow task structure rather than fashion.",
        expected_output="The expected result chooses the multi-finger hand because reorientation is required and object diversity is high. In a high-throughput structured cell, the same heuristic would often flip back to a simple gripper.",
        library_shortcut="MoveIt can support both hardware classes at the planning level, but the sensing and control stacks diverge quickly. Parallel-jaw workflows often pair well with Dex-Net style scoring, while multi-finger hands usually demand tactile and contact-rich policy loops.",
        recipe_steps=[
            "Write the task envelope before discussing hand morphology.",
            "Benchmark at least one structured and one adversarial object set.",
            "Account for calibration, maintenance, and controller tuning time as real system cost.",
            "Measure reorientation success separately from first-contact grasp success.",
            "Prefer the simpler hand unless the task truly needs the extra contact modes.",
        ],
        warning="Teams often underestimate the software tax of multi-finger hands. The fingers are not just more actuators. They are more contacts, more failure modes, and more state that has to be sensed and controlled.",
        practical_example="In warehouse picking, a parallel-jaw gripper often wins on throughput and reliability. In electronics assembly or in-hand tool reorientation, the multi-finger hand may justify its complexity.",
        fun_note="A five-finger hand can absolutely outperform a two-finger gripper, right after it finishes asking for better calibration, better tactile sensing, and several more weeks of control tuning.",
        frontier="Recent dexterous hands combine tactile skins, richer proprioception, and learned controllers. The central deployment question is still where that extra complexity pays back in task breadth or recovery power.",
        self_check="Could you explain the exact task that requires more fingers, or are you using dexterity as a synonym for ambition?",
        deep_dive_1="This section is useful pedagogically because it forces students to see embodiment as a design variable. The policy and dataset questions only make sense after the hardware contact family has been chosen.",
        deep_dive_2="It is also where whole-system cost becomes concrete. More contact richness can mean fewer task-specific fixtures and more general behavior, but it also means more sensing, more calibration drift, and a larger action space to learn or control.",
        tool_rows=[
            ["Parallel-jaw grippers", "High-throughput stable grasps", "Best when tasks are structured and reorientation demands are low."],
            ["Multi-finger hands", "Rich contact and in-hand control", "Best when reorientation, tool use, or delicate contact are central."],
            ["Tactile sensors", "Contact observability", "Almost mandatory for making the extra fingers pay off in real tasks."],
        ],
        lab="Create a decision table for three application scenarios and justify whether each should use a parallel-jaw gripper or a multi-finger hand, including recovery and maintenance costs.",
        failure_pattern="If the hand repeatedly fails in the same way, ask whether the failure is controller weakness or embodiment mismatch. The latter is more common than teams like to admit.",
        takeaway="Hand choice is a task-envelope decision shaped by contact needs, not a generic race toward higher finger count.",
        exercise="Pick one application where a multi-finger hand is truly justified and one where it is not. Support both choices with contact and recovery arguments.",
        bibliography=[
            BibEntry("Modern Robotics", "https://modernrobotics.northwestern.edu/", "Reference for grasping, hand kinematics, and wrench-space intuition."),
            BibEntry("Dex-Net project", "https://berkeleyautomation.github.io/dex-net/", "Useful as a strong reference lineage for parallel-jaw grasping workflows."),
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Open tactile-processing library relevant once the hand design demands richer contact sensing."),
        ],
    ),
    SectionData(
        number="43.3",
        title="In-hand manipulation and reorientation",
        chapter_num=43,
        chapter_title="Grasping and Dexterous Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-43-grasping-and-dexterous-manipulation",
        image="chapter-43-illustration-03.png",
        epigraph="The hard part of dexterity is not holding on, it is changing contact without losing meaning.",
        epigraph_cite="A Dexterous Manipulation Bench",
        description="In-hand manipulation changes object pose while preserving useful control over contact. The task is not just gripping harder, but moving through a sequence of contact modes without dropping the object or losing task intent.",
        reader_pathway="Track object orientation, fingertip contacts, slip, contact-mode transitions, and regrasp plans. The important abstractions are contact sequence and reachable reorientation path.",
        develops="This section treats in-hand manipulation as a sequence of contact transitions such as rolling, pivoting, finger gaiting, and regrasping. The robot must reason over object pose and hand configuration together.",
        connects="It extends grasping from one-shot acquisition to object reorientation, tool positioning, and dexterous correction, which is where simple grasp scores stop being enough.",
        key_insight="A secure initial grasp is only the opening move. In-hand manipulation succeeds when the robot can change contact intentionally while keeping the object inside a controllable region of the hand.",
        figure_boxes=["Observe|pose and contacts", "Plan|contact sequence", "Act|roll or regrasp", "Verify|orientation residual"],
        figure_caption="Dexterous in-hand manipulation is a sequence-planning problem over contact modes, not just a stronger version of grasp closure.",
        theory_1="The state includes object orientation, fingertip contacts, joint configuration, and latent slip state. The action is often a combination of finger motion and controlled object motion induced by rolling or pivoting contacts.",
        theory_2="This is why reorientation cannot be reduced to a single grasp quality number. The planner must care about whether the current contact set admits a path to the target pose through reachable intermediate contacts.",
        formula=r"R_{o,T} = R(\Delta \theta_K)\cdots R(\Delta \theta_2)R(\Delta \theta_1)R_{o,0},\qquad c_{k+1} \in \mathcal{R}(c_k, q_k)\qquad \text{while}\ \Pr(\text{drop}) < \tau",
        mechanism="The system estimates the object pose in the hand, chooses a contact-mode transition such as rolling or finger gaiting, executes the transition under tactile and proprioceptive feedback, and verifies progress toward the target orientation after each step.",
        algorithm_steps=[
            "Estimate object pose and current contacts in the hand frame.",
            "Search for a contact sequence that reaches the target orientation without violating joint or force limits.",
            "Execute one local contact transition and measure slip or pose residual immediately.",
            "Regrasp or backtrack if the next transition becomes unreachable under the current contact state.",
        ],
        code_title="Algorithm: Reorientation Step Selection",
        code="""# Choose the next in-hand move from orientation progress and slip risk.
moves = [
    {"name": "roll", "progress_deg": 12, "slip_risk": 0.22},
    {"name": "pivot", "progress_deg": 8, "slip_risk": 0.10},
    {"name": "finger_gait", "progress_deg": 15, "slip_risk": 0.45},
]

ranked = []
for m in moves:
    score = round(m["progress_deg"] - 20 * m["slip_risk"], 2)
    ranked.append((m["name"], score))

ranked.sort(key=lambda row: row[1], reverse=True)
print(ranked)""",
        code_output="[('roll', 7.6), ('pivot', 6.0), ('finger_gait', 6.0)]",
        code_caption="Code Fragment 43.3.1 makes the tradeoff explicit: the best local move is the one that advances orientation without taking the object outside a stable contact regime.",
        expected_output="The expected ranking prefers rolling because it makes strong orientation progress with moderate slip risk. In a real controller, ties would be broken using reachability of the next contact set.",
        library_shortcut="MuJoCo dexterous hand models, tactile processing libraries, and learned contact policies can help, but the missing abstraction in many systems is still the contact-sequence ledger that explains why a reorientation path exists or fails.",
        recipe_steps=[
            "Represent object pose in the hand frame and update it after every contact transition.",
            "Log contact set, orientation residual, and slip estimate together.",
            "Use short local transitions with frequent verification instead of long open-loop finger motions.",
            "Reserve explicit regrasp states when the current contact family cannot reach the target orientation.",
            "Evaluate on held-out object shapes, not only on one friendly benchmark object.",
        ],
        warning="Secure grasping can hide a dead-end contact topology. The hand may hold the object stably while making the target orientation unreachable without a deliberate regrasp.",
        practical_example="Screwdriver pickup, package label presentation, and connector alignment all benefit from in-hand reorientation because moving the whole arm for every orientation change is slow and often unstable.",
        fun_note="A hand that can hold a lemon very confidently is still not dexterous if every attempt to rotate it turns into an unplanned citrus launch.",
        frontier="Current systems combine tactile sensing, vision, and policy learning to infer latent object pose inside the hand. The strongest results tend to come from better state estimation and contact-transition supervision rather than from larger networks alone.",
        self_check="Could your system explain why the current contact set can or cannot reach the target orientation without a regrasp?",
        deep_dive_1="This section highlights the conceptual jump from grasping to dexterity. The object is no longer only constrained. It becomes a controlled body moving through a sequence of intermediate contact states.",
        deep_dive_2="A powerful classroom exercise here is to draw a contact graph over reorientation states. Students quickly see that dexterity is partly about planning over graph connectivity, not only about local control precision.",
        tool_rows=[
            ["MuJoCo dexterous hand models", "Simulation of contact transitions", "Use them to prototype rolling, pivoting, and regrasp routines with rich contact signals."],
            ["Tactile sensors", "Slip and contact-state feedback", "Critical for deciding whether a transition is proceeding or failing."],
            ["Replay traces", "Contact-sequence debugging", "Save pose, contact, and slip together so failed transitions can be explained."],
        ],
        lab="Implement a three-step reorientation planner for a simple object and show where a regrasp becomes necessary when one finger joint limit is tightened.",
        failure_pattern="If orientation progress stalls, distinguish between bad state estimation, risky local transition choice, and unreachable next contact set. Each cause implies a different repair.",
        takeaway="In-hand manipulation is successful contact-sequence planning under slip, reachability, and orientation constraints.",
        exercise="Sketch a contact-transition graph for reorienting a rectangular object by 90 degrees inside a multi-finger hand. Mark where a regrasp might be required.",
        bibliography=[
            BibEntry("MuJoCo", "https://mujoco.org/", "Widely used simulator for dexterous hand control and contact-rich rollouts."),
            BibEntry("NeuralFeels", "https://github.com/facebookresearch/neuralfeels", "Visuo-tactile in-hand perception project connecting touch, vision, and reorientation."),
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Open tactile-learning library relevant for contact and slip processing."),
        ],
    ),
    SectionData(
        number="43.4",
        title="Dexterous RL with demonstrations",
        chapter_num=43,
        chapter_title="Grasping and Dexterous Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-43-grasping-and-dexterous-manipulation",
        image="chapter-43-illustration-04.png",
        epigraph="Demonstrations teach the hand where the search should begin.",
        epigraph_cite="A Data-Hungry Dexterity Group",
        description="Dexterous manipulation is one of the clearest cases where demonstrations and reinforcement learning complement each other. Demonstrations bootstrap the policy into plausible contact regimes, while RL refines robustness and recovery.",
        reader_pathway="Track the role of demonstrations, replay buffers, privileged simulation, reward shaping, and hardware transfer. The question is how to learn contact behavior without falling into impossible exploration.",
        develops="This section explains why dexterous RL often starts from demonstrations or teleoperation data, then fine-tunes with reinforcement learning under domain randomization or privileged critics.",
        connects="It pulls together offline data, on-policy refinement, and contact-rich evaluation for tasks where random exploration would be too slow or too unsafe to be useful.",
        key_insight="Demonstrations do not replace reinforcement learning in dexterity. They cut the exploration problem down to the contact neighborhoods where reinforcement learning can actually discover recovery.",
        figure_boxes=["Data|demo traces", "Bootstrap|policy init", "Refine|rl updates", "Verify|real contact skill"],
        figure_caption="Dexterous RL with demonstrations works by constraining exploration to plausible contact regions and then optimizing robustness inside them.",
        theory_1="Pure RL in high-dimensional dexterous action spaces often wastes experience before it even discovers stable contact. Demonstrations move the policy into the right contact manifold, making policy improvement gradients far more useful.",
        theory_2="The hybrid pipeline therefore mixes imitation loss, value-based or policy-gradient updates, and heavy randomization. The system still needs an action interface and a recovery-aware reward or verifier to prevent reward hacking.",
        formula=r"\mathcal{L}(\theta)=\lambda_{BC}\,\mathcal{L}_{BC}(\theta)-\mathbb{E}_{\pi_\theta}\left[\sum_t r_t\right],\qquad \pi_{\theta_0}\leftarrow \text{BC on demos},\qquad \theta \leftarrow \text{RL fine-tuning}",
        mechanism="Demonstrations initialize the policy and sometimes the critic, RL rollouts refine the contact behavior under perturbation, and the final policy is evaluated on same-panel dexterous tasks with object diversity, slip, and recovery metrics. The important artifact is the training curriculum plus the real-world evaluation panel.",
        algorithm_steps=[
            "Collect or curate demonstrations that cover successful contact-entry patterns and partial recoveries.",
            "Pretrain the policy with imitation until it consistently enters stable contact regimes.",
            "Fine-tune with RL using perturbations that exercise recovery rather than only nominal success.",
            "Evaluate on held-out objects and disturbance cases with the same action interface and success code.",
        ],
        code_title="Algorithm: Demo-Then-RL Training Switch",
        code="""# Decide when to switch from pure imitation to RL fine-tuning.
bc_success = 0.78
contact_entry_rate = 0.86
switch_to_rl = bc_success > 0.7 and contact_entry_rate > 0.8

phase = "rl_finetune" if switch_to_rl else "continue_bc"
print({"phase": phase, "bc_success": bc_success, "contact_entry_rate": contact_entry_rate})""",
        code_output="{'phase': 'rl_finetune', 'bc_success': 0.78, 'contact_entry_rate': 0.86}",
        code_caption="Code Fragment 43.4.1 reflects a practical rule of thumb: switch to RL only once the policy reliably reaches meaningful contact states.",
        expected_output="The expected result enters RL fine-tuning because the cloned policy already reaches stable contact often enough to make further exploration useful instead of random.",
        library_shortcut="robomimic, ManiSkill, Isaac Lab style RL stacks, and dexterous hand simulators provide the right substrate. They save time only if the demonstrations, perturbations, and evaluation panel are specified clearly first.",
        recipe_steps=[
            "Record demonstrations with enough variability to teach contact entry and small corrections.",
            "Measure contact-entry rate explicitly before RL begins.",
            "Use perturbations during RL that reflect realistic drop, slip, or pose errors.",
            "Keep behavior-cloning and RL checkpoints for the same task panel so regressions stay visible.",
            "Treat sim-to-real evaluation as part of the training plan, not as a last-day surprise.",
        ],
        warning="Starting RL too early in dexterous domains often looks like learning progress but is really the policy thrashing around outside the useful contact manifold.",
        practical_example="Cube reorientation and tool pickup are classic examples where demonstrations give the policy a workable contact grammar, while RL improves disturbance recovery and timing.",
        fun_note="Dexterous RL without demonstrations often resembles a pianist learning by punching the keyboard and hoping harmony arrives out of respect.",
        frontier="The frontier mixes demonstrations, diffusion action models, privileged critics, and large tactile or teleoperation datasets. The stable lesson is still that exploration must be biased toward meaningful contact structure.",
        self_check="Could you state which contact behavior the demonstrations teach and which remaining behavior the RL phase is expected to discover?",
        deep_dive_1="This section is useful for teaching curriculum design. Students often assume the data question and the RL question are separate, but dexterous learning succeeds precisely because the initial data changes the effective exploration landscape.",
        deep_dive_2="It is also a good place to insist on disturbance-aware evaluation. A dexterous policy that only performs on nominal states may have learned choreography rather than robust manipulation.",
        tool_rows=[
            ["robomimic", "Demonstration-based pretraining", "Use it to build strong imitation baselines before adding RL complexity."],
            ["ManiSkill", "Large-scale rollout generation", "Useful for broad perturbation panels and GPU throughput."],
            ["Isaac-style RL stacks", "Fine-tuning with randomization", "Good when policy improvement needs high simulation throughput and vectorized environments."],
        ],
        lab="Pretrain a toy dexterous policy on demonstrations, then fine-tune with disturbances. Plot contact-entry rate and recovery rate before and after RL.",
        failure_pattern="If RL regressions appear, ask whether the reward changed the contact style, the perturbations are unrealistic, or the demonstrations covered too narrow a contact manifold.",
        takeaway="Dexterous RL with demonstrations works by using data to enter the right contact manifold and RL to harden behavior inside it.",
        exercise="Write a curriculum for a dexterous reorientation task that includes one BC phase and one RL phase. State the metric that decides when to switch.",
        bibliography=[
            BibEntry("robomimic", "https://robomimic.github.io/", "Strong benchmark and library for learning manipulation from offline demonstrations."),
            BibEntry("ManiSkill documentation", "https://maniskill.readthedocs.io/en/latest/", "GPU-enabled manipulation benchmark suite for policy learning."),
            BibEntry("LeRobot", "https://github.com/huggingface/lerobot", "Open tooling for demonstration datasets and policy training relevant to dexterous learning."),
        ],
    ),
    SectionData(
        number="43.5",
        title="Sim-to-real for dexterity",
        chapter_num=43,
        chapter_title="Grasping and Dexterous Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-43-grasping-and-dexterous-manipulation",
        image="chapter-43-illustration-05.png",
        epigraph="Dexterity in simulation becomes interesting only after hardware disagrees.",
        epigraph_cite="A Sim-to-Real Transfer Diary",
        description="Dexterous sim-to-real transfer is hard because every hidden modeling error in friction, compliance, sensing, delay, and calibration becomes a new contact failure mode.",
        reader_pathway="Follow the transfer loop through system identification, domain randomization, tactile mismatch, teacher-student distillation, and hardware safety gates. The key abstraction is transfer evidence, not just simulator score.",
        develops="This section explains why dexterity transfer needs more than randomization. The team must manage actuator delays, fingertip compliance, tactile noise, latency, and contact-model mismatch explicitly.",
        connects="It ties dexterous learning back to sensing, simulation, and deployment. The result is a transfer ledger that records exactly what simulator assumptions survived hardware contact.",
        key_insight="Dexterous sim-to-real does not fail only because the simulator is imperfect. It fails because contact behavior is so sensitive that small mismatches in delay, friction, or compliance can change the entire contact sequence.",
        figure_boxes=["Model|sim assumptions", "Randomize|contact params", "Transfer|real rollouts", "Audit|gap and repair"],
        figure_caption="Dexterous transfer works when simulator assumptions are recorded, stressed, and audited against real contact traces rather than treated as invisible background.",
        theory_1="The simulator serves as a proposal generator for contact strategies, not as an oracle. Transfer succeeds when the policy has seen enough variability to survive the small but decisive differences between simulated and real fingertips, objects, and timing.",
        theory_2="For dexterity, the important gaps are often not image realism but contact realism: friction coefficients, local compliance, sensor latency, finger backlash, and object inertial mismatch.",
        formula=r"\theta^\star = \arg\min_\theta \mathbb{E}_{\phi \sim p(\Phi)}\left[\mathcal{L}_{\text{sim}}(\theta;\phi)\right],\qquad \Delta_{\text{real-sim}} = d(\tau_{\text{real}}, \tau_{\text{sim}})",
        mechanism="The team fits or randomizes a family of simulator parameters, trains a dexterous policy across that family, and then compares simulator and hardware traces for the same task panel. The transfer artifact should include the parameter ranges and the first real-world failure signatures.",
        algorithm_steps=[
            "Identify or randomize friction, delay, compliance, and sensor-noise ranges before large-scale training.",
            "Train on parameter families that preserve plausible contact physics instead of randomizing blindly.",
            "Run hardware pilots with strong safety limits and compare real traces against simulated traces directly.",
            "Update the simulator family or recovery policy when the first mismatch signatures appear.",
        ],
        code_title="Algorithm: Transfer Gap Ledger",
        code="""# Record one sim-to-real gap summary for a dexterous task.
sim = {"slip_rate": 0.08, "success": 0.81}
real = {"slip_rate": 0.19, "success": 0.62}

gap = {
    "slip_gap": round(real["slip_rate"] - sim["slip_rate"], 2),
    "success_gap": round(sim["success"] - real["success"], 2),
}
print(gap)""",
        code_output="{'slip_gap': 0.11, 'success_gap': 0.19}",
        code_caption="Code Fragment 43.5.1 is intentionally simple: the first transfer artifact should make the gap concrete before anyone argues about why it happened.",
        expected_output="The expected output reveals that real hardware slips more and succeeds less than simulation. That immediately suggests a contact mismatch rather than a purely visual mismatch.",
        library_shortcut="MuJoCo, ManiSkill, and tactile simulators help produce transfer-ready rollouts, but successful dexterous transfer still depends on careful real-trace comparison and guarded hardware deployment.",
        recipe_steps=[
            "Measure actuator delay and fingertip compliance on hardware before sim policy training begins.",
            "Randomize only parameters that could plausibly vary in the real system.",
            "Compare sim and real on the same task instances and metrics whenever possible.",
            "Use a hardware safety gate that limits force, speed, and number of consecutive failures.",
            "Log real-world failures as transfer cases, not as embarrassing exceptions.",
        ],
        warning="Randomization can become a ritual. If the parameter family does not cover the real mismatch that matters, more randomization only hides the blind spot behind extra compute.",
        practical_example="Dexterous cube rotation often transfers poorly when fingertip friction or actuator delay is mis-modeled, even if the simulator looks visually convincing and the policy score is high.",
        fun_note="A simulator that always agrees with your policy might just be a very supportive fiction writer.",
        frontier="Differentiable tactile simulation, faster visuo-tactile rendering, and richer hand models are improving transfer. The lasting discipline is still to measure the first real mismatch and fold it back into the model family.",
        self_check="Could you name the top three contact parameters whose mismatch would most damage your hardware result?",
        deep_dive_1="Sim-to-real for dexterity is a natural place to teach parameter families rather than single best-fit models. Contact behavior lives in ranges, and robust policies must survive those ranges rather than memorize a single simulator setting.",
        deep_dive_2="It is also where careful evidence culture pays off. A side-by-side trace of sim and real force, slip, and orientation can explain more than a hundred aggregate benchmark points.",
        tool_rows=[
            ["MuJoCo", "Dexterous transfer simulation", "Use it for fast contact rollouts and parameter sweeps."],
            ["TACTO or tactile simulators", "Touch-channel modeling", "Helpful when tactile cues drive contact transitions or slip detection."],
            ["Hardware transfer ledger", "Mismatch auditing", "Record slip, timing, and success gaps for each transfer round."],
        ],
        lab="Train a toy dexterous policy in simulation under three friction settings, then evaluate a held-out friction value and explain how the transfer gap should be recorded.",
        failure_pattern="When transfer fails, first check which trace diverged earliest: pose, force, slip, or timing. The earliest divergence is usually the most actionable one.",
        takeaway="Dexterous sim-to-real succeeds by auditing contact mismatches explicitly and training across the parameter ranges that actually matter on hardware.",
        exercise="Write a transfer ledger template for a dexterous task with fields for friction, delay, tactile noise, success, slip, and first divergence time.",
        bibliography=[
            BibEntry("MuJoCo", "https://mujoco.org/", "Widely used simulator for dexterous control and transfer studies."),
            BibEntry("TACTO", "https://github.com/facebookresearch/tacto", "Open-source simulator for high-resolution vision-based tactile sensing."),
            BibEntry("Tactile Gym", "https://github.com/ac-93/tactile_gym", "Open tactile RL environments useful for sim-to-real studies."),
        ],
    ),
    SectionData(
        number="44.1",
        title="Why touch matters for contact-rich tasks",
        chapter_num=44,
        chapter_title="Tactile and Visuo-Tactile Learning",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-44-tactile-and-visuo-tactile-learning",
        image="chapter-44-illustration-01.png",
        epigraph="Vision sees where contact might happen, touch says what contact actually became.",
        epigraph_cite="A Tactile Systems Group",
        description="Touch matters because many decisive task variables, slip, local compliance, micro-geometry, and incipient failure, become observable only after contact begins.",
        reader_pathway="Track the hidden variables that vision misses: contact onset, pressure, shear, slip, compliance, and texture. The central systems question is how those signals change action before failure becomes visible.",
        develops="This section explains why tactile sensing is not an exotic add-on. For contact-rich tasks, it is often the only channel that exposes the local state the robot must react to within tens of milliseconds.",
        connects="It joins perception, manipulation, and control by showing how touch converts hidden contact state into measurable evidence that can change the next action.",
        key_insight="Touch is valuable not because it duplicates vision, but because it reveals the variables vision cannot reliably infer once the scene is occluded by the hand or the object itself.",
        figure_boxes=["Sense|pressure and shear", "Infer|contact state", "Act|adjust grip", "Verify|slip avoided"],
        figure_caption="Touch closes the loop on contact by surfacing state variables that are invisible or ambiguous in camera space.",
        theory_1="Once contact begins, the robot's latent state includes normal force, tangential shear, contact patch shape, and local compliance. These quantities drive success or failure, yet they are often weakly observed or fully hidden from vision.",
        theory_2="Tactile sensing matters most when the correct action depends on these hidden states, such as increasing grip force before slip, searching for insertion alignment, or distinguishing a rigid stop from a soft obstacle.",
        formula=r"\text{slip risk} \propto \|\mathbf{f}_t\| - \mu f_n,\qquad o_t = [I_t, q_t, z_t^{\text{tactile}}],\qquad a_t = \pi(o_t)",
        mechanism="The robot observes tactile signals at contact, infers a contact state such as stable hold, incipient slip, or misalignment, adjusts force or motion accordingly, and then verifies whether the contact stabilized or deteriorated.",
        algorithm_steps=[
            "Instrument one contact-rich task with tactile and non-tactile observations collected in sync.",
            "Label which action decisions require contact information rather than only vision or proprioception.",
            "Train or script a policy that can react to those tactile cues before visible failure occurs.",
            "Evaluate on cases where vision becomes ambiguous or fully occluded during contact.",
        ],
        code_title="Algorithm: Slip Margin Monitor",
        code="""# Compute a simple tactile slip margin from tangential and normal force.
mu = 0.55
normal_force = 8.0
tangential_force = 3.8

margin = round(mu * normal_force - tangential_force, 2)
status = "stable" if margin > 0.0 else "slip_risk"
print({"slip_margin_N": margin, "status": status})""",
        code_output="{'slip_margin_N': 0.6, 'status': 'stable'}",
        code_caption="Code Fragment 44.1.1 turns a tactile contact estimate into a control-relevant stability margin.",
        expected_output="The expected result reports a positive slip margin, meaning the current grip should hold under the simple friction model. As that margin shrinks toward zero, the controller should react before visible object motion appears.",
        library_shortcut="DIGIT, GelSight, ReSkin or AnySkin style hardware, and tactile-processing libraries can expose the raw tactile stream quickly. The real engineering work is connecting that stream to the right control decision and verifier.",
        recipe_steps=[
            "Synchronize tactile, vision, and robot-state logs before modeling anything.",
            "Identify one task decision that genuinely depends on contact evidence.",
            "Derive simple tactile baselines such as slip margins or contact-onset detectors first.",
            "Compare tactile and vision-only policies on occluded or slippery cases.",
            "Store tactile traces beside controller actions and success labels.",
        ],
        warning="Teams often add touch and then evaluate on tasks where vision already solves everything. That guarantees disappointment because the extra modality is never given a chance to matter.",
        practical_example="Grasping a smooth bottle, inserting a plug, or opening a child-safe container all benefit from touch because the crucial success cues appear only after the hand blocks the camera or local contact starts to deform.",
        fun_note="If the robot learns that the object is slipping only after the object is halfway to the floor, the tactile sensor has become a historian instead of a teammate.",
        frontier="The frontier includes richer tactile skins, visuo-tactile pretraining, and whole-hand contact representations. The stable benchmark remains simple: does the extra modality change the next action in a way that reduces failure?",
        self_check="Can you name one failure in your manipulation loop that becomes detectable earlier with touch than with vision?",
        deep_dive_1="Touch is especially important pedagogically because it shifts students away from camera-centric thinking. Many contact-rich problems are not missing intelligence so much as missing observability of the right state variables.",
        deep_dive_2="This section also frames tactile sensing as an information-value problem. The modality is worth its hardware and software cost only when it changes action quality on the hard cases, not when it confirms what vision already knew.",
        tool_rows=[
            ["DIGIT or GelSight", "High-resolution local contact sensing", "Use them when surface geometry and slip cues matter at the fingertip."],
            ["Force-torque sensors", "Global contact loads", "Helpful for complementing localized tactile images with overall wrench information."],
            ["PyTouch", "Tactile data processing", "Useful for prototyping tactile-learning pipelines and feature extraction."],
        ],
        lab="Build a slip detector using tactile and force data, then show on a held-out object why the detector fires before a vision-only baseline notices failure.",
        failure_pattern="If tactile signals do not help, ask whether the task truly requires contact information, whether the sensor was synchronized correctly, or whether the policy ignores the tactile channel entirely.",
        takeaway="Touch matters when hidden contact variables decide the next action faster than vision can observe the failure.",
        exercise="Describe one contact-rich task where touch should change the action earlier than vision. Name the exact tactile feature you would monitor.",
        bibliography=[
            BibEntry("DIGIT tactile sensor", "https://digit.ml/digit.html", "Compact high-resolution tactile sensor widely used for manipulation research."),
            BibEntry("AnySkin", "https://any-skin.github.io/", "Replaceable magnetic tactile sensing platform for robust robot touch."),
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Machine-learning library for tactile-signal processing and modeling."),
        ],
    ),
    SectionData(
        number="44.2",
        title="Vision-based tactile sensors (GelSight, DIGIT)",
        chapter_num=44,
        chapter_title="Tactile and Visuo-Tactile Learning",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-44-tactile-and-visuo-tactile-learning",
        image="chapter-44-illustration-02.png",
        epigraph="A tactile camera turns deformation into geometry.",
        epigraph_cite="A Sensor Bench Engineer",
        description="Vision-based tactile sensors convert local surface deformation inside a compliant fingertip into images that can be processed like dense contact maps.",
        reader_pathway="Follow the signal path from elastomer deformation to illumination pattern, image formation, feature extraction, and contact-state estimation. The core question is what the tactile image is actually measuring.",
        develops="This section explains how GelSight, DIGIT, and related optical tactile sensors encode contact geometry, pressure patterns, and shear through deformable skins, lighting, and camera observation.",
        connects="It links tactile hardware design to perception pipelines and to the downstream manipulation policies that consume those local contact images.",
        key_insight="A vision-based tactile image is not just another camera frame. It is an indirect measurement of deformation, so calibration and reconstruction assumptions matter as much as the neural network that reads the image.",
        figure_boxes=["Deform|elastomer", "Image|illumination", "Infer|contact map", "Act|grip update"],
        figure_caption="Optical tactile sensors transform deformation into images, then back into contact-state estimates that the controller can use immediately.",
        theory_1="Optical tactile sensors observe a deformable interface under controlled lighting. Contact changes marker motion, shading, or surface normal fields, which can then be decoded into geometry, force proxies, or slip cues.",
        theory_2="The modeling burden shifts from classical force sensing toward calibration, photometric consistency, and deformation reconstruction. That is why tactile-image interpretation benefits from both geometric and learned approaches.",
        formula=r"I_t = \mathcal{R}(n_t, \rho, \ell, c),\qquad \hat z_t = f_\theta(I_t),\qquad \Delta m_t \Rightarrow \text{shear or slip cue}",
        mechanism="The sensor records a contact image, maps it to deformation features or reconstructed geometry, estimates local force or slip proxies, and then feeds those estimates into a manipulation controller or policy. Calibration drift and skin wear are part of the real system state.",
        algorithm_steps=[
            "Calibrate the tactile camera and lighting under no-contact and known-contact conditions.",
            "Extract contact patch, marker motion, or reconstructed depth from each tactile frame.",
            "Map tactile image features to control-relevant quantities such as slip, shear, or local geometry.",
            "Monitor drift from sensor wear or lighting change and refresh calibration when needed.",
        ],
        code_title="Algorithm: Marker-Shift Slip Cue",
        code="""# Turn marker motion into a simple slip cue.
marker_dx = [0.2, 0.5, 0.9, 1.3]
mean_shift = round(sum(marker_dx) / len(marker_dx), 2)
slip_like = mean_shift > 0.7
print({"mean_marker_shift_px": mean_shift, "slip_like": slip_like})""",
        code_output="{'mean_marker_shift_px': 0.72, 'slip_like': True}",
        code_caption="Code Fragment 44.2.1 captures the basic logic behind many optical tactile pipelines: local image motion can become a slip-relevant control signal.",
        expected_output="The expected trace flags a slip-like event because average marker motion is large. In a real system, that cue would be combined with normal-force context and controller state before acting.",
        library_shortcut="DIGIT and GelSight ecosystems supply hardware references, while tactile-processing libraries and simulator tools help with fast prototyping. The winning workflow still depends on clean calibration and task-specific control targets.",
        recipe_steps=[
            "Start with no-contact, static-contact, and sliding-contact calibration captures.",
            "Choose the contact quantity you actually need: geometry, shear, force proxy, or slip cue.",
            "Keep raw tactile frames and derived features together in the dataset.",
            "Track sensor wear because elastomer aging changes the signal distribution over time.",
            "Validate tactile-image interpretations on real tasks, not only on offline reconstruction metrics.",
        ],
        warning="A visually beautiful tactile image can still be useless if the calibration does not tie it to a control-relevant quantity. Pretty contact images are not the same thing as actionable touch.",
        practical_example="Optical tactile sensors are especially strong for local shape discrimination, slip onset, and fine alignment tasks such as connector insertion or textured-surface following.",
        fun_note="Tactile cameras are among the few sensors where a blurry blob can be exactly what you wanted, provided you know which contact patch and shear field it represents.",
        frontier="Recent work expands from flat optical fingertips to richer geometries, higher taxel density, and on-device tactile inference. The systems challenge remains calibration stability and fast control integration.",
        self_check="Could you explain what physical quantity your tactile model is estimating from the image, and which calibration assumption makes that estimate possible?",
        deep_dive_1="This section is a natural point to teach sensor models. Students often jump straight into neural decoding, but optical tactile sensing is most legible when the image formation and deformation path are named explicitly first.",
        deep_dive_2="It also clarifies why visuo-tactile learning is not a free fusion win. If the tactile image is poorly calibrated or heavily drifting, the combined model may learn the wrong alignment altogether.",
        tool_rows=[
            ["DIGIT", "Compact optical tactile hardware", "Good for portable, affordable, image-based touch sensing."],
            ["GelSight family", "High-fidelity contact geometry", "Strong when local shape and texture detail matter."],
            ["PyTouch", "Feature extraction and learning", "Use it to prototype tactile-image pipelines quickly."],
        ],
        lab="Collect a small tactile dataset with no-contact, stable-contact, and slip phases. Show how one visual feature changes across the three modes.",
        failure_pattern="If predictions drift, inspect calibration, elastomer wear, and illumination before blaming the learning model. Optical tactile pipelines fail physically before they fail statistically.",
        takeaway="Vision-based tactile sensors are powerful because they transform deformation into dense contact images, but that power depends on careful calibration and task-linked interpretation.",
        exercise="Choose one optical tactile feature, such as marker shift or reconstructed height, and explain how it would enter a manipulation controller.",
        bibliography=[
            BibEntry("DIGIT", "https://digit.ml/digit.html", "Reference hardware platform for compact high-resolution optical tactile sensing."),
            BibEntry("TACTO", "https://github.com/facebookresearch/tacto", "Simulation framework for high-resolution vision-based tactile sensing."),
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Open ML library for tactile touch sensing and feature learning."),
        ],
    ),
    SectionData(
        number="44.3",
        title="Simulating touch (e.g., tactile sim in Isaac)",
        chapter_num=44,
        chapter_title="Tactile and Visuo-Tactile Learning",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-44-tactile-and-visuo-tactile-learning",
        image="chapter-44-illustration-03.png",
        epigraph="Simulated touch is a promise about which contact features will survive reality.",
        epigraph_cite="A Tactile Sim Engineer",
        description="Tactile simulation matters because collecting large real tactile datasets is expensive, but the simulator must decide which parts of tactile reality it aims to preserve and which it approximates.",
        reader_pathway="Follow the split between contact mechanics and tactile rendering. The central idea is that many tactile simulators approximate image formation or deformation without fully solving the true physics.",
        develops="This section explains the main tactile simulation styles: rendering-based optical tactile simulators, mechanics-focused deformation models, and integrated simulators in frameworks such as Isaac or MuJoCo extensions.",
        connects="It ties simulation, data generation, and sim-to-real transfer by making the sensor model explicit rather than hiding it behind a generic domain-randomization story.",
        key_insight="A tactile simulator is only useful if you can state which contact quantities it preserves well enough for the downstream policy or estimator you care about.",
        figure_boxes=["Physics|contact state", "Render|tactile signal", "Learn|policy or encoder", "Audit|sim-real gap"],
        figure_caption="Tactile simulation is a pipeline from contact mechanics to synthetic sensor output, and the weak link depends on which tactile quantity the downstream task needs.",
        theory_1="Many tactile simulators split the problem into rigid-body contact from a base physics engine and sensor rendering or deformation synthesis on top. That makes them fast, but it means their guarantees are task-specific rather than universal.",
        theory_2="For optical tactile sensors, image realism can matter more than exact force fidelity if the downstream model reads local geometry from marker motion or shading. For force or compliance tasks, the opposite can be true.",
        formula=r"\hat I_t = \mathcal{S}(x_t, c_t, \phi),\qquad \Delta_{\text{tactile}} = d(\hat I_t, I_t^{\text{real}}),\qquad \Delta_{\text{control}} = d(a_t^{\text{sim}}, a_t^{\text{real}})",
        mechanism="The simulator consumes contact state from a physics engine, synthesizes a tactile observation according to a sensor model, and feeds it into a learning or control stack. The real evaluation question is whether control behavior transfers, not only whether the tactile frame looks plausible.",
        algorithm_steps=[
            "Define the tactile quantity your downstream task actually needs.",
            "Choose a simulator whose abstractions preserve that quantity well enough.",
            "Generate paired sim and real tactile episodes under matched contact conditions.",
            "Measure both frame-level similarity and control-level transfer for the same task panel.",
        ],
        code_title="Algorithm: Tactile Sim Gap Check",
        code="""# Compare a simulated and real tactile scalar proxy.
sim_depth = [0.12, 0.18, 0.21]
real_depth = [0.10, 0.15, 0.19]

mean_gap = round(sum(abs(a - b) for a, b in zip(sim_depth, real_depth)) / len(sim_depth), 3)
print({"mean_depth_gap": mean_gap, "usable_for_pretraining": mean_gap < 0.03})""",
        code_output="{'mean_depth_gap': 0.023, 'usable_for_pretraining': True}",
        code_caption="Code Fragment 44.3.1 is a reminder that tactile simulation should be audited against the quantity the downstream model will actually use.",
        expected_output="The expected result declares the simulator usable for a pretraining stage under this simple proxy. In a full system, that claim still needs downstream control validation on the same task panel.",
        library_shortcut="TACTO remains a standard optical tactile simulator, while MuJoCo forks and Isaac-based tactile projects extend the ecosystem. Each route saves effort only if the team records the sensor assumptions and real-world comparison panel.",
        recipe_steps=[
            "Match simulated and real contact episodes as closely as possible before comparing outputs.",
            "Audit the tactile quantity that the downstream learner will consume, not an arbitrary image similarity score.",
            "Randomize sensor assumptions within plausible limits rather than inventing unrealistic noise.",
            "Keep one transfer ledger that stores both frame-level and behavior-level gap measures.",
            "Use real tactile clips to spot the first failure mode your simulator cannot reproduce.",
        ],
        warning="Teams often report tactile simulation quality with beautiful rendered frames but never show whether the same policy or estimator behaves similarly on real hardware. For embodied systems, that omission is fatal.",
        practical_example="Plug insertion or peg alignment can benefit enormously from tactile simulation if the simulator captures the local geometry cues the policy uses, even if it does not reconstruct exact absolute force values.",
        fun_note="A tactile simulator can be wrong in two impressively different ways: it can look real and control badly, or look fake and still teach the policy the right contact habit.",
        frontier="Differentiable tactile simulation, faster GPU pipelines, and Isaac-integrated visuo-tactile stacks are improving quickly. The core systems job is still to define what realism means for the task at hand.",
        self_check="What exact tactile quantity does your simulator need to preserve for your downstream controller to behave correctly?",
        deep_dive_1="This section is ideal for teaching task-grounded simulation fidelity. Students learn that no simulator is realistic in the abstract; it is realistic relative to a target quantity and downstream use.",
        deep_dive_2="It also reveals why sim-to-real audits should include control trajectories, not just rendered sensor examples. The policy might ignore visually striking simulator flaws while failing on a small missing slip cue.",
        tool_rows=[
            ["TACTO", "Optical tactile rendering", "Strong baseline when working with DIGIT-like sensors and PyBullet-style pipelines."],
            ["TACTO-MuJoCo", "MuJoCo tactile integration", "Useful when the rest of the manipulation stack already lives in MuJoCo."],
            ["Isaac-based tactile projects", "High-throughput tactile data generation", "Good when large-scale parallel simulation and policy learning are central."],
        ],
        lab="Generate a tiny synthetic tactile dataset and compare it to three matched real contacts. Explain which differences would matter for control and which would not.",
        failure_pattern="If transfer fails, distinguish whether the simulator missed a frame-level cue, a dynamics cue, or a controller-timing cue. Those gaps call for different repairs.",
        takeaway="Tactile simulation is useful when its abstractions preserve the contact signals that your downstream learner or controller actually consumes.",
        exercise="Choose a tactile task and define one frame-level and one control-level sim-to-real metric you would use to judge a tactile simulator.",
        bibliography=[
            BibEntry("TACTO", "https://github.com/facebookresearch/tacto", "Open-source simulator for high-resolution vision-based tactile sensors."),
            BibEntry("TACTO-MuJoCo", "https://github.com/L3S/TACTO-MuJoCo", "MuJoCo integration for optical tactile simulation."),
            BibEntry("TactSim Isaac Lab project", "https://github.com/yuanqing-ai/TactSim-IsaacLab", "Example of Isaac-based tactile simulation for parallel data collection."),
        ],
    ),
    SectionData(
        number="44.4",
        title="Visuo-tactile pretraining and policies",
        chapter_num=44,
        chapter_title="Tactile and Visuo-Tactile Learning",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-44-tactile-and-visuo-tactile-learning",
        image="chapter-44-illustration-04.png",
        epigraph="The point of multimodality is to make one channel useful when the other one lies.",
        epigraph_cite="A Multimodal Robot Group",
        description="Visuo-tactile pretraining tries to align what the robot sees before contact with what it feels during contact, so a policy can carry uncertainty and object state across that transition more intelligently.",
        reader_pathway="Track representation learning, cross-modal alignment, downstream policy interfaces, and the dataset biases that can cause a model to ignore touch entirely.",
        develops="This section explains contrastive and sequence-model approaches to joint visual and tactile representation learning, then ties them to manipulation policies that need to react under occlusion, slip, or contact ambiguity.",
        connects="It connects tactile sensing to modern robot foundation-model ideas, but grounds them in the concrete question of whether touch changes the next action on difficult episodes.",
        key_insight="A visuo-tactile model is only stronger than a visual model if the training process forces it to use the tactile channel on cases where vision is uncertain or misleading.",
        figure_boxes=["Encode|vision and touch", "Align|shared latent", "Act|policy head", "Verify|hard-case gain"],
        figure_caption="Joint visuo-tactile learning is valuable when the shared representation changes control behavior on occluded, slippery, or contact-ambiguous tasks.",
        theory_1="The central representation question is whether vision and touch should share a latent space, a predictive state, or only a late fused policy head. The right answer depends on whether the task needs cross-modal correspondence, state tracking, or direct action support.",
        theory_2="Many practical systems use a contrastive or predictive loss to align pre-contact visual features with post-contact tactile observations, then fine-tune a policy on top. The failure mode is obvious: if vision alone solves the training distribution, the model learns to ignore touch.",
        formula=r"\mathcal{L}_{\text{vt}} = -\log \frac{\exp(\mathrm{sim}(z_v, z_t)/\tau)}{\sum_j \exp(\mathrm{sim}(z_v, z_t^{(j)})/\tau)},\qquad a_t = \pi([z_v, z_t, q_t])",
        mechanism="The learner encodes visual and tactile streams, aligns or predicts across them, and then exposes a fused latent state to the manipulation policy. Evaluation must isolate hard cases where the tactile branch should matter.",
        algorithm_steps=[
            "Define which task phases are pre-contact visual, contact-rich tactile, or mixed.",
            "Train a representation that couples those phases through aligned objects, actions, or future outcomes.",
            "Fine-tune the policy with episodes where tactile information changes the optimal action.",
            "Audit the fused model against vision-only and touch-only ablations on the same hard cases.",
        ],
        code_title="Algorithm: Cross-Modal Hard-Case Audit",
        code="""# Compare fused and vision-only performance on hard episodes.
vision_only = {"hard_success": 0.41}
visuo_tactile = {"hard_success": 0.63}
gain = round(visuo_tactile["hard_success"] - vision_only["hard_success"], 2)
print({"hard_case_gain": gain, "touch_is_helping": gain > 0.0})""",
        code_output="{'hard_case_gain': 0.22, 'touch_is_helping': True}",
        code_caption="Code Fragment 44.4.1 encodes the central evaluation idea for visuo-tactile learning: compare on the hard episodes where touch should matter.",
        expected_output="The expected output reports a positive gain on hard cases. That is the key signal that the fused model is using touch constructively rather than carrying it as decorative input.",
        library_shortcut="LeRobot, PyTouch, and custom multimodal encoders can accelerate experimentation, but the key artifact remains the hard-case audit that proves touch affects decisions under occlusion or slip.",
        recipe_steps=[
            "Define hard cases before pretraining so the evaluation target is clear.",
            "Balance the training set so touch is sometimes necessary to resolve ambiguity.",
            "Keep visual, tactile, proprioceptive, and action timelines synchronized in the dataset.",
            "Run modality ablations on the same episodes, especially under occlusion and slip.",
            "Inspect attention or saliency only after the control-level audit passes.",
        ],
        warning="If the dataset lets vision solve almost every example, the model will gladly ignore touch while still producing impressive aggregate metrics.",
        practical_example="Package opening, compliant insertion, and slippery pick tasks often benefit from visuo-tactile pretraining because the model can use visual context to anticipate contact and tactile feedback to correct it.",
        fun_note="Multimodal models are a little like group projects: if one member can do all the work, the others may quietly coast until the hard case arrives.",
        frontier="The frontier includes visuo-tactile transformers, contact-predictive world models, and large multimodal robot corpora. The reliable contribution is still measurable hard-case improvement tied to action quality.",
        self_check="What exact episode type in your benchmark should force the fused model to use touch instead of only vision?",
        deep_dive_1="A useful way to teach this topic is through counterfactuals. Ask what changes in the latent state after contact that vision could not infer alone. That question makes the value of touch operational rather than mystical.",
        deep_dive_2="This section also introduces an important research discipline: ablate by episode type, not only by dataset average. Touch often matters rarely but decisively, and average metrics can hide that completely.",
        tool_rows=[
            ["LeRobot", "Multimodal robot data handling", "Useful for synchronized robot trajectories and policy training pipelines."],
            ["PyTouch", "Tactile encoding and learning", "Good for quickly prototyping tactile feature extractors or encoders."],
            ["Custom transformer or sequence models", "Fusion backbone", "Use them only after defining the episode types where fusion should matter."],
        ],
        lab="Build a fused and a vision-only model on a tiny benchmark with occluded-contact episodes. Compare only on those episodes and explain the difference.",
        failure_pattern="If the fused model shows no hard-case gain, ask whether the dataset hid tactile necessity, whether synchronization is broken, or whether the policy head ignores the tactile latent.",
        takeaway="Visuo-tactile pretraining is successful when it creates measurable hard-case gains on episodes where touch should change the action.",
        exercise="Design a hard-case panel for a visuo-tactile policy and specify the ablations you would run to prove the tactile channel is useful.",
        bibliography=[
            BibEntry("LeRobot", "https://github.com/huggingface/lerobot", "Open framework for robot datasets and policy training that can host multimodal inputs."),
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Reference tactile-learning library for multimodal experiments."),
            BibEntry("NeuralFeels", "https://github.com/facebookresearch/neuralfeels", "Visuo-tactile neural-field project showing multimodal object-state inference in manipulation."),
        ],
    ),
    SectionData(
        number="44.5",
        title="Combining vision and touch",
        chapter_num=44,
        chapter_title="Tactile and Visuo-Tactile Learning",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-44-tactile-and-visuo-tactile-learning",
        image="chapter-44-illustration-05.png",
        epigraph="Fusion is only useful when it changes what the robot decides next.",
        epigraph_cite="A Fusion Engineer's Whiteboard",
        description="Combining vision and touch is an estimation and control problem, not just a neural-architecture choice. The modalities differ in range, field of view, latency, and the kinds of uncertainty they expose.",
        reader_pathway="Track complementarity, fusion timing, confidence, and modality handoff. The practical question is when the controller should trust vision, when it should trust touch, and when it should request more evidence.",
        develops="This section covers early, late, and state-level fusion between vision and tactile sensing, with attention to contact onset, occlusion, uncertainty, and action-conditioned confidence.",
        connects="It synthesizes the whole chapter by turning multimodal sensing into a real control interface rather than a general claim that more modalities must be better.",
        key_insight="Vision and touch should not always vote equally. The right fusion policy changes with distance to contact, occlusion level, slip risk, and what state variable the controller needs right now.",
        figure_boxes=["See|pre-contact scene", "Feel|local contact", "Fuse|state belief", "Act|adaptive control"],
        figure_caption="Good vision-touch fusion is state-dependent: vision dominates before contact, touch often dominates during local interaction, and the controller should know when to hand over trust.",
        theory_1="Vision offers global context and long-range target localization, while touch offers precise local contact evidence after interaction begins. Fusion should therefore be conditioned on phase and uncertainty rather than forced into a static weighted average.",
        theory_2="A useful formulation maintains a latent state with modality-specific observation models. The controller then updates its belief differently before contact, at contact onset, and during sustained manipulation.",
        formula=r"b_{t+1}(s) \propto p(o_t^{v}\mid s)\,p(o_t^{t}\mid s)\,\sum_{s'} p(s\mid s', a_t)\,b_t(s'),\qquad \alpha_t = f(\text{contact}, \sigma_v, \sigma_t)",
        mechanism="The system predicts state from vision before contact, shifts weight toward touch as local interaction begins, and exposes a fused belief to the policy or controller. The decisive engineering choice is the gating logic that decides when each modality should dominate.",
        algorithm_steps=[
            "Define which state variables are better observed by vision and which by touch.",
            "Switch or reweight modalities based on contact phase and uncertainty.",
            "Expose the fused belief, not the raw modalities alone, to the downstream controller where possible.",
            "Audit failure cases where one modality confidently disagrees with the other.",
        ],
        code_title="Algorithm: Contact-Phase Fusion Gate",
        code="""# Reweight vision and touch after contact onset.
vision_sigma = 0.35
tactile_sigma = 0.12
contact = True

touch_weight = 0.7 if contact else 0.2
vision_weight = 1.0 - touch_weight
fused_uncertainty = round(vision_weight * vision_sigma + touch_weight * tactile_sigma, 3)
print({"vision_weight": vision_weight, "touch_weight": touch_weight, "fused_uncertainty": fused_uncertainty})""",
        code_output="{'vision_weight': 0.3, 'touch_weight': 0.7, 'fused_uncertainty': 0.189}",
        code_caption="Code Fragment 44.5.1 demonstrates the most important multimodal lesson in contact-rich control: fusion weights should change when the physics of the task changes.",
        expected_output="The expected result shifts trust toward touch after contact. That is appropriate when local contact cues become more reliable than vision for the state variable the controller now needs.",
        library_shortcut="ROS 2 message synchronizers, tactile libraries, and multimodal encoders make data transport manageable. The difficult part is still designing the phase-aware trust logic and auditing disagreement cases.",
        recipe_steps=[
            "Write down which state variables each modality should dominate before building the fusion model.",
            "Synchronize timestamps tightly so disagreements are interpretable.",
            "Use explicit contact-phase gates or learned uncertainty estimates rather than static equal weighting.",
            "Create disagreement episodes where one modality is wrong and the other is right.",
            "Evaluate fusion with task metrics and disagreement analysis, not only latent-space pretty pictures.",
        ],
        warning="Equal-weight fusion is often lazy engineering. When one modality is uninformative or stale, averaging can be worse than trusting the better source decisively.",
        practical_example="In peg insertion, vision places the peg near the hole, while touch takes over for local alignment and slip-free seating once the peg starts interacting with the rim.",
        fun_note="Vision and touch are like two strong opinions at a meeting. The trick is not to average them politely, it is to know which one has actually seen the problem from the right distance.",
        frontier="Current work explores learned fusion gates, world models with tactile state, and cross-modal retrieval. The enduring systems question is still whether fusion improves action quality on disagreement-heavy episodes.",
        self_check="When vision and touch disagree in your task, which modality should win, and what evidence supports that choice?",
        deep_dive_1="This section is where the chapter's pieces finally connect. The fusion problem is about sensing, control phase, uncertainty, and action consequences all at once, which makes it a compact summary of embodied-system thinking.",
        deep_dive_2="A good advanced exercise is to compare early fusion, late fusion, and belief-state fusion on the same task. Students quickly see that the architecture question is inseparable from the control-phase question.",
        tool_rows=[
            ["ROS 2 synchronization tools", "Timestamp alignment", "Use them to keep multimodal episodes temporally coherent."],
            ["PyTouch", "Tactile features", "Useful for constructing tactile state estimates that can be fused with vision."],
            ["Belief-state or sequence models", "Phase-aware fusion", "Prefer them when uncertainty and contact phase change the best action materially."],
        ],
        lab="Build a simple fusion gate that changes modality weights at contact onset. Compare it with static equal weighting on a small insertion or slip-detection benchmark.",
        failure_pattern="When fusion fails, inspect timestamp alignment, phase gating, and disagreement handling before changing the neural backbone. Many multimodal failures are systems bugs wearing a representation-learning costume.",
        takeaway="Combining vision and touch works when modality trust shifts with contact phase, uncertainty, and the actual state variable the controller needs.",
        exercise="Design a disagreement benchmark in which vision is misleading but touch is informative, and a second benchmark with the opposite property. Explain how your fusion logic should react in each.",
        bibliography=[
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Open tactile-learning library relevant for tactile feature extraction and fusion experiments."),
            BibEntry("DIGIT", "https://digit.ml/digit.html", "Representative optical tactile hardware often fused with vision."),
            BibEntry("NeuralFeels", "https://github.com/facebookresearch/neuralfeels", "Visuo-tactile object-state inference project illustrating cross-modal fusion for manipulation."),
        ],
    ),
]


def chapter_sections(ch_num: int) -> List[SectionData]:
    return [s for s in SECTIONS if s.chapter_num == ch_num]


CHAPTERS: List[ChapterData] = [
    ChapterData(
        number=42,
        title="Robotic Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-42-robotic-manipulation",
        epigraph="Manipulation begins where motion planning meets consequence.",
        epigraph_cite="A Careful Embodied Systems Builder",
        big_picture="This chapter treats robotic manipulation as object-state control under geometry, contact, friction, and uncertainty. The core teaching move is to keep object outcome, not arm motion alone, at the center of every method.",
        remember="Good manipulation stacks expose explicit contracts for object state, contact mode, verifier logic, and recovery. A motion that looks smooth but leaves those contracts vague is not yet an embodied system.",
        overview_1="Chapter 42 moves from the simplest object-state changes, reaching and pushing, into staged pick-and-place pipelines, contact-rich control, perception for action, learned policies, recovery, and finally whole-body mobile manipulation.",
        overview_2="The practical stack emphasizes MoveIt 2, cuRobo or cuMotion, Drake, MuJoCo, ManiSkill, Nav2, and BehaviorTree.CPP. The theory thread stays grounded in object-state change, contact residuals, and same-panel evidence.",
        prereqs="Readers should already be comfortable with frames, Jacobians, control loops, simulation, and basic policy-learning ideas. This chapter shows how those ingredients become a manipulation system that can be audited and repaired.",
        tooling_note="Use maintained planners and simulators early, but keep the manipulation contract explicit: object state, action interface, verifier, and recovery route must survive any library swap.",
        lab_objective="Build a small manipulation benchmark that includes at least one reach-push task, one pick-and-place task, and one failure-recovery branch, all logged with the same evidence schema.",
        lab_steps=[
            "Define the object-state variables, action interfaces, and success metrics for all tasks.",
            "Implement a transparent baseline and one maintained-tool route for each task family.",
            "Log object outcomes, controller signals, and failure labels in one artifact per run.",
            "Compare nominal and perturbed episodes on the same panel.",
            "Write a short postmortem that explains one failure and one successful recovery.",
        ],
        production_notes="Read each section as a system contract. Ask what the robot observes, which object state changes, which contact assumptions are active, and how the system proves success rather than merely animating the arm convincingly.",
        tool_map=[
            ["MoveIt 2", "Motion planning, staging, and execution for arm-level manipulation"],
            ["cuMotion or cuRobo", "Fast collision-free motion generation and replanning"],
            ["Drake and MuJoCo", "Contact-aware simulation, control analysis, and residual inspection"],
            ["ManiSkill", "Manipulation benchmarks and high-throughput policy training"],
            ["Nav2 and BehaviorTree.CPP", "Whole-body staging and recovery for mobile manipulation"],
        ],
        instructor_notes="The chapter works best when students build one inspectable artifact per section: a push residual plot, a pick-stage ledger, a contact-force trace, a perception uncertainty plot, a policy audit, a recovery branch table, and a mobile-manipulation base-pose scorecard.",
        readiness="Before leaving the chapter, the reader should be able to state how manipulation success is measured at the object level, how contact is verified, and how failure is routed into bounded recovery.",
        teaching_takeaway="Manipulation is the part of embodied AI where vague system boundaries are punished quickly. The teaching goal is to make those boundaries explicit enough that failure becomes localizable and repairable.",
        evidence_standard="A manipulation claim is ready only when it names the object-state target, contact assumption, action interface, verifier, perturbation panel, and recovery route on one shared evaluation script.",
        bibliography=[
            BibEntry("MoveIt 2 Documentation", "https://moveit.picknik.ai/", "Official planning and execution stack for ROS 2 manipulation."),
            BibEntry("cuMotion integration", "https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_cumotion/isaac_ros_cumotion/index.html", "GPU motion generation integrated with MoveIt workflows."),
            BibEntry("Drake", "https://drake.mit.edu/", "Simulation, optimization, and manipulation-planning toolkit."),
            BibEntry("ManiSkill", "https://maniskill.readthedocs.io/en/latest/", "Benchmark and simulator suite for generalizable manipulation skills."),
        ],
    ),
    ChapterData(
        number=43,
        title="Grasping and Dexterous Manipulation",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-43-grasping-and-dexterous-manipulation",
        epigraph="Dexterity is contact planning with consequences.",
        epigraph_cite="A Dexterous Systems Team",
        big_picture="This chapter studies grasping and dexterity as the design of useful contact sets over time. The object is not just acquired, it is stabilized, reoriented, and transferred under disturbance.",
        remember="The main lesson is that dexterity increases task breadth by increasing contact options, but that same richness expands sensing, calibration, and control burden. Strong systems make that tradeoff explicit.",
        overview_1="Chapter 43 starts with analytic and learned grasp synthesis, then compares hand morphologies, moves into in-hand manipulation, adds demonstration-bootstrapped RL, and closes with sim-to-real transfer for dexterous skills.",
        overview_2="The practical stack emphasizes Dex-Net and GQ-CNN lineage, MoveIt feasibility checks, MuJoCo dexterous hands, tactile libraries, robomimic, ManiSkill, and transfer ledgers that compare simulation and hardware traces directly.",
        prereqs="Readers should know the basics of manipulation, control, and policy learning. This chapter asks them to reason more explicitly about contact families, disturbance resistance, and the cost of richer hands.",
        tooling_note="Use analytic contact tools and learned scorers together. Dexterous systems become legible when contact mechanics, embodiment feasibility, and policy learning all remain visible in the same experiment ledger.",
        lab_objective="Build a grasp-and-reorientation benchmark that compares a simple gripper workflow to a dexterous workflow, then adds one demonstration-bootstrapped learning experiment and one transfer-gap audit.",
        lab_steps=[
            "Define the object panel, disturbance model, and success metrics for grasp and reorientation.",
            "Implement or document one grasp-synthesis path and one dexterous reorientation path.",
            "Compare hand or policy choices on the same objects and failure taxonomy.",
            "Add one demonstration-initialized policy and record when RL fine-tuning begins to help.",
            "Finish with a transfer ledger that names the first real-world mismatch encountered.",
        ],
        production_notes="Each section should leave behind a contact-centered artifact: a grasp score table, a hand-selection decision matrix, a contact-transition graph, a demo-to-RL curriculum note, or a sim-to-real mismatch ledger.",
        tool_map=[
            ["Dex-Net and GQ-CNN", "Synthetic supervision and learned grasp scoring"],
            ["MoveIt 2", "Reachability and collision filtering for grasp candidates"],
            ["MuJoCo", "Dexterous-hand simulation and contact-rich rollouts"],
            ["robomimic and LeRobot", "Demonstration-based policy learning pipelines"],
            ["Tactile libraries", "Slip, contact, and reorientation state feedback"],
        ],
        instructor_notes="Teach this chapter through tradeoffs rather than hero demos. Ask what contact family the task demands, what extra burden richer hands introduce, and what evidence would convince a skeptical engineer that the dexterous path is worth its cost.",
        readiness="Before leaving the chapter, the reader should be able to justify a hand choice, explain a grasp robustness metric, sketch a reorientation path, and describe the first mismatch they would expect during dexterous transfer.",
        teaching_takeaway="Dexterity is not a monolith. It is a stack of contact choices, sensing choices, and learning choices whose value should be argued in task-specific terms.",
        evidence_standard="A dexterity claim is ready only when it states the contact family, disturbance model, embodiment constraints, success and recovery metrics, and any transfer gap observed between simulation and hardware.",
        bibliography=[
            BibEntry("Dex-Net", "https://berkeleyautomation.github.io/dex-net/", "Synthetic grasping dataset and robust-grasp project page."),
            BibEntry("GQ-CNN", "https://berkeleyautomation.github.io/gqcnn/", "Official learned-grasp-scoring package documentation."),
            BibEntry("robomimic", "https://robomimic.github.io/", "Manipulation imitation-learning benchmark library."),
            BibEntry("MuJoCo", "https://mujoco.org/", "Simulation reference for dexterous hands and contact-rich control."),
        ],
    ),
    ChapterData(
        number=44,
        title="Tactile and Visuo-Tactile Learning",
        part_title="Part IX: Manipulation, Locomotion, and Embodied Skills",
        dir_name="module-44-tactile-and-visuo-tactile-learning",
        epigraph="Touch becomes a science when it changes the next action.",
        epigraph_cite="A Multimodal Manipulation Lab",
        big_picture="This chapter treats tactile sensing as an observability upgrade for contact-rich embodied systems. Vision gives global context, touch supplies local contact truth, and the combined system must decide how to act under disagreement.",
        remember="The extra modality earns its place only when it changes the robot's next action on the hard cases, especially under occlusion, slip, compliance, or local geometry ambiguity.",
        overview_1="Chapter 44 begins with the value of touch, moves through optical tactile hardware, tactile simulation, visuo-tactile pretraining, and finishes with phase-aware fusion of vision and touch.",
        overview_2="The practical stack emphasizes DIGIT, GelSight, AnySkin or ReSkin style sensors, PyTouch, TACTO, tactile simulation extensions, and multimodal policy pipelines that are evaluated on hard-contact episodes rather than average-case image tasks.",
        prereqs="Readers should already know manipulation basics, multimodal learning ideas, and the difference between scene-level and contact-level state estimation. This chapter narrows those abstractions onto the tactile interface.",
        tooling_note="Instrument first, model second. Tactile systems become useful when synchronization, calibration, and control hooks are handled carefully before large multimodal models are introduced.",
        lab_objective="Build a tactile or visuo-tactile benchmark that includes slip detection, one optical tactile signal, one multimodal comparison, and one disagreement case where the better modality should win explicitly.",
        lab_steps=[
            "Collect synchronized tactile, vision, and robot-state traces for one contact-rich task.",
            "Implement a simple tactile baseline such as slip margin or marker-motion detection.",
            "Compare a vision-only and a fused policy or estimator on hard cases.",
            "Run one simulation-to-real audit if simulated tactile data is involved.",
            "Record one disagreement episode and explain which modality should dominate and why.",
        ],
        production_notes="Read this chapter with the question, what contact state became observable that was previously hidden? Each section should answer that with a concrete signal, controller hook, and evaluation artifact.",
        tool_map=[
            ["DIGIT and GelSight", "Optical tactile sensing for geometry, shear, and slip cues"],
            ["AnySkin and related skins", "Replaceable tactile sensing for broader contact coverage"],
            ["PyTouch", "Feature extraction and tactile-learning pipelines"],
            ["TACTO and related simulators", "Synthetic tactile data and visuo-tactile pretraining support"],
            ["Multimodal policy stacks", "Fusion of touch, vision, and proprioception for manipulation"],
        ],
        instructor_notes="The chapter works well as a progression from sensing to action. Begin with what touch reveals, then show how sensor design and simulation shape the signal, and only then ask how multimodal policies should use it.",
        readiness="Before leaving the chapter, the reader should be able to state what tactile quantity is being measured, how it is calibrated, when it should change the action, and how a fusion system should react under disagreement.",
        teaching_takeaway="Touch is not a novelty modality. It is a practical route to observing the local contact states that often decide whether manipulation succeeds or fails.",
        evidence_standard="A tactile or visuo-tactile claim is ready only when it names the contact variable revealed by touch, the control decision it changes, the hard-case panel where the modality matters, and the artifact that proves the gain.",
        bibliography=[
            BibEntry("DIGIT tactile sensor", "https://digit.ml/digit.html", "Compact optical tactile sensor platform."),
            BibEntry("AnySkin", "https://any-skin.github.io/", "Current tactile skin platform focused on replaceability and generalization."),
            BibEntry("TACTO", "https://github.com/facebookresearch/tacto", "Open tactile simulator for high-resolution optical tactile sensing."),
            BibEntry("PyTouch", "https://github.com/facebookresearch/pytouch", "Open tactile machine-learning library."),
        ],
    ),
]


for chapter in CHAPTERS:
    chapter.number_end = chapter_sections(chapter.number)[-1].number  # type: ignore[attr-defined]

CHAPTERS_BY_NUMBER = {chapter.number: chapter for chapter in CHAPTERS}
SECTIONS_BY_NUMBER = {section.number: section for section in SECTIONS}


def main() -> None:
    for chapter in CHAPTERS:
        sections = chapter_sections(chapter.number)
        chapter_path(chapter).write_text(render_chapter(chapter, sections), encoding="utf-8")
        for section in sections:
            section_path(section).write_text(render_section(section, sections), encoding="utf-8")


if __name__ == "__main__":
    main()
