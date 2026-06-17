from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "audit"
SECTION_RE = re.compile(r"section-(\d+)\.(\d+)\.html$")
TAG_RE = re.compile(r"<[^>]+>")


TEMPLATE_PHRASES = [
    "is one lens on",
    "decisions that survive contact with noisy sensors, delayed effects, and changing environments",
    "This section turns the idea of",
    "Run this tiny probe before moving to the maintained library path",
    "pick up the red block and place it on the tray",
    "reader fill in",
    "Design a minimal experiment",
    "Agent Checklist Applied To This Section",
    "Choose the smallest simulator, dataset, or wrapper that exposes the contract faithfully",
    "Only compare methods that were evaluated by the same script on the same panel",
    "A representation is useful only when it improves action",
    "becomes easier to reason about when the reader can see the perception, decision, action, and feedback loop as one physical situation",
    "smallest executable pattern for this section's idea",
    "minimum evidence schema for testing",
    "See the chapter bibliography for primary papers and official tool documentation connected to",
    "is ready for embodied AI work when it changes a concrete action",
    "The common mistake is to believe a strong component score automatically transfers to the closed loop",
    "Current work increasingly blends foundation visual features",
    "For implementation, start from the official documentation",
    "The hand-built version is about 30 to 45 lines",
]


FORMAL_TERMS = [
    "equation", "objective", "loss", "constraint", "gradient", "jacobian", "hessian",
    "state-space", "transfer function", "lyapunov", "bellman", "mdp", "pomdp",
    "policy", "value function", "dynamics", "kinematics", "se(3)", "so(3)",
    "kalman", "particle filter", "bayes", "optimization", "convex", "nonlinear",
    "stability", "observability", "controllability", "uncertainty", "covariance",
]


MECHANISM_TERMS = [
    "because", "therefore", "under", "assumption", "failure", "latency", "timing",
    "perturbation", "ablation", "tradeoff", "diagnostic", "saturation", "drift",
    "calibration", "frame", "metric", "evaluate", "compare", "baseline",
]


TOOL_TERMS = [
    "ROS 2", "Nav2", "MoveIt", "Gazebo", "Isaac", "MuJoCo", "PyBullet", "Drake",
    "Gymnasium", "PettingZoo", "Habitat", "AI2-THOR", "OpenCV", "Open3D",
    "PyTorch", "JAX", "CasADi", "python-control", "do-mpc", "OMPL", "NetworkX",
    "Hugging Face", "Stable-Baselines3", "Ray RLlib", "Weights & Biases",
    "TensorBoard", "DINOv2", "Segment Anything", "SAM", "SLAM",
]


SPECIFICITY_TERMS = [
    "RRT", "RRT*", "PRM", "A*", "Dijkstra", "DWA", "MPC", "PID", "LQR", "iLQR",
    "CEM", "PPO", "SAC", "TD3", "DDPG", "BC", "DAgger", "GAIL", "VLA",
    "CLIP", "RT-2", "RT-X", "SayCan", "PaLM-E", "V-JEPA", "Dreamer",
    "occupancy grid", "factor graph", "pose graph", "loop closure", "ICP",
    "visual odometry", "Gaussian splatting", "NeRF", "diffusion policy",
    "calibration", "precision", "recall", "success rate", "confidence interval",
    "expected calibration error", "risk", "hazard", "monitor", "shield",
    "out-of-distribution", "conformal", "ensemble", "uncertainty estimate",
]


MATH_HEAVY_CHAPTERS = set(range(4, 9)) | set(range(14, 21)) | {29, 30, 31, 32, 36, 37, 38, 39, 40, 41, 52, 53, 54}


@dataclass
class SectionAudit:
    path: str
    chapter: int
    section: int
    title: str
    words: int
    code_blocks: int
    figures: int
    tables: int
    math_markers: int
    bibliography_cards: int
    template_hits: int
    formal_hits: int
    mechanism_hits: int
    tool_hits: int
    specificity_hits: int
    score: int
    verdict: str
    issues: str
    recommendation: str


def strip_text(raw: str) -> str:
    raw = re.sub(r"<script\b.*?</script>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<style\b.*?</style>", " ", raw, flags=re.I | re.S)
    text = TAG_RE.sub(" ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def count_terms(text: str, terms: list[str]) -> int:
    low = text.lower()
    return sum(low.count(term.lower()) for term in terms)


def title_for(raw: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", raw, flags=re.I | re.S)
    if not match:
        match = re.search(r"<title>(.*?)</title>", raw, flags=re.I | re.S)
    if not match:
        return "(untitled)"
    return strip_text(match.group(1))


def audit_section(path: Path) -> SectionAudit:
    raw = path.read_text(encoding="utf-8")
    text = strip_text(raw)
    low = text.lower()
    match = SECTION_RE.search(path.name)
    chapter = int(match.group(1)) if match else 0
    section = int(match.group(2)) if match else 0
    words = len(re.findall(r"[A-Za-z][A-Za-z0-9_+-]*", text))
    code_blocks = raw.lower().count("<pre><code")
    figures = raw.lower().count("<figure")
    tables = raw.lower().count("<table")
    math_markers = raw.count("$") + raw.lower().count("katex") + raw.lower().count("math")
    bibliography_cards = raw.count("bib-entry-card")
    template_hits = sum(raw.count(phrase) for phrase in TEMPLATE_PHRASES)
    formal_hits = count_terms(text, FORMAL_TERMS)
    mechanism_hits = count_terms(text, MECHANISM_TERMS)
    tool_hits = count_terms(text, TOOL_TERMS)
    specificity_hits = count_terms(text, SPECIFICITY_TERMS)

    score = 0
    score += min(words // 180, 10)
    score += min(formal_hits, 8)
    score += min(mechanism_hits // 2, 8)
    score += min(tool_hits, 8)
    score += min(specificity_hits, 8)
    score += min(code_blocks * 2, 6)
    score += min(figures, 4)
    score += min(tables * 2, 4)
    score += min(bibliography_cards * 2, 4)
    score += min(math_markers // 4, 4)
    score -= min(template_hits * 3, 18)

    issues: list[str] = []
    if words < 950:
        issues.append("short prose body")
    if template_hits >= 3:
        issues.append("repeated scaffold language")
    if formal_hits < 4 and chapter in MATH_HEAVY_CHAPTERS:
        issues.append("insufficient formal or algorithmic specificity")
    if mechanism_hits < 8:
        issues.append("weak mechanism and failure analysis")
    if tool_hits < 3:
        issues.append("few concrete tool or library anchors")
    if specificity_hits < 2 and chapter in MATH_HEAVY_CHAPTERS:
        issues.append("topic-specific names are sparse")
    if code_blocks and "expected" not in low and "print(" in raw:
        issues.append("code lacks explicit expected-output discussion")
    if bibliography_cards == 0:
        issues.append("missing local reference card")

    if not issues and score >= 34:
        verdict = "COURSE-READY"
        recommendation = "Keep. Spot-check only during publication QA."
    elif score >= 34 and len(issues) <= 3 and template_hits == 0:
        verdict = "REVIEW"
        recommendation = "Add the missing local reference or expected-output note, then keep the section."
    elif score >= 28 and len(issues) <= 2:
        verdict = "REVIEW"
        recommendation = "Add one topic-specific mechanism paragraph and one evidence or tool detail."
    else:
        verdict = "DEPTH-GAP"
        recommendation = "Rewrite around the section's actual algorithm, model, toolchain, assumptions, failure modes, and runnable evidence."

    return SectionAudit(
        path=str(path.relative_to(ROOT)).replace("\\", "/"),
        chapter=chapter,
        section=section,
        title=title_for(raw),
        words=words,
        code_blocks=code_blocks,
        figures=figures,
        tables=tables,
        math_markers=math_markers,
        bibliography_cards=bibliography_cards,
        template_hits=template_hits,
        formal_hits=formal_hits,
        mechanism_hits=mechanism_hits,
        tool_hits=tool_hits,
        specificity_hits=specificity_hits,
        score=score,
        verdict=verdict,
        issues="; ".join(issues),
        recommendation=recommendation,
    )


def main() -> None:
    sections = sorted(
        p for p in ROOT.glob("part-*/*/section-*.html")
        if SECTION_RE.search(p.name)
    )
    audits = [audit_section(p) for p in sections]
    OUT_DIR.mkdir(exist_ok=True)

    csv_path = OUT_DIR / "scientific_depth_round_2.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(audits[0]).keys()))
        writer.writeheader()
        for row in audits:
            writer.writerow(asdict(row))

    json_path = OUT_DIR / "scientific_depth_round_2.json"
    json_path.write_text(json.dumps([asdict(a) for a in audits], indent=2), encoding="utf-8")

    verdict_counts = Counter(a.verdict for a in audits)
    issue_counts = Counter()
    for audit in audits:
        for issue in filter(None, audit.issues.split("; ")):
            issue_counts[issue] += 1

    by_chapter: dict[int, Counter[str]] = defaultdict(Counter)
    for audit in audits:
        by_chapter[audit.chapter][audit.verdict] += 1

    weakest = sorted(audits, key=lambda a: (a.score, -a.template_hits, a.path))[:40]
    review = [a for a in audits if a.verdict != "COURSE-READY"]

    md = []
    md.append("# Scientific and Technological Depth Audit, Round 2\n")
    md.append("This audit reads every section HTML file and applies the book-writers depth rubrics: deep explanation, code pedagogy, research grounding, self-containment, and publication QA. The automated pass is a triage tool, not a substitute for author judgment, so it deliberately flags polished but generic sections.\n")
    md.append("## Scope\n")
    md.append(f"- Section files audited: {len(audits)}\n")
    md.append(f"- Machine-readable inventory: `audit/scientific_depth_round_2.csv` and `audit/scientific_depth_round_2.json`\n")
    md.append("- Rubric: mechanism depth, formal or algorithmic specificity, concrete tools and libraries, runnable evidence, self-contained definitions, local references, and scaffold reuse.\n")
    md.append("## Verdict Counts\n")
    for key in ["COURSE-READY", "REVIEW", "DEPTH-GAP"]:
        md.append(f"- {key}: {verdict_counts.get(key, 0)}\n")
    md.append("## Most Common Issues\n")
    for issue, count in issue_counts.most_common(12):
        md.append(f"- {issue}: {count}\n")
    md.append("## Chapter-Level Distribution\n")
    md.append("| Chapter | Course-ready | Review | Depth-gap |\n")
    md.append("|---:|---:|---:|---:|\n")
    for chapter in sorted(by_chapter):
        c = by_chapter[chapter]
        md.append(f"| {chapter} | {c.get('COURSE-READY', 0)} | {c.get('REVIEW', 0)} | {c.get('DEPTH-GAP', 0)} |\n")
    md.append("## Weakest Sections To Fix First\n")
    md.append("| Score | Verdict | Section | Issues | Recommendation |\n")
    md.append("|---:|---|---|---|---|\n")
    for audit in weakest:
        md.append(
            f"| {audit.score} | {audit.verdict} | `{audit.path}` | {audit.issues or 'none'} | {audit.recommendation} |\n"
        )
    md.append("## Agent Rubric Notes\n")
    md.append("- Deep explanation gate: a section must answer what, why, how, and when it fails, not only define the topic.\n")
    md.append("- Code pedagogy gate: runnable fragments need a reason to exist, named inputs and outputs, and expected-output interpretation when output is nontrivial.\n")
    md.append("- Research scientist gate: a graduate section should name algorithms, assumptions, measurement artifacts, and credible tools rather than broad families only.\n")
    md.append("- Self-containment gate: sections should define variables, frames, metrics, and failure labels locally enough for a course reader to proceed without leaving the page.\n")
    md.append("- Publication QA gate: repeated scaffold language is treated as a defect even when links, images, and callouts are structurally valid.\n")
    md.append("## Remediation Policy\n")
    md.append("Fix depth gaps by replacing generic action-loop prose with topic-specific material: derivation or algorithm sketch, assumptions, implementation contract, tool-specific recipe, failure analysis, and one evidence artifact. Do not add decorative prose to pass the audit.\n")

    report_path = ROOT / "DEPTH_AUDIT_ROUND_2.md"
    report_path.write_text("".join(md), encoding="utf-8")

    print(f"audited={len(audits)}")
    print("verdicts=" + ", ".join(f"{k}:{v}" for k, v in verdict_counts.items()))
    print(f"review_or_gap={len(review)}")
    print(f"report={report_path}")
    print(f"csv={csv_path}")


if __name__ == "__main__":
    main()
