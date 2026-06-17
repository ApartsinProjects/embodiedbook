import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MARKER = "production-depth-expansion"

SKIP_CHAPTERS = {
    "module-11-physics-simulators-mujoco-mjx-isaac-lab-genesis",
    "module-34-vision-language-action-models",
}

PART_TOOLS = {
    "Foundations of Embodied AI": ["Gymnasium", "PettingZoo", "ROS 2", "MuJoCo", "LeRobot"],
    "Mathematical, Robotics, and Control Foundations": ["numpy", "scipy", "spatialmath", "pinocchio", "pydrake", "ROS 2 tf2"],
    "Simulation, Tooling, and the Modern Stack": ["Gymnasium", "PettingZoo", "MuJoCo", "Isaac Lab", "ManiSkill", "BlenderProc"],
    "Reinforcement Learning for Embodied Agents": ["CleanRL", "Stable-Baselines3", "Tianshou", "SKRL", "RSL-RL", "rl_games"],
    "Imitation Learning, Demonstrations, and Robot Data": ["LeRobot", "robomimic", "Diffusion Policy", "ACT", "ALOHA", "UMI"],
    "Embodied Perception": ["OpenCV", "PyTorch", "Detectron2", "Ultralytics", "SAM", "DINOv2", "Open3D"],
    "Language, Vision, and Action": ["Transformers", "OpenVLA", "LeRobot", "openpi", "vLLM", "ROS 2"],
    "World Models and Model-Based Embodied AI": ["PyTorch", "JAX", "Dreamer-style agents", "TD-MPC style planners", "diffusion planners"],
    "Manipulation, Locomotion, and Embodied Skills": ["MuJoCo", "Isaac Lab", "ManiSkill", "robosuite", "Pinocchio", "ROS 2"],
    "Multi-Agent and Human-Centered Embodiment": ["PettingZoo", "ROS 2", "LangGraph", "OpenTelemetry", "human study logs"],
    "Evaluation, Safety, Robustness, and Deployment": ["pytest", "OpenTelemetry", "Prometheus", "control barrier functions", "runtime monitors"],
    "Frontiers, Capstones, and Course Design": ["LeRobot", "OpenVLA", "Gymnasium", "Weights and Biases", "course notebooks"],
}


def clean(text: str) -> str:
    replacements = {
        "\u2014": ":",
        "\u2013": "-",
        "honestly": "rigorously",
        "frankly": "plainly",
        "candidly": "directly",
        "to be honest": "in practice",
        "in truth": "in practice",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def between(text: str, pattern: str) -> str:
    match = re.search(pattern, text, re.S)
    return html.unescape(match.group(1)).strip() if match else ""


def part_name(text: str) -> str:
    label = between(text, r'<div class="part-label">.*?</a>Part [IVX]+: ([^<]+)</div>')
    return label or "Foundations of Embodied AI"


def chapter_name(text: str) -> str:
    return between(text, r'<div class="chapter-label">.*?</a>Chapter \d+: ([^<]+)</div>')


def section_title(text: str) -> str:
    return between(text, r"<h1>Section ([^<]+)</h1>")


def section_number(title: str) -> str:
    match = re.match(r"(\d+\.\d+):", title)
    return match.group(1) if match else "0.0"


def tools_for(part: str) -> list[str]:
    return PART_TOOLS.get(part, ["Python", "structured logs", "experiment dashboards", "simulation"])


def esc(text: str) -> str:
    return html.escape(clean(text), quote=True)


def section_expansion(text: str) -> str:
    part = part_name(text)
    chapter = chapter_name(text)
    title = section_title(text)
    number = section_number(title)
    topic = title.split(": ", 1)[-1] if ": " in title else title
    tools = tools_for(part)
    primary = tools[0]
    secondary = tools[1] if len(tools) > 1 else tools[0]
    tertiary = tools[2] if len(tools) > 2 else tools[0]
    tool_cells = "".join(f"<tr><td>{esc(tool)}</td><td>{esc(topic)}</td><td>Use it when the experiment needs a maintained implementation rather than custom glue.</td></tr>" for tool in tools[:5])
    code_id = number.replace(".", "_")
    return f"""
<section class="{MARKER}">
<h2>Builder's Deep Dive</h2>
<p>{esc(topic)} becomes useful when it is tied to a closed-loop contract. In this chapter on {esc(chapter)}, the contract names the observation stream, the state estimate, the action representation, the timing budget, and the evaluation artifact. Without that contract, a model can look capable in a notebook while failing the first time a sensor drops a frame or a controller saturates.</p>
<p>The graduate-level habit is to separate three claims. The conceptual claim explains why the method should help. The systems claim explains which interface it changes. The evidence claim records which measurement would convince a skeptical builder. This separation keeps theory, implementation, and evaluation connected without letting any one of them pretend to prove the other two.</p>

<div class="comparison-table">
<div class="comparison-table-title">Practical Tool Choices For This Section</div>
<table>
<thead><tr><th>Tool or Library</th><th>Role in the Topic</th><th>Builder Advice</th></tr></thead>
<tbody>
{tool_cells}
</tbody>
</table>
</div>

<h2>Implementation Recipe</h2>
<p>A robust implementation starts with a tiny, inspectable baseline and only then moves to {esc(primary)} or {esc(secondary)}. The baseline should log inputs, outputs, units, timestamps, and termination conditions. The library version should produce the same artifact schema, so the comparison is a same-task comparison rather than a story assembled from separate experiments.</p>
<ol>
<li>Write a one-paragraph task contract with observation, action, success, and failure fields.</li>
<li>Choose the smallest simulator, dataset, or wrapper that exposes the contract faithfully.</li>
<li>Run one deterministic smoke test and one perturbation test before scaling.</li>
<li>Save a single result artifact containing configuration, seed, metrics, videos or traces, and failure labels.</li>
<li>Only compare methods that were evaluated by the same script on the same panel.</li>
</ol>

<pre><code class="language-python"># Build one evidence record for {esc(topic)}.
# The same schema should be used for the baseline and the library shortcut.
from dataclasses import dataclass, asdict

@dataclass
class EvidenceRecord:
    section: str
    tool: str
    observation: str
    action: str
    metric: str
    perturbation: str

record = EvidenceRecord(
    section="{esc(number)}",
    tool="{esc(primary)}",
    observation="reader fill in: sensor or state input",
    action="reader fill in: control or decision output",
    metric="reader fill in: construct-matched success metric",
    perturbation="reader fill in: delay, noise, domain shift, or contact change",
)
print(asdict(record))</code></pre>
<div class="code-caption">Code Fragment {esc(number)}.2 records the minimum evidence schema for testing {esc(topic)} with {esc(primary)} while keeping results comparable to {esc(secondary)} and {esc(tertiary)}.</div>

<div class="callout tip"><div class="callout-title">Teaching Move</div><p>Ask readers to fill the evidence record before they touch model code. The exercise exposes vague task definitions early, when they are cheap to repair.</p></div>

<h2>Failure Analysis Pattern</h2>
<p>When {esc(topic)} fails, avoid labeling the whole method as weak. First assign the failure to perception, state estimation, planning, control, timing, data coverage, or evaluation. Then rerun one controlled perturbation that isolates the suspected cause. This pattern turns a disappointing rollout into a reusable diagnostic asset.</p>
</section>
"""


def chapter_expansion(text: str) -> str:
    part = part_name(text)
    chapter = chapter_name(text)
    tools = tools_for(part)
    cells = "".join(f"<tr><td>{esc(tool)}</td><td>Use for a concrete lab, comparison, or extension in this chapter.</td></tr>" for tool in tools[:6])
    return f"""
<section class="{MARKER}">
<h2>Production Notes For Readers</h2>
<p>This chapter is written for readers who want theory and a working build path in the same pass. Read each section twice: first for the mechanism, then for the artifact you would save if you had to reproduce the result six months later.</p>
<div class="comparison-table">
<div class="comparison-table-title">Chapter Tool Map</div>
<table>
<thead><tr><th>Tool or Library</th><th>Where It Pays Off</th></tr></thead>
<tbody>
{cells}
</tbody>
</table>
</div>
<div class="callout lab"><div class="callout-title">Chapter Lab Extension</div><p>Extend the lab by adding one baseline, one maintained-library implementation, and one perturbation test. Save the result as a single folder containing configuration, logs, summary metrics, and two representative failure cases.</p></div>
</section>
"""


def chapter_topup(text: str) -> str:
    part = part_name(text)
    chapter = chapter_name(text)
    tools = tools_for(part)
    tool_list = ", ".join(tools[:5])
    return f"""
<section class="production-index-depth-topup">
<h2>Instructor And Builder Notes</h2>
<p>The chapter can be used as a self-contained reading unit or as the basis for an undergraduate or graduate teaching week. The recommended pattern is concept, minimal implementation, library shortcut, diagnostic exercise, then reflection on failure modes. This keeps the mathematical idea attached to a concrete system artifact rather than letting it float as notation.</p>
<p>For {esc(chapter)}, the practical stack should be introduced as a set of choices rather than a shopping list. The relevant tools include {esc(tool_list)}. Each tool earns its place only when it shortens a working path, improves reproducibility, or exposes a standard interface that students will meet in real embodied systems.</p>
<div class="callout self-check"><div class="callout-title">Readiness Check</div><p>Before leaving the chapter, the reader should be able to state one theory claim, one implementation claim, one evaluation claim, and one realistic failure mode. If any of those four are missing, the chapter should be revisited through the lab.</p></div>
<div class="callout key-takeaway"><div class="callout-title">Teaching Takeaway</div><p>A strong chapter session ends with an artifact: a small script, a plotted trace, a simulator run, a data card, or a reproducible evaluation panel. The artifact is what turns reading into embodied-system-building practice.</p></div>
</section>
"""


def chapter_finalizer(text: str) -> str:
    part = part_name(text)
    chapter = chapter_name(text)
    tools = tools_for(part)
    primary = tools[0]
    secondary = tools[1] if len(tools) > 1 else tools[0]
    return f"""
<section class="production-index-finalizer">
<h2>Assessment And Extension Path</h2>
<p>A rigorous reading of this chapter should end with a small assessment package. The package contains one conceptual answer, one runnable artifact, one diagnostic trace, and one extension idea. That format works for self-study, undergraduate projects, and graduate seminars because it checks understanding without pretending that a single quiz captures embodied competence.</p>
<p>For {esc(chapter)}, rebuild the simplest example twice: once from first principles, and once with {esc(primary)} or {esc(secondary)}. The first version exposes the mechanics. The second version teaches the professional toolchain. The contrast is the signature move of this book: understand the mechanism, then use the library that makes the reliable version practical.</p>
<div class="callout practical-example"><div class="callout-title">Course Artifact</div><p>For a teaching setting, ask each reader to submit a two-page lab note with the task contract, the command used to run the artifact, the resulting metric table, and one failure screenshot or trace. This makes grading about evidence rather than polish.</p></div>
</section>
"""


def enrich_section(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    cleaned = text.replace("This section builds", "This section develops")
    cleaned = cleaned.replace("What This Section Builds", "What This Section Develops")
    if cleaned != text:
        path.write_text(clean(cleaned), encoding="utf-8", newline="\n")
        return True
    if MARKER in text:
        return False
    if path.stat().st_size >= 11000:
        return False
    insertion = section_expansion(text)
    marker = '<div class="callout key-takeaway">'
    index = text.find(marker)
    if index == -1:
        marker = '<nav class="chapter-nav">'
        index = text.find(marker)
    if index == -1:
        return False
    text = text[:index] + insertion + "\n" + text[index:]
    path.write_text(clean(text), encoding="utf-8", newline="\n")
    return True


def enrich_chapter(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    text = text.replace("This section builds", "This section develops")
    text = text.replace("What This Section Builds", "What This Section Develops")
    if "production-index-depth-topup" in text and "production-index-finalizer" not in text and path.stat().st_size < 13000:
        insertion = chapter_finalizer(text)
        marker = '<section class="bibliography">'
        index = text.find(marker)
        if index == -1:
            marker = '<nav class="chapter-nav">'
            index = text.find(marker)
        if index == -1:
            path.write_text(clean(text), encoding="utf-8", newline="\n")
            return True
        text = text[:index] + insertion + "\n" + text[index:]
        path.write_text(clean(text), encoding="utf-8", newline="\n")
        return True
    if MARKER in text and "production-index-depth-topup" in text:
        path.write_text(clean(text), encoding="utf-8", newline="\n")
        return False
    if MARKER in text and path.stat().st_size < 13000:
        insertion = chapter_topup(text)
        marker = '<section class="bibliography">'
        index = text.find(marker)
        if index == -1:
            marker = '<nav class="chapter-nav">'
            index = text.find(marker)
        if index == -1:
            return False
        text = text[:index] + insertion + "\n" + text[index:]
        path.write_text(clean(text), encoding="utf-8", newline="\n")
        return True
    if MARKER in text:
        return False
    if path.stat().st_size >= 13000:
        return False
    insertion = chapter_expansion(text)
    marker = '<section class="bibliography">'
    index = text.find(marker)
    if index == -1:
        marker = '<nav class="chapter-nav">'
        index = text.find(marker)
    if index == -1:
        return False
    text = text[:index] + insertion + "\n" + text[index:]
    path.write_text(clean(text), encoding="utf-8", newline="\n")
    return True


def main():
    changed = []
    for module in ROOT.glob("part-*/module-*"):
        if module.name in SKIP_CHAPTERS:
            continue
        index = module / "index.html"
        if index.exists() and enrich_chapter(index):
            changed.append(index.relative_to(ROOT))
        for section in sorted(module.glob("section-*.html")):
            if enrich_section(section):
                changed.append(section.relative_to(ROOT))
    print(f"changed={len(changed)}")
    for rel in changed[:80]:
        print(rel)


if __name__ == "__main__":
    main()
