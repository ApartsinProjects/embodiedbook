import html
import re
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "building_embodied_ai_book_plan.md"

BOOK_TITLE = "Building Embodied AI"
BOOK_SUBTITLE = "From Perception to Autonomous Action"
FULL_TITLE = f"{BOOK_TITLE}: {BOOK_SUBTITLE}"
AUTHORS = "Alexander Apartsin &amp; Yehudit Aperstein"
YEAR = "2026"

FRONT_MATTER = [
    ("foreword", "Foreword", "F1"),
    ("about-authors", "About the Authors", "F2"),
    ("about-the-series", "About the Hands-On AI Science Series", "F3"),
    ("fm-who-should-read", "Who Should Read This Book", "F4"),
    ("fm-how-to-use", "How to Use This Book", "F5"),
    ("fm-what-this-book-covers", "What This Book Covers", "F6"),
    ("look-inside-preview", "Look Inside Preview", "F7"),
    ("copyright", "Copyright and Legal", "F8"),
]

APPENDICES = [
    ("appendix-a-linear-algebra-3d-geometry", "A", "Linear Algebra and 3D Geometry Refresher"),
    ("appendix-b-probability-estimation-optimization", "B", "Probability, Estimation, and Optimization Refresher"),
    ("appendix-c-embodied-ai-toolbox", "C", "The Embodied AI Toolbox"),
    ("appendix-d-pytorch-jax", "D", "PyTorch and JAX for Embodied AI"),
    ("appendix-e-compute-recipes", "E", "Compute Recipes"),
    ("appendix-f-datasets-benchmarks", "F", "Datasets and Benchmarks Catalog"),
    ("appendix-g-reproducibility", "G", "Reproducibility and Experiment Hygiene"),
    ("appendix-h-notation-glossary", "H", "Notation and Glossary"),
    ("appendix-i-citing-frontier", "I", "Citing the Frontier"),
]

PART_SUMMARIES = {
    "Foundations of Embodied AI": "the conceptual vocabulary of agents, environments, embodiment, and closed-loop intelligence",
    "Mathematical, Robotics, and Control Foundations": "the geometry, kinematics, dynamics, control, and sensing that make physical agents intelligible",
    "Simulation, Tooling, and the Modern Stack": "the simulators, environments, benchmarks, and synthetic-data practices used to build embodied systems today",
    "Reinforcement Learning for Embodied Agents": "interaction-driven learning, from policy gradients and off-policy methods to safe exploration and sim-to-real transfer",
    "Imitation Learning, Demonstrations, and Robot Data": "learning from demonstrations, teleoperation, action chunking, robot datasets, and data scaling",
    "Embodied Perception": "vision, 3D understanding, localization, mapping, and navigation as perception for action",
    "Language, Vision, and Action": "language-guided agents, VLMs, LLM planners, VLAs, and cross-embodiment foundation models",
    "World Models and Model-Based Embodied AI": "prediction, latent dynamics, model-based control, generative worlds, and diffusion planning",
    "Manipulation, Locomotion, and Embodied Skills": "hands, legs, humanoids, drones, vehicles, and the skills that let agents move through the world",
    "Multi-Agent and Human-Centered Embodiment": "teams of agents, humans in the loop, open worlds, and lifelong interaction",
    "Evaluation, Safety, Robustness, and Deployment": "metrics, uncertainty, safety filters, deployment architecture, and operational discipline",
    "Frontiers, Capstones, and Course Design": "memory, continual learning, open problems, capstone projects, and teaching paths",
}

TOOL_HINTS = {
    "simulation": "MuJoCo, MJX, Isaac Lab, Genesis, Newton, Drake, ROS 2, and modern Gazebo",
    "reinforcement": "Gymnasium, CleanRL, Stable-Baselines3, Tianshou, SKRL, RSL-RL, and rl_games",
    "imitation": "LeRobot, robomimic, ACT, Diffusion Policy, VQ-BeT, ALOHA, GELLO, and UMI",
    "vision": "OpenCV, PyTorch, Detectron2, Ultralytics, Segment Anything, DINOv2, SigLIP, and Gaussian Splatting tools",
    "language": "Hugging Face Transformers, open VLMs, OpenVLA, openpi, LeRobot, and tool-calling planners",
    "world": "Dreamer-style world models, TD-MPC style planners, JEPA encoders, diffusion planners, and NVIDIA Cosmos style workflows",
    "safety": "control barrier functions, reachability tools, runtime monitors, structured logging, and evaluation dashboards",
}

KEY_REFERENCES = [
    ("Sutton, R. S., and Barto, A. G.", "Reinforcement Learning: An Introduction", "2018", "http://incompleteideas.net/book/the-book-2nd.html", "A foundation for value functions, policy gradients, exploration, and the RL framing used throughout the book."),
    ("Todorov, E., Erez, T., and Tassa, Y.", "MuJoCo: A physics engine for model-based control", "2012", "https://mujoco.org/", "The simulator lineage behind much modern robot learning, now extended through MJX and Warp workflows."),
    ("Brohan, A. et al.", "RT-1: Robotics Transformer for real-world control at scale", "2022", "https://arxiv.org/abs/2212.06817", "A landmark in large-scale robot policy learning with transformer policies."),
    ("Brohan, A. et al.", "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", "2023", "https://arxiv.org/abs/2307.15818", "A central reference for connecting web-scale VLM knowledge to robot actions."),
    ("Open X-Embodiment Collaboration", "Open X-Embodiment: Robotic Learning Datasets and RT-X Models", "2023", "https://arxiv.org/abs/2310.08864", "The cross-embodiment data and transfer reference used by the data chapters."),
    ("Chi, C. et al.", "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion", "2023", "https://arxiv.org/abs/2303.04137", "The practical diffusion policy reference for imitation learning and continuous action generation."),
    ("Hafner, D. et al.", "Mastering Diverse Domains through World Models", "2023", "https://arxiv.org/abs/2301.04104", "DreamerV3, a modern reference for latent world models and imagination-based control."),
    ("Hugging Face", "LeRobot", "2024", "https://github.com/huggingface/lerobot", "The open robot-learning stack used for datasets, policies, demos, and low-cost embodied AI workflows."),
]


def esc(text):
    return html.escape(clean_text(str(text)), quote=True)


def clean_text(text):
    replacements = {
        "\u2014": ":",
        "\u2013": "-",
        "honestly": "rigorously",
        "Honestly": "Rigorously",
        "frankly": "plainly",
        "Frankly": "Plainly",
        "candidly": "directly",
        "Candidly": "Directly",
        "to be honest": "in practice",
        "To be honest": "In practice",
        "in truth": "in practice",
        "In truth": "In practice",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def slugify(text):
    text = text.lower()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def roman(n):
    vals = [
        (12, "XII"), (11, "XI"), (10, "X"), (9, "IX"), (8, "VIII"), (7, "VII"),
        (6, "VI"), (5, "V"), (4, "IV"), (3, "III"), (2, "II"), (1, "I")
    ]
    for value, label in vals:
        if n == value:
            return label
    return str(n)


def read_plan():
    text = PLAN.read_text(encoding="utf-8")
    parts = []
    current_part = None
    current_chapter = None
    for raw in text.splitlines():
        line = raw.strip()
        part_match = re.match(r"^# Part ([IVX]+) . (.+)$", line)
        if part_match:
            current_part = {
                "roman": part_match.group(1),
                "number": len(parts) + 1,
                "title": clean_text(part_match.group(2).strip()),
                "chapters": [],
            }
            parts.append(current_part)
            current_chapter = None
            continue
        chapter_match = re.match(r"^## Chapter (\d+) . (.+)$", line)
        if chapter_match and current_part:
            current_chapter = {
                "number": int(chapter_match.group(1)),
                "title": clean_text(chapter_match.group(2).strip()),
                "sections": [],
                "demo": "",
                "assignment": "",
            }
            current_part["chapters"].append(current_chapter)
            continue
        section_match = re.match(r"^(\d+)\.(\d+) (.+)$", line)
        if section_match and current_chapter:
            current_chapter["sections"].append({
                "num": f"{section_match.group(1)}.{section_match.group(2)}",
                "title": clean_text(section_match.group(3).strip()),
            })
            continue
        if line.startswith("- **Demo:**") and current_chapter:
            current_chapter["demo"] = line.replace("- **Demo:**", "").strip()
        elif line.startswith("- **Frontier Watch:**") and current_chapter:
            current_chapter["sections"].append({
                "num": f"{current_chapter['number']}.99",
                "title": "Frontier Watch",
            })
    for part in parts:
        part["slug"] = f"part-{part['number']}-{slugify(part['title'])}"
        for chapter in part["chapters"]:
            chapter["slug"] = f"module-{chapter['number']:02d}-{slugify(chapter['title'])}"
            if not chapter["sections"]:
                chapter["sections"] = default_sections(chapter)
    return parts


def default_sections(chapter):
    n = chapter["number"]
    return [
        {"num": f"{n}.1", "title": "Core idea and motivation"},
        {"num": f"{n}.2", "title": "Theory and formal model"},
        {"num": f"{n}.3", "title": "Practical implementation recipe"},
        {"num": f"{n}.4", "title": "Evaluation, failure modes, and extensions"},
    ]


def page_head(title, rel, desc, code=True, math=True):
    prism = ""
    if code:
        prism = f"""
<link href="{rel}styles/pygments.css" rel="stylesheet"/>
<link href="{rel}vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer="" src="{rel}vendor/prism/prism-bundle.min.js"></script>"""
    katex = ""
    if math:
        katex = f"""
<link href="{rel}vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer="" src="{rel}vendor/katex/katex.min.js"></script>
<script defer="" onload="renderMathInElement(document.body, {{
  delimiters: [
  {{left: '$$', right: '$$', display: true}},
  {{left: '$', right: '$', display: false}}
  ],
  throwOnError: false
  }});" src="{rel}vendor/katex/contrib/auto-render.min.js"></script>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="{esc(desc)}" name="description"/>
<title>{esc(title)} | {FULL_TITLE}</title>
<link href="{rel}styles/book.css" rel="stylesheet"/>{prism}{katex}
<script defer="" src="{rel}scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
"""


def header(rel, part_label, chapter_label, h1, part_href=None, chapter_href=None):
    part = esc(part_label)
    chapter = esc(chapter_label)
    if part_href:
        part = f'<a href="{part_href}">{part}</a>'
    if chapter_href:
        chapter = f'<a href="{chapter_href}">{chapter}</a>'
    return f"""<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="{rel}index.html">{FULL_TITLE}</a>
<a class="toc-link" href="{rel}toc.html" title="Table of Contents"><span class="toc-icon">&#9776;</span> Contents</a>
</nav>
<div class="header-search"><div id="search"></div></div>
<div class="part-label">{part}</div>
<div class="chapter-label">{chapter}</div>
<h1>{esc(h1)}</h1>
</header>
<main class="content" id="main-content">
"""


def footer(rel):
    return f"""<footer>
<p class="footer-title">{FULL_TITLE}, Web Edition</p>
<p>&#169; {YEAR} {AUTHORS} &#183; <a href="{rel}toc.html">Contents</a></p>
<p class="footer-updated">Last updated: <script>document.write(new Date(document.lastModified).toLocaleDateString('en-US', {{year:'numeric', month:'long', day:'numeric'}}))</script></p>
</footer>
</main>
</body>
</html>
"""


def callout(kind, title, body):
    return f"""<div class="callout {kind}">
<div class="callout-title">{esc(title)}</div>
{body}
</div>
"""


def bibliography(rel, focus):
    cards = []
    for author, title, year, url, note in KEY_REFERENCES:
        cards.append(f"""<div class="bib-entry-card">
<p class="bib-ref">{esc(author)}. "{esc(title)}." ({esc(year)}). <a href="{esc(url)}" target="_blank" rel="noopener">{esc(url)}</a></p>
<p class="bib-annotation">{esc(note)}</p>
</div>""")
    cards.append(f"""<div class="bib-entry-card">
<p class="bib-ref">Official documentation and source repositories for {esc(focus)}.</p>
<p class="bib-annotation">Use official docs for install commands, current APIs, and version caveats before running the chapter lab.</p>
</div>""")
    return f"""<section class="bibliography">
<h2>Bibliography &amp; Further Reading</h2>
<h3>Foundational Papers, Tools, and References</h3>
{''.join(cards)}
</section>
"""


def topic_kind(title):
    low = title.lower()
    if any(w in low for w in ["simulation", "simulator", "mujoco", "isaac", "benchmark", "domain"]):
        return "simulation"
    if any(w in low for w in ["reinforcement", "policy", "ppo", "reward", "exploration", "rl"]):
        return "reinforcement"
    if any(w in low for w in ["imitation", "teleoperation", "dataset", "offline", "action chunking", "diffusion policy"]):
        return "imitation"
    if any(w in low for w in ["vision", "perception", "slam", "mapping", "navigation", "3d"]):
        return "vision"
    if any(w in low for w in ["language", "vla", "vision-language", "llm", "foundation"]):
        return "language"
    if any(w in low for w in ["world", "model-based", "latent", "generative", "jepa", "diffusion"]):
        return "world"
    if any(w in low for w in ["safety", "robustness", "deployment", "evaluating", "uncertainty"]):
        return "safety"
    return "simulation"


def chapter_paths(parts):
    chapters = []
    for part in parts:
        for chapter in part["chapters"]:
            chapters.append((part, chapter))
    return chapters


def nav_links(current, all_chapters, rel):
    idx = all_chapters.index(current)
    prev_link = '<span class="prev">Start</span>'
    next_link = '<span class="next">End</span>'
    if idx > 0:
        p, c = all_chapters[idx - 1]
        prev_link = f'<a class="prev" href="{rel}{p["slug"]}/{c["slug"]}/index.html">&#8592; Chapter {c["number"]}: {esc(c["title"])}</a>'
    if idx + 1 < len(all_chapters):
        p, c = all_chapters[idx + 1]
        next_link = f'<a class="next" href="{rel}{p["slug"]}/{c["slug"]}/index.html">Chapter {c["number"]}: {esc(c["title"])} &#8594;</a>'
    return prev_link, next_link


def section_filename(section):
    return f"section-{section['num']}.html"


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def clean_output(parts):
    keep = {"archive", "styles", "templates", "vendor", "scripts", "pagefind", "images"}
    for item in ROOT.iterdir():
        if item.name in keep or item.name.endswith(".md"):
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    for part in parts:
        target = ROOT / part["slug"]
        if target.exists():
            shutil.rmtree(target)
    for folder in ["front-matter", "appendices", "capstone"]:
        target = ROOT / folder
        if target.exists():
            shutil.rmtree(target)


def create_cover_image():
    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    out = images_dir / "book-cover.jpg"
    w, h = 1600, 2560
    img = Image.new("RGB", (w, h), (6, 12, 20))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        ratio = y / h
        r = int(8 + 20 * ratio)
        g = int(16 + 34 * ratio)
        b = int(28 + 52 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    for x in range(0, w, 80):
        draw.line([(x, 0), (x, h)], fill=(22, 50, 78), width=1)
    for y in range(0, h, 80):
        draw.line([(0, y), (w, y)], fill=(22, 50, 78), width=1)
    for i in range(16):
        cx = 160 + i * 88
        cy = 860 + int(160 * ((i % 5) - 2) / 2)
        draw.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), fill=(116, 208, 212))
        if i > 0:
            px = 160 + (i - 1) * 88
            py = 860 + int(160 * (((i - 1) % 5) - 2) / 2)
            draw.line([(px, py), (cx, cy)], fill=(120, 180, 226), width=5)
    robot = [(610, 1090), (990, 1090), (1090, 1320), (960, 1600), (640, 1600), (510, 1320)]
    draw.polygon(robot, outline=(235, 194, 122), fill=(18, 42, 62))
    draw.rounded_rectangle((660, 1160, 940, 1340), radius=36, outline=(124, 210, 236), width=8, fill=(12, 28, 44))
    draw.ellipse((700, 1210, 760, 1270), fill=(124, 210, 236))
    draw.ellipse((840, 1210, 900, 1270), fill=(124, 210, 236))
    draw.line([(610, 1360), (410, 1480), (330, 1660)], fill=(235, 194, 122), width=14)
    draw.line([(990, 1360), (1190, 1480), (1270, 1660)], fill=(235, 194, 122), width=14)
    draw.line([(705, 1600), (640, 1880), (560, 2140)], fill=(124, 210, 236), width=18)
    draw.line([(895, 1600), (960, 1880), (1040, 2140)], fill=(124, 210, 236), width=18)
    try:
        title_font = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 112)
        arc_font = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 60)
        small_font = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 44)
    except OSError:
        title_font = arc_font = small_font = ImageFont.load_default()
    draw.text((120, 210), "Building", font=arc_font, fill=(226, 238, 246))
    draw.text((120, 290), "Embodied AI", font=title_font, fill=(238, 246, 252))
    draw.text((120, 445), "From Perception", font=arc_font, fill=(124, 210, 236))
    draw.text((120, 525), "to Autonomous Action", font=arc_font, fill=(235, 194, 122))
    draw.text((120, 2320), "Hands-On AI Science", font=small_font, fill=(206, 220, 232))
    draw.text((120, 2385), "Apartsin and Aperstein", font=small_font, fill=(165, 184, 202))
    img.save(out, quality=92)


def part_intro(part):
    return PART_SUMMARIES.get(part["title"], "a coherent segment of the embodied AI stack")


def write_index(parts):
    create_cover_image()
    part_cards = []
    total_chapters = sum(len(p["chapters"]) for p in parts)
    total_sections = sum(len(c["sections"]) for p in parts for c in p["chapters"])
    for idx, part in enumerate(parts, start=1):
        sec_count = sum(len(c["sections"]) for c in part["chapters"])
        part_cards.append(f"""<a class="part-card part-{((idx - 1) % 4) + 1}" href="{part['slug']}/index.html">
<span class="part-roman">{esc(part['roman'])}</span>
<h3>{esc(part['title'])}</h3>
<p>{esc(part_intro(part).capitalize())}.</p>
<span class="part-count">{len(part['chapters'])} chapters &#183; {sec_count} sections</span>
</a>""")
    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="{FULL_TITLE}. A hands-on science guide to robotics, simulation, world models, robot learning, and autonomous agents." name="description"/>
<title>{FULL_TITLE}</title>
<meta content="{FULL_TITLE}" property="og:title"/>
<meta content="A hands-on science guide to embodied AI, robotics, simulation, world models, robot learning, and autonomous action." property="og:description"/>
<meta content="images/book-cover.jpg" property="og:image"/>
<meta content="book" property="og:type"/>
<meta content="summary_large_image" name="twitter:card"/>
<link href="styles/book.css" rel="stylesheet"/>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap');
body.cover-page {{ margin: 0; padding: 0; min-height: 100vh; background: radial-gradient(ellipse at 30% 15%, #122338 0%, #0b1626 45%, #070d18 100%); color: #dce5ee; font-family: 'Cormorant Garamond', Georgia, serif; line-height: 1.6; overflow-x: hidden; }}
body.cover-page::before {{ content: ''; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, rgba(120, 170, 220, 0.035) 0, rgba(120, 170, 220, 0.035) 1px, transparent 1px, transparent 48px), repeating-linear-gradient(90deg, rgba(120, 170, 220, 0.035) 0, rgba(120, 170, 220, 0.035) 1px, transparent 1px, transparent 48px), radial-gradient(ellipse at center, transparent 40%, rgba(5, 9, 16, 0.65) 100%); pointer-events: none; z-index: 1; }}
body.cover-page .cover-wrap {{ position: relative; z-index: 2; max-width: 1060px; margin: 0 auto; padding: 0 1.5rem; }}
body.cover-page .cover-image-wrapper {{ margin: 0 auto 1.4rem; }}
body.cover-page .cover-image {{ max-width: 280px; width: 100%; height: auto; border-radius: 10px; box-shadow: 0 18px 48px rgba(0,0,0,0.45); border: 1px solid rgba(255,255,255,0.15); display: block; margin: 0 auto; }}
@media (max-width: 600px) {{ body.cover-page .cover-image {{ max-width: 200px; }} }}
body.cover-page .hero {{ min-height: 88vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 4rem 0 3rem; animation: coverFadeIn 0.9s ease-out both; }}
@keyframes coverFadeIn {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
@media (prefers-reduced-motion: reduce) {{ body.cover-page .hero, body.cover-page .part-card {{ animation: none !important; transition: none !important; }} }}
body.cover-page .edition-pill {{ font-family: 'Cinzel', Georgia, serif; font-size: clamp(0.66rem, 1.4vw, 0.8rem); font-weight: 500; text-transform: uppercase; letter-spacing: 0.28em; color: rgba(150, 200, 235, 0.75); border: 1px solid rgba(150, 200, 235, 0.22); border-radius: 100px; padding: 0.4rem 1.3rem; margin-bottom: 1.6rem; display: inline-block; }}
body.cover-page .cover-title {{ font-family: 'Cinzel', Georgia, serif; font-weight: 700; font-size: clamp(2.1rem, 5.2vw, 3.4rem); line-height: 1.18; color: #e9f1f8; letter-spacing: 0.02em; margin: 0 0 0.55rem; text-shadow: 0 0 36px rgba(110, 180, 235, 0.22), 0 2px 4px rgba(0, 0, 0, 0.45); }}
body.cover-page .cover-title .title-arc {{ display: block; font-size: clamp(1.15rem, 2.9vw, 1.85rem); font-weight: 500; margin-top: 0.45rem; background: linear-gradient(90deg, #6fc6e8 0%, #9fb6f0 35%, #d99ad0 70%, #f0c27a 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: #9fb6f0; }}
body.cover-page .cover-subtitle {{ font-size: clamp(1.18rem, 2.7vw, 1.58rem); font-weight: 500; color: rgba(229, 238, 246, 0.94); max-width: 660px; margin: 1.1rem auto 0; line-height: 1.5; letter-spacing: 0.01em; }}
body.cover-page .cover-separator {{ margin: 1.6rem auto 1.1rem; display: flex; align-items: center; justify-content: center; gap: 1rem; width: 220px; }}
body.cover-page .cover-separator::before, body.cover-page .cover-separator::after {{ content: ''; flex: 1; height: 1px; background: linear-gradient(90deg, transparent, rgba(150, 200, 235, 0.4), transparent); }}
body.cover-page .cover-separator span {{ color: rgba(150, 200, 235, 0.6); font-size: 0.8rem; line-height: 1; }}
body.cover-page .cover-authors {{ margin: 0 auto; font-size: clamp(1rem, 2vw, 1.2rem); color: rgba(220, 229, 238, 0.72); letter-spacing: 0.02em; }}
body.cover-page .cover-authors a {{ color: rgba(229, 238, 246, 0.9); text-decoration: none; border-bottom: 1px solid rgba(150, 200, 235, 0.3); transition: color 0.25s, border-color 0.25s; }}
body.cover-page .cover-authors a:hover {{ color: #7fd0ec; border-bottom-color: rgba(150, 200, 235, 0.6); }}
body.cover-page .cover-authors .amp {{ margin: 0 0.5rem; opacity: 0.45; }}
body.cover-page .cover-promise {{ font-size: clamp(1.04rem, 2vw, 1.22rem); color: rgba(220, 229, 238, 0.88); max-width: 680px; margin: 1.7rem auto 0; line-height: 1.75; }}
body.cover-page .cover-cta {{ display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 2.3rem; }}
body.cover-page .btn-start, body.cover-page .btn-contents, body.cover-page .btn-amazon {{ font-family: 'Cinzel', Georgia, serif; font-size: 0.95rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none; border-radius: 8px; padding: 0.85rem 2.1rem; transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease, color 0.18s ease; }}
body.cover-page .btn-start {{ color: #081120; background: linear-gradient(120deg, #7fd0ec 0%, #b6c6f4 55%, #f0c27a 130%); box-shadow: 0 6px 26px rgba(110, 180, 235, 0.28); }}
body.cover-page .btn-start:hover, body.cover-page .btn-start:focus {{ transform: translateY(-2px); box-shadow: 0 10px 34px rgba(110, 180, 235, 0.4); color: #081120; }}
body.cover-page .btn-contents {{ color: rgba(220, 229, 238, 0.85); border: 1px solid rgba(150, 200, 235, 0.35); background: transparent; }}
body.cover-page .btn-contents:hover, body.cover-page .btn-contents:focus {{ color: #eaf3fa; border-color: rgba(150, 200, 235, 0.7); background: rgba(110, 180, 235, 0.08); }}
body.cover-page .btn-amazon {{ color: #2a1a05; background: linear-gradient(120deg, #f0c27a 0%, #e6a84e 100%); box-shadow: 0 6px 26px rgba(230, 168, 78, 0.28); }}
body.cover-page .cover-meta {{ display: flex; justify-content: center; gap: 1.6rem; flex-wrap: wrap; margin-top: 2.4rem; font-size: 0.92rem; color: rgba(220, 229, 238, 0.45); letter-spacing: 0.05em; }}
body.cover-page .cover-section-title {{ font-family: 'Cinzel', Georgia, serif; font-size: clamp(1.25rem, 2.6vw, 1.7rem); font-weight: 700; color: #dfeaf4; text-align: center; letter-spacing: 0.06em; margin: 0 0 0.4rem; }}
body.cover-page .cover-section-sub {{ text-align: center; font-style: italic; color: rgba(220, 229, 238, 0.55); font-size: 1.02rem; margin: 0 0 2rem; }}
body.cover-page .parts-section, body.cover-page .series-section, body.cover-page .teaches-section {{ padding: 3rem 0 1.5rem; }}
body.cover-page .part-grid, body.cover-page .teach-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1.1rem; }}
body.cover-page .part-card, body.cover-page .teach-item {{ display: flex; flex-direction: column; text-decoration: none; background: rgba(16, 30, 48, 0.72); border: 1px solid rgba(150, 200, 235, 0.14); border-radius: 12px; padding: 1.5rem 1.4rem 1.3rem; color: inherit; transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease; }}
body.cover-page .part-card:hover, body.cover-page .part-card:focus {{ transform: translateY(-4px); border-color: rgba(150, 200, 235, 0.5); box-shadow: 0 14px 36px rgba(0, 0, 0, 0.45); }}
body.cover-page .part-card .part-roman {{ font-family: 'Cinzel', Georgia, serif; font-size: 2rem; font-weight: 700; line-height: 1; color: #7fd0ec; margin-bottom: 0.55rem; }}
body.cover-page .part-card h3, body.cover-page .teach-item h3 {{ font-family: 'Cinzel', Georgia, serif; font-size: 1.06rem; font-weight: 700; color: #e9f1f8; margin: 0 0 0.55rem; line-height: 1.35; }}
body.cover-page .part-card p, body.cover-page .teach-item p {{ font-size: 0.99rem; color: rgba(220, 229, 238, 0.72); line-height: 1.55; margin: 0 0 1rem; flex-grow: 1; }}
body.cover-page .part-card .part-count, body.cover-page .series-here, body.cover-page .series-links {{ font-family: 'Cinzel', Georgia, serif; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(150, 200, 235, 0.8); }}
body.cover-page .part-card.part-1 .part-roman, body.cover-page .part-card.part-1 .part-count {{ color: #6fd0cd; }}
body.cover-page .part-card.part-2 .part-roman, body.cover-page .part-card.part-2 .part-count {{ color: #d9bd7a; }}
body.cover-page .part-card.part-3 .part-roman, body.cover-page .part-card.part-3 .part-count {{ color: #b3a2f5; }}
body.cover-page .part-card.part-4 .part-roman, body.cover-page .part-card.part-4 .part-count {{ color: #ef9eb4; }}
body.cover-page .teach-glyph {{ font-size: 1.25rem; line-height: 1; display: block; margin-bottom: 0.5rem; color: #7fd0ec; }}
body.cover-page footer.cover-footer {{ position: relative; z-index: 2; text-align: center; padding: 2.5rem 1.5rem 2.2rem; margin-top: 2rem; border-top: 1px solid rgba(150, 200, 235, 0.12); color: rgba(220, 229, 238, 0.45); font-size: 0.9rem; background: transparent; }}
body.cover-page footer.cover-footer p {{ margin: 0 0 0.3rem; text-align: center; }}
body.cover-page footer.cover-footer .footer-title {{ font-family: 'Cinzel', Georgia, serif; font-size: 0.82rem; letter-spacing: 0.1em; color: rgba(220, 229, 238, 0.55); }}
body.cover-page footer.cover-footer a, body.cover-page .series-links a, body.cover-page .series-cta a {{ color: rgba(150, 200, 235, 0.75); text-decoration: none; }}
</style>
<script defer="" src="scripts/book.js"></script>
<link href="pagefind/pagefind-ui.css" rel="stylesheet"/>
<script defer="" src="pagefind/pagefind-ui.js"></script>
</head>
<body class="cover-page">
<div class="cover-wrap">
<header class="hero">
<span class="edition-pill">Web Edition &#183; 2026</span>
<div class="cover-image-wrapper"><img alt="Book cover: a humanoid robot silhouette standing in a sensor grid, connected to perception, control, simulation, and world-model motifs, with the title Building Embodied AI" class="cover-image" height="2560" src="images/book-cover.jpg" width="1600"/></div>
<h1 class="cover-title">Building Embodied AI<span class="title-arc">From Perception to Autonomous Action</span></h1>
<p class="cover-subtitle">A practitioner's guide to embodied agents, robot learning, simulation, world models, and physical intelligence.</p>
<div aria-hidden="true" class="cover-separator"><span>&#10022;</span></div>
<p class="cover-authors"><a href="front-matter/about-authors.html">Alexander (Sasha) Apartsin, Ph.D.</a><span class="amp">&amp;</span><a href="front-matter/about-authors.html">Yehudit Aperstein, Ph.D.</a></p>
<p class="cover-promise">Embodied intelligence begins when an agent must act, observe the consequences, and adapt inside a changing world. This book is one connected journey through robotics, control, simulation, reinforcement learning, imitation learning, vision-language-action models, world models, humanoids, safety, and deployment.</p>
<nav aria-label="Primary" class="cover-cta">
<a class="btn-start" href="{parts[0]['slug']}/{parts[0]['chapters'][0]['slug']}/index.html">Start Reading</a>
<a class="btn-contents" href="toc.html">Contents</a>
<a class="btn-amazon" href="front-matter/about-the-series.html">About the Series</a>
</nav>
<div class="cover-meta"><span>{len(parts)} parts</span><span>{total_chapters} chapters</span><span>{total_sections} sections</span><span>{len(APPENDICES)} appendices</span></div>
</header>
<section aria-labelledby="parts-heading" class="parts-section">
<h2 class="cover-section-title" id="parts-heading">The Twelve-Part Arc</h2>
<p class="cover-section-sub">Each part adds one layer to the agent that senses, predicts, decides, acts, and learns.</p>
<div class="part-grid">{''.join(part_cards)}</div>
</section>
<section aria-labelledby="teaches-heading" class="teaches-section">
<h2 class="cover-section-title" id="teaches-heading">How This Book Teaches</h2>
<p class="cover-section-sub">Five habits, kept in every chapter from the first simulator to the final deployment.</p>
<div class="teach-grid">
<div class="teach-item"><span aria-hidden="true" class="teach-glyph">&#9881;</span><h3>Worked Systems</h3><p>Every chapter connects concepts to a runnable artifact, from a tiny environment to a robot-learning pipeline.</p></div>
<div class="teach-item"><span aria-hidden="true" class="teach-glyph">&#9889;</span><h3>Library Shortcuts</h3><p>After each from-scratch build, a shortcut names the maintained tool that makes the practical version small.</p></div>
<div class="teach-item"><span aria-hidden="true" class="teach-glyph">&#9998;</span><h3>A Callout System</h3><p>Failure modes, research frontiers, recipes, and cross-references are typeset as distinct boxes for fast scanning.</p></div>
<div class="teach-item"><span aria-hidden="true" class="teach-glyph">&#9654;</span><h3>Exercises And Labs</h3><p>Chapters close with build tasks that turn theory into testable systems.</p></div>
<div class="teach-item"><span aria-hidden="true" class="teach-glyph">&#8634;</span><h3>Classical Ideas Return Learned</h3><p>Geometry, control, estimation, and simulation reappear inside modern learned policies and world models.</p></div>
</div>
</section>
<section aria-labelledby="series-heading" class="series-section">
<h2 class="cover-section-title" id="series-heading">The Hands-On AI Science Series</h2>
<p class="cover-section-sub">Building Embodied AI is the fifth connected book in a deep, build-it-yourself AI series.</p>
<p class="cover-promise" style="margin-top:0;">Hands-On AI Science is a series of in-depth guides to the major fields of artificial intelligence. Every book goes deep into the theory, models, and internals, covers the classical foundations and the most recent ideas, then shows how to build each one in Python with modern libraries and tools.</p>
<div class="part-grid">
<div class="part-card series-card part-1"><h3>Building Language AI</h3><p>From Tokens to Agents.</p><span class="series-links"><a href="https://llmbook.apartsin.com" rel="noopener" target="_blank">Read online</a></span></div>
<div class="part-card series-card part-2"><h3>Building Vision AI</h3><p>From Pixels to Generative Models.</p><span class="series-links"><a href="https://visionbook.apartsin.com" rel="noopener" target="_blank">Read online</a></span></div>
<div class="part-card series-card part-3"><h3>Building Temporal AI</h3><p>From Forecasting to Sequential Decision Making.</p><span class="series-links"><a href="https://temporalbook.apartsin.com" rel="noopener" target="_blank">Read online</a></span></div>
<div class="part-card series-card part-4"><h3>Building Scalable AI</h3><p>From Big Data Algorithms to Distributed Intelligence.</p><span class="series-links"><a href="https://scalablebook.apartsin.com" rel="noopener" target="_blank">Read online</a></span></div>
<div class="part-card series-card part-1"><h3>Building Embodied AI</h3><p>From Perception to Autonomous Action.</p><span class="series-here">You are here</span></div>
</div>
<p class="series-cta">Read the full <a href="front-matter/about-the-series.html">About the Hands-On AI Science Series</a> note.</p>
</section>
</div>
<footer class="cover-footer">
<p class="footer-title">{FULL_TITLE}, Web Edition</p>
<p>&#169; {YEAR} {AUTHORS} &#183; <a href="toc.html">Contents</a></p>
</footer>
</body>
</html>
"""
    write(ROOT / "index.html", body)


def write_toc(parts):
    front_items = []
    for slug, title, label in FRONT_MATTER:
        front_items.append(f"""<li class="toc-chapter"><div class="toc-chapter-head"><span class="toc-chapter-num">{label}</span><div><a class="toc-card-link" href="front-matter/{slug}.html"><span class="toc-chapter-title">{esc(title)}</span></a><span class="toc-chapter-subtitle">Front matter for {FULL_TITLE}.</span></div></div><code class="toc-chapter-dir">front-matter/{slug}.html</code></li>""")
    part_sections = []
    for part in parts:
        chapter_items = []
        for chapter in part["chapters"]:
            section_items = []
            for section in chapter["sections"]:
                section_items.append(f"""<li><span class="toc-section-num">{esc(section["num"])}</span> <a class="toc-sec-link" href="{part["slug"]}/{chapter["slug"]}/{section_filename(section)}">{esc(section["title"])}</a></li>""")
            chapter_items.append(f"""<li class="toc-chapter">
<div class="toc-chapter-head"><span class="toc-chapter-num">{chapter["number"]}</span><div>
<a class="toc-card-link" href="{part["slug"]}/{chapter["slug"]}/index.html"><span class="toc-chapter-title">{esc(chapter["title"])}</span></a>
<span class="toc-chapter-subtitle">Theory, practical recipe, lab, and library shortcuts for this chapter.</span>
</div></div>
<ol class="toc-section-list">{''.join(section_items)}</ol>
<code class="toc-chapter-dir">{part["slug"]}/{chapter["slug"]}/</code>
</li>""")
        sec_count = sum(len(c["sections"]) for c in part["chapters"])
        part_sections.append(f"""<section class="toc-part" data-part-num="{part['number']}" id="part-{part['number']}">
<header class="toc-part-header">
<h2 class="toc-part-title"><span class="toc-part-prefix">Part {esc(part["roman"])}</span> <span class="toc-part-sep">&#183;</span> <a href="{part["slug"]}/index.html">{esc(part["title"])}</a></h2><span class="toc-part-count">{len(part["chapters"])} chapters &#183; {sec_count} sections</span>
<p class="toc-part-subtitle">{esc(part_intro(part).capitalize())}.</p>
</header>
<ol class="toc-chapter-list">{''.join(chapter_items)}</ol>
</section>""")
    appendix_items = []
    for slug, letter, title in APPENDICES:
        appendix_items.append(f"""<li class="toc-chapter"><div class="toc-chapter-head"><span class="toc-chapter-num">{letter}</span><div><a class="toc-card-link" href="appendices/{slug}/index.html"><span class="toc-chapter-title">{esc(title)}</span></a><span class="toc-chapter-subtitle">Reference material supporting the self-contained book promise.</span></div></div><code class="toc-chapter-dir">appendices/{slug}/</code></li>""")
    total_chapters = sum(len(p["chapters"]) for p in parts)
    total_sections = sum(len(c["sections"]) for p in parts for c in p["chapters"])
    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Detailed table of contents for {FULL_TITLE}." name="description"/>
<title>Contents | {FULL_TITLE}</title>
<link href="styles/book.css" rel="stylesheet"/>
<style>
.toc-draft-note {{ max-width: 1080px; margin: 1.25rem auto 0; padding: 0 1.5rem; font-family: sans-serif; font-size: 0.8rem; color: #5a626c; text-align: center; }}
.toc-main {{ max-width: 1080px; }}
.toc-chapter {{ padding: 0.65rem 0.75rem; }}
.toc-chapter-head {{ display: grid; grid-template-columns: 2rem 1fr; gap: 0 0.65rem; align-items: start; margin-bottom: 0.45rem; }}
.toc-chapter-head .toc-chapter-num {{ margin-top: 0.1rem; }}
.toc-chapter-subtitle {{ display: block; font-size: 0.78rem; font-style: italic; color: #5a626c; line-height: 1.4; margin-top: 0.15rem; }}
.toc-section-list {{ list-style: none; margin: 0 0 0.5rem 2.65rem; padding: 0; }}
.toc-section-list li {{ display: grid; grid-template-columns: 2.3rem 1fr; align-items: baseline; font-family: sans-serif; font-size: 0.78rem; color: #3c4451; line-height: 1.45; padding: 0.12rem 0; border-top: 1px dotted #e8ebf1; }}
.toc-section-list li:first-child {{ border-top: none; }}
.toc-section-num {{ font-weight: 700; color: #8a93a3; font-size: 0.72rem; }}
.toc-chapter-dir {{ display: none; margin-left: 2.65rem; font-family: Consolas, Menlo, monospace; font-size: 0.66rem; color: #9aa3b2; word-break: break-all; }}
.toc-card-link {{ color: inherit; text-decoration: none; }}
.toc-card-link:hover .toc-chapter-title {{ color: #e94560; }}
.toc-sec-link {{ color: inherit; text-decoration: none; border-bottom: 1px dotted #c3cad6; }}
.toc-sec-link:hover {{ color: #e94560; border-bottom-color: #e94560; }}
.toc-part-title a {{ color: #ffffff; text-decoration: none; border-bottom: 1px dotted rgba(255,255,255,0.5); }}
.toc-part-title a:hover {{ color: rgba(255,255,255,0.85); }}
</style>
<script defer="" src="scripts/book.js"></script>
<link href="pagefind/pagefind-ui.css" rel="stylesheet"/>
<script defer="" src="pagefind/pagefind-ui.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="index.html">{FULL_TITLE}</a>
<span aria-current="page" class="toc-link" title="Table of Contents"><span class="toc-icon">&#9776;</span> Contents</span>
</nav>
<div class="header-search"><div id="search"></div></div>
<h1>Table of Contents</h1>
<p class="chapter-subtitle">A hands-on science guide to embodied agents, robot learning, simulation, world models, and autonomous action.</p>
<p class="chapter-subtitle">Web Edition &#183; 2026</p>
</header>
<p class="toc-draft-note">{len(parts)} parts &#183; {total_chapters} chapters &#183; {total_sections} sections, plus front matter and {len(APPENDICES)} appendices. Every chapter and section linked below is generated and live.</p>
<main class="content toc-main" id="main-content">
<section class="toc-part toc-front-matter" id="front-matter">
<header class="toc-part-header"><h2 class="toc-part-title"><span class="toc-part-prefix">Front Matter</span> <span class="toc-part-sep">&#183;</span> <a href="front-matter/foreword.html">Opening Material</a></h2><span class="toc-part-count">{len(FRONT_MATTER)} entries</span></header>
<ol class="toc-chapter-list">{''.join(front_items)}</ol>
</section>
{''.join(part_sections)}
<section class="toc-part toc-appendices" id="appendices">
<header class="toc-part-header"><h2 class="toc-part-title"><span class="toc-part-prefix">Appendices</span> <span class="toc-part-sep">&#183;</span> <a href="appendices/index.html">Reference and Pedagogy</a></h2><span class="toc-part-count">{len(APPENDICES)} appendices</span></header>
<ol class="toc-chapter-list">{''.join(appendix_items)}</ol>
</section>
<footer><p>{FULL_TITLE} &#183; Web Edition, 2026</p></footer>
</main>
</body>
</html>
"""
    write(ROOT / "toc.html", body)


def front_text(slug, title):
    if slug == "about-the-series":
        return f"""<p><em>{BOOK_TITLE}</em> is part of <strong>Hands-On AI Science</strong>, a series that pairs serious depth with serious building.</p>
<p>Each book takes a major field of AI from first principles to the research frontier, then asks the reader to build. The series treats theory, models, internals, tooling, and engineering practice as one connected story.</p>
{callout("key-insight", "What Hands-On AI Science Promises", "<p>It is hands-on: every major idea becomes code. It is science: it explains why the method works and where it fails. It is AI: it moves from foundations to frontier systems without hiding the classical ideas underneath the modern tools.</p>")}
<p>Embodied AI is the volume where intelligence leaves the static dataset and enters a world. The reader meets geometry, control, simulation, robot learning, VLA policies, world models, humanoids, evaluation, and deployment as parts of one closed loop.</p>"""
    if slug == "fm-how-to-use":
        return """<p>The book can be read front to back, which is the strongest path, or by route. Engineers can begin with the setup chapter, simulation stack, and deployment chapters. Researchers can jump to VLA models, world models, humanoids, and evaluation after reading the foundations. Instructors can use the course design chapter and appendices to build an advanced undergraduate or graduate offering.</p>
<div class="callout pathway"><div class="callout-title">Reading Pathways</div><p>For a fast builder path, read Chapters 0, 1, 3, 9, 10, 11, 21, 22, 23, 34, 52, and 55. For a research path, read Chapters 4 to 8, 14 to 25, 34 to 41, 46, 52, 54, and 58.</p></div>"""
    if slug == "fm-what-this-book-covers":
        return """<p>The book covers embodied AI as a full stack: agent-environment interfaces, spatial math, kinematics, dynamics, control, sensors, simulation, RL, imitation learning, robot data, perception, language grounding, VLAs, world models, manipulation, locomotion, humanoids, multi-agent settings, human interaction, safety, robustness, deployment, memory, continual learning, capstones, and course design.</p>"""
    if slug == "fm-who-should-read":
        return """<p>This book is for advanced undergraduate students, graduate students, researchers, engineers, and instructors who want to build embodied systems rather than only read about them. It assumes Python and basic machine learning, then supplies the robotics, control, RL, and simulation background needed to continue.</p>"""
    if slug == "about-authors":
        return """<p>Alexander Apartsin and Yehudit Aperstein write the Hands-On AI Science books for readers who want both conceptual depth and working systems. This volume extends that approach to agents that perceive, act, and learn from consequences.</p>"""
    if slug == "copyright":
        return f"""<p>Copyright {YEAR} Alexander Apartsin and Yehudit Aperstein. All rights reserved.</p><p>This web edition is prepared as part of the Hands-On AI Science series.</p>"""
    if slug == "look-inside-preview":
        return """<p>Inside the book, each chapter combines a conceptual map, a theory section, a worked example, runnable code, a library shortcut, exercises, and a hands-on lab. The through line is always the same: build the mechanism, then use the right tool.</p>"""
    return """<p>Embodied AI begins when intelligence is measured by interaction. This book follows the loop from perception to action, and from simple simulated agents to modern robot foundation models.</p>"""


def write_front_matter():
    for index, (slug, title, label) in enumerate(FRONT_MATTER):
        rel = "../"
        prev_href = "../index.html" if index == 0 else f"{FRONT_MATTER[index - 1][0]}.html"
        next_href = "../toc.html" if index + 1 == len(FRONT_MATTER) else f"{FRONT_MATTER[index + 1][0]}.html"
        body = page_head(title, rel, f"{title} for {FULL_TITLE}.", code=False, math=False)
        body += header(rel, "Front Matter", f"{label} · {title}", title)
        body += front_text(slug, title)
        body += f"""<nav class="chapter-nav">
<a class="prev" href="{prev_href}">&#8592; Previous</a>
<a href="../toc.html">Contents</a>
<a class="next" href="{next_href}">Next &#8594;</a>
</nav>
"""
        body += footer(rel)
        write(ROOT / "front-matter" / f"{slug}.html", body)


def write_part_pages(parts):
    for i, part in enumerate(parts):
        rel = "../"
        cards = []
        for chapter in part["chapters"]:
            section_items = "".join(
                f'<li><span class="sec-num">{esc(s["num"])}</span> {esc(s["title"])}</li>'
                for s in chapter["sections"][:5]
            )
            cards.append(f"""<div class="chapter-card">
<div class="chapter-card-header"><a href="{chapter['slug']}/index.html"><span class="mod-num">Chapter {chapter['number']}</span> {esc(chapter['title'])}</a></div>
<div class="chapter-card-body"><p>This chapter develops {esc(chapter['title'].lower())} as part of the embodied AI stack.</p><ul class="section-list">{section_items}</ul></div>
</div>""")
        next_text = "the appendices consolidate tools and references"
        next_href = "../appendices/index.html"
        if i + 1 < len(parts):
            next_part = parts[i + 1]
            next_text = f"Part {next_part['roman']}: {next_part['title']} extends the stack"
            next_href = f"../{next_part['slug']}/index.html"
        body = page_head(f"Part {part['roman']}: {part['title']}", rel, f"Part {part['roman']} of {FULL_TITLE}.", code=False, math=False)
        body += header(rel, "Book Part", f"Part {part['roman']}", f"Part {part['roman']}: {part['title']}")
        body += f"""<div class="part-overview">
<h2>Part Overview</h2>
<p>This part covers {esc(part_intro(part))}. It connects formal ideas with the tools and labs needed to build working systems.</p>
<p>Chapters: {len(part['chapters'])}. Each chapter includes theory, recipes, practical code, a library shortcut, and exercises.</p>
</div>
{callout("big-picture", "Why This Part Matters", f"<p>{esc(part['title'])} gives the reader a working layer of the embodied AI stack. Later chapters assume this layer when agents must perceive, plan, act, and recover from mistakes.</p>")}
{''.join(cards)}
<div class="whats-next"><h3>What's Next?</h3><p>After this part, <a href="{next_href}">{esc(next_text)}</a>.</p></div>
<nav class="chapter-nav"><a class="prev" href="../toc.html">&#8592; Contents</a><a href="../index.html">Book Home</a><a class="next" href="{next_href}">Next &#8594;</a></nav>
"""
        body += footer(rel)
        write(ROOT / part["slug"] / "index.html", body)


def chapter_overview(chapter, part):
    kind = topic_kind(chapter["title"] + " " + part["title"])
    tools = TOOL_HINTS[kind]
    return f"""<p>Chapter {chapter['number']} develops <strong>{esc(chapter['title'])}</strong> as a working piece of the embodied AI stack. The chapter starts with the role this topic plays in the sense, represent, predict, decide, act, observe, and learn loop, then turns that role into a concrete implementation pattern.</p>
<p>The practical thread uses {esc(tools)} where appropriate, while the theory thread keeps the mechanism visible. The reader should leave with both a mental model and a build path.</p>"""


def write_chapter_pages(parts):
    all_chapters = chapter_paths(parts)
    for part, chapter in all_chapters:
        rel = "../../"
        part_href = "../index.html"
        chapter_dir = ROOT / part["slug"] / chapter["slug"]
        first_section = section_filename(chapter["sections"][0])
        prev_link, next_link = nav_links((part, chapter), all_chapters, rel)
        section_list = "".join(
            f"""<li><span class="section-num">{esc(s['num'])}</span> <a href="{section_filename(s)}"><span class="section-title">{esc(s['title'])}</span></a><span class="section-desc">Build the concept, inspect the assumptions, and connect it to tools and evaluation.</span></li>"""
            for s in chapter["sections"]
        )
        kind = topic_kind(chapter["title"] + " " + part["title"])
        tools = TOOL_HINTS[kind]
        body = page_head(f"Chapter {chapter['number']}: {chapter['title']}", rel, f"Chapter {chapter['number']} of {FULL_TITLE}: {chapter['title']}.")
        body += header(rel, f"Part {part['roman']}: {part['title']}", f"Chapter {chapter['number']}: {chapter['title']}", f"Chapter {chapter['number']}: {chapter['title']}", part_href, "index.html")
        body += f"""<blockquote class="epigraph">
<p>"An agent becomes interesting at the exact moment the world refuses to be a dataset."</p>
<cite>A Patient Embodied AI Agent</cite>
</blockquote>
{callout("big-picture", "Big Picture", f"<p><strong>{esc(chapter['title'])}</strong> matters because embodied intelligence is a closed loop. The agent must turn partial observations into useful state, choose actions under uncertainty, and learn from the consequences in a physical or simulated world.</p>")}
{callout("key-insight", "Remember This Chapter", f"<p>The core move is to connect {esc(chapter['title'].lower())} to action. A static model can be accurate and still be useless if it cannot support timely, safe, and recoverable behavior.</p>")}
<div class="overview">
<h2>Chapter Overview</h2>
{chapter_overview(chapter, part)}
</div>
<div class="prereqs"><h3>Prerequisites</h3><p>Readers should be comfortable with Python, tensors, and the perception-action loop. When the chapter uses geometry, control, or probability, the relevant appendices provide a compact refresher.</p></div>
<h2>Chapter Roadmap</h2>
<ul class="sections-list">{section_list}</ul>
{callout("library-shortcut", "Tooling Note", f"<p>This chapter uses the right-tool principle. Build the mechanism once, then reach for maintained tools such as {esc(tools)} when the task moves from learning exercise to working system.</p>")}
<section class="lab" id="lab-{chapter['number']}">
<h2>Hands-On Lab: Build the Chapter System</h2>
<div class="lab-meta"><span class="lab-duration">Duration: about 60 to 120 minutes</span><span class="lab-difficulty">Difficulty: Intermediate to Advanced</span></div>
<div class="lab-objective"><h3>Objective</h3><p>Turn the chapter concept into a small working artifact: define the interface, run a baseline, inspect failure modes, then replace the hand-built part with a library shortcut.</p></div>
<div class="lab-steps"><h3>Steps</h3><ol><li>Define observations, actions, state, and evaluation metrics.</li><li>Implement the smallest useful version from scratch.</li><li>Run the maintained library version and compare behavior.</li><li>Log success, failure, latency, and robustness.</li><li>Write a short postmortem explaining what changed between the simple version and the practical version.</li></ol></div>
</section>
<div class="whats-next"><h3>What's Next?</h3><p>Continue with <a href="{first_section}">Section {esc(chapter['sections'][0]['num'])}: {esc(chapter['sections'][0]['title'])}</a>, where the chapter moves from motivation to the first concrete idea.</p></div>
{bibliography(rel, chapter['title'])}
<nav class="chapter-nav">{prev_link}<a href="../index.html">Part {esc(part['roman'])}</a>{next_link}</nav>
"""
        body += footer(rel)
        write(chapter_dir / "index.html", body)
        write_section_pages(part, chapter, all_chapters)


def code_example(section, kind):
    label = slugify(section["title"]).replace("-", "_")[:30] or "embodied_step"
    if kind == "reinforcement":
        return f"""import gymnasium as gym

env = gym.make("CartPole-v1")
obs, info = env.reset(seed=7)
for step in range(5):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    print(step, action, reward, terminated or truncated)"""
    if kind == "imitation":
        return f"""from pathlib import Path

dataset_root = Path("robot_demos")
for episode in sorted(dataset_root.glob("episode_*")):
    print("inspect", episode.name)
print("next step: convert demonstrations to the LeRobotDataset format")"""
    if kind == "vision":
        return f"""import numpy as np

points_world = np.array([[0.0, 0.0, 1.0], [0.5, 0.2, 1.0]])
camera_offset = np.array([0.1, 0.0, 0.0])
points_camera = points_world - camera_offset
print(points_camera)"""
    if kind == "language":
        return f"""instruction = "pick up the red block and place it on the tray"
skills = ["find_object", "estimate_pose", "grasp", "move_to_tray", "release"]
plan = [skill for skill in skills]
print(instruction)
print(plan)"""
    if kind == "world":
        return f"""state = 0.0
velocity = 1.0
dt = 0.1
for horizon in range(5):
    state = state + velocity * dt
    print(horizon, round(state, 3))"""
    if kind == "safety":
        return f"""def safety_filter(action, distance_to_human):
    if distance_to_human < 0.5:
        return 0.0
    return action

print(safety_filter(1.0, 0.3))
print(safety_filter(1.0, 1.2))"""
    return f"""from dataclasses import dataclass

@dataclass
class EmbodiedStep:
    observation: str
    action: str
    result: str

step = EmbodiedStep("{label}", "act", "observe consequence")
print(step)"""


def section_nav(chapter, section, rel):
    sections = chapter["sections"]
    idx = sections.index(section)
    prev = '<span class="prev">Chapter Home</span>'
    nxt = '<span class="next">Chapter End</span>'
    if idx == 0:
        prev = '<a class="prev" href="index.html">&#8592; Chapter Home</a>'
    else:
        prev_s = sections[idx - 1]
        prev = f'<a class="prev" href="{section_filename(prev_s)}">&#8592; Section {esc(prev_s["num"])}</a>'
    if idx + 1 < len(sections):
        next_s = sections[idx + 1]
        nxt = f'<a class="next" href="{section_filename(next_s)}">Section {esc(next_s["num"])} &#8594;</a>'
    return f'<nav class="chapter-nav">{prev}<a href="index.html">Chapter {chapter["number"]}</a>{nxt}</nav>'


def write_section_pages(part, chapter, all_chapters):
    kind = topic_kind(chapter["title"] + " " + part["title"])
    tools = TOOL_HINTS[kind]
    for section in chapter["sections"]:
        rel = "../../"
        body = page_head(f"Section {section['num']}: {section['title']}", rel, f"Section {section['num']} of {FULL_TITLE}: {section['title']}.")
        body += header(rel, f"Part {part['roman']}: {part['title']}", f"Chapter {chapter['number']}: {chapter['title']}", f"Section {section['num']}: {section['title']}", "../index.html", "index.html")
        code = esc(code_example(section, kind))
        body += f"""<blockquote class="epigraph"><p>"The world is an exam where the answer key changes after every action."</p><cite>A Careful Control Loop</cite></blockquote>
{callout("big-picture", "Big Picture", f"<p><strong>{esc(section['title'])}</strong> is one lens on {esc(chapter['title'].lower())}. We study it because an embodied agent needs decisions that survive contact with noisy sensors, delayed effects, and changing environments.</p>")}
<h2>What This Section Builds</h2>
<p>This section turns the idea of {esc(section['title'].lower())} into a usable mental model. First we define the object of study, then we connect it to the agent loop, then we test it with a compact implementation.</p>
<p>The key question is practical: what must the agent know, what can it observe, what action is available, and what evidence shows that the action worked?</p>
{callout("key-insight", "Action Is The Test", f"<p>A representation is useful only when it improves action. In {esc(section['title'].lower())}, the reader should keep asking which decision becomes easier, safer, or more reliable.</p>")}
<h2>Theory</h2>
<p>We can view the agent at time $t$ as receiving an observation $o_t$, maintaining an internal state estimate $\\hat s_t$, choosing an action $a_t$, and observing a consequence $o_{{t+1}}$. The section topic changes one part of this loop, but the loop itself stays fixed.</p>
<p>The practical design rule is to make the interface explicit. Inputs, outputs, assumptions, timing, and failure modes should be named before a model is trained or a controller is tuned.</p>
{callout("under-the-hood", "Mechanism", "<p>The mechanism is a sequence of transformations: observe, encode, estimate, choose, execute, monitor. Each transformation should have a measurable contract, otherwise debugging collapses into guessing.</p>")}
<h2>Worked Example</h2>
<p>Consider a simulated tabletop agent. A camera observation locates a block, a state estimator converts pixels into an approximate pose, a policy selects a motion, and a controller executes that motion. If the block slips, the loop must notice and recover rather than declare success too early.</p>
<pre><code class="language-python">{code}</code></pre>
<div class="code-caption">Code Fragment {esc(section['num'])}.1 shows the smallest executable pattern for this section's idea.</div>
{callout("library-shortcut", "Library Shortcut", f"<p>The from-scratch fragment is for understanding. In a practical system, use {esc(tools)} to handle environment interfaces, batching, physics, data formats, logging, and model loading. The shortcut removes boilerplate so the engineering attention goes to task design, evaluation, and failure recovery.</p>")}
<h2>Practical Recipe</h2>
<ol>
<li>Write the observation, action, and success metric before choosing a model.</li>
<li>Build a baseline that is simple enough to debug by inspection.</li>
<li>Add the library implementation only after the baseline behavior is understood.</li>
<li>Record failures as structured cases: perception error, state error, planning error, control error, or evaluation error.</li>
<li>Run at least one perturbation test before trusting the result.</li>
</ol>
{callout("warning", "Common Failure Mode", "<p>The common mistake is to evaluate a component in isolation and then assume the closed loop will inherit that score. Embodied systems often fail at the interfaces between components.</p>")}
{callout("practical-example", "Practical Example", f"<p>A robotics team using {esc(section['title'].lower())} should log not only final success, but intermediate observations, chosen actions, controller status, and recovery events. The logs reveal whether the method is solving the task or merely passing the easiest episodes.</p>")}
{callout("research-frontier", "Research Frontier", "<p>Frontier systems increasingly combine learned policies with structured constraints, tool use, large datasets, and simulation-driven evaluation. Claims from vendor releases should be treated as frontier watch items until independent evaluations or reproducible artifacts appear.</p>")}
{callout("self-check", "Self Check", f"<p>Can you name the observation, state estimate, action, success metric, and most likely failure mode for {esc(section['title'].lower())}? If not, the system boundary is still too vague.</p>")}
{callout("key-takeaway", "Key Takeaway", f"<p>{esc(section['title'])} is useful when it makes the perception-action loop more reliable, not when it merely adds a more impressive model name.</p>")}
<div class="callout exercise"><div class="callout-title">Exercise {esc(section['num'])}.1</div><p>Design a minimal experiment that tests this section's idea in simulation. Specify the environment, observations, actions, metric, and one perturbation.</p></div>
{section_nav(chapter, section, rel)}
"""
        body += footer(rel)
        write(ROOT / part["slug"] / chapter["slug"] / section_filename(section), body)


def write_appendices(parts):
    body = page_head("Appendices", "../", f"Appendices for {FULL_TITLE}.", code=False, math=False)
    body += header("../", "Appendices", "Reference", "Appendices")
    items = []
    for slug, letter, title in APPENDICES:
        items.append(f'<li><span class="section-num">{letter}</span> <a href="{slug}/index.html">{esc(title)}</a></li>')
    body += f"""<div class="overview"><h2>Reference Material</h2><p>The appendices keep the book self-contained: math, tools, compute recipes, datasets, reproducibility, notation, and citation discipline.</p></div>
<ul class="sections-list">{''.join(items)}</ul>
<nav class="chapter-nav"><a class="prev" href="../toc.html">&#8592; Contents</a><a href="../index.html">Book Home</a><a class="next" href="{APPENDICES[0][0]}/index.html">Appendix A &#8594;</a></nav>
"""
    body += footer("../")
    write(ROOT / "appendices" / "index.html", body)
    for idx, (slug, letter, title) in enumerate(APPENDICES):
        rel = "../../"
        body = page_head(f"Appendix {letter}: {title}", rel, f"Appendix {letter} of {FULL_TITLE}: {title}.")
        body += header(rel, "Appendices", f"Appendix {letter}", f"Appendix {letter}: {title}", "../index.html", "index.html")
        body += f"""{callout("big-picture", "Why This Appendix Exists", f"<p>{esc(title)} supports the self-contained promise of the book. It gives readers enough reference material to continue without opening a second textbook.</p>")}
<h2>Reference Notes</h2>
<p>This appendix should be used on demand. The main chapters link here when a mathematical tool, software package, benchmark, compute estimate, or citation convention needs a compact refresher.</p>
<h2>Practical Checklist</h2>
<ol><li>Identify the concept or tool needed by the chapter.</li><li>Review the minimal definition and notation.</li><li>Run the smallest example.</li><li>Return to the chapter with the missing prerequisite restored.</li></ol>
{callout("library-shortcut", "Operational Shortcut", "<p>For tools and libraries, prefer official documentation and pinned environment files. For math and notation, prefer the definitions used in this book so symbols stay consistent.</p>")}
{bibliography(rel, title)}
"""
        prev = "../index.html" if idx == 0 else f"../{APPENDICES[idx - 1][0]}/index.html"
        nxt = "../index.html" if idx + 1 == len(APPENDICES) else f"../{APPENDICES[idx + 1][0]}/index.html"
        body += f'<nav class="chapter-nav"><a class="prev" href="{prev}">&#8592; Previous</a><a href="../index.html">Appendices</a><a class="next" href="{nxt}">Next &#8594;</a></nav>'
        body += footer(rel)
        write(ROOT / "appendices" / slug / "index.html", body)


def main():
    parts = read_plan()
    clean_output(parts)
    write_index(parts)
    write_toc(parts)
    write_front_matter()
    write_part_pages(parts)
    write_chapter_pages(parts)
    write_appendices(parts)
    count_html = len(list(ROOT.rglob("*.html")))
    print(f"Generated {count_html} HTML files")


if __name__ == "__main__":
    main()
