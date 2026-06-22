from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAG_RE = re.compile(r"<[^>]+>")


def strip_text(raw: str) -> str:
    text = TAG_RE.sub(" ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def section_title(raw: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", raw, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return "the section topic"
    title = strip_text(match.group(1))
    title = re.sub(r"^Section\s+\d+\.\d+:\s*", "", title)
    title = re.sub(r"^Chapter\s+\d+:\s*", "", title)
    return title


def replace_exact(raw: str, old: str, new: str) -> str:
    return raw.replace(old, new)


def chapter9_builder_replacement(raw: str, safe_title: str) -> str:
    replacements = {
        "first estimate the real cost of hardware exploration, then decide which assumptions simulation can test cheaply, then save the artifact that proves the real robot is being used for targeted verification rather than blind trial collection": "estimate the real cost of hardware exploration, identify which assumptions simulation can test cheaply, and reserve real robot time for targeted verification backed by saved rollout artifacts",
        "first label the role of each rollout, then keep training, validation, held-out testing, and diagnostics in separate artifacts, then make sure the reported claim uses only evidence from the matching role": "label the role of each rollout, keep training, validation, held-out testing, and diagnostics in separate artifacts, and make the reported claim use only evidence from the matching role",
        "first name the fidelity axis that could change the robot's decision, then choose a simulator because it covers that axis, then record the unsupported axes as limits on the claim": "name the fidelity axis that could change the robot's decision, choose a simulator because it covers that axis, and record unsupported axes as explicit limits on the claim",
        "first define the paired sim-real panel, then compute the metric difference on the same task cases, then use the residual gap to decide whether to calibrate, randomize, narrow the claim, or return to hardware": "define the paired sim-real panel, compute the metric difference on the same task cases, and use the residual gap to decide whether to calibrate, randomize, narrow the claim, or return to hardware",
        "first identify the embodied construct you need to measure, then choose a benchmark family whose assumptions match that construct, then save the wrapper, config, version, seed panel, and failure diagnostics as the experiment artifact": "identify the embodied construct being measured, choose a benchmark family whose assumptions match that construct, and save the wrapper, config, version, seed panel, and failure diagnostics as the experiment artifact",
    }
    for old_tail, new_tail in replacements.items():
        raw = raw.replace(
            f"<p>Read this section as a builder's chain: {old_tail}.</p>",
            f"<p>Use {safe_title} as an engineering audit: {new_tail}.</p>",
        )
    return raw


def process(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8", errors="replace")
    title = section_title(raw)
    safe_title = html.escape(title)
    updated = raw
    updated = chapter9_builder_replacement(updated, safe_title)

    updated = replace_exact(
        updated,
        '<p>"The world is an exam where the answer key changes after every action."</p>',
        f'<p>"{safe_title} matters when the next action changes the evidence you thought you had."</p>',
    )
    updated = replace_exact(
        updated,
        "<p>The mechanism is a sequence of transformations: observe, encode, estimate, choose, execute, monitor. Each transformation should have a measurable contract, otherwise debugging collapses into guessing.</p>",
        f"<p>The mechanism in {safe_title} is the contract between representation and action. Name what enters the module, what leaves it, which assumptions make that transformation valid, and which log would reveal a bad handoff.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>The practical design rule is to make the interface explicit. Inputs, outputs, assumptions, timing, and failure modes should be named before a model is trained or a controller is tuned.</p>",
        f"<p>For {safe_title}, the practical design rule is to make the interface inspectable before optimization begins: inputs, outputs, units, latency, bounds, and failure labels should all be visible in the saved artifact.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>We can view the agent at time $t$ as receiving an observation $o_t$, maintaining an internal state estimate $\\hat s_t$, choosing an action $a_t$, and observing a consequence $o_{t+1}$. The section topic changes one part of this loop, but the loop itself stays the same.</p>",
        f"<p>Formally, {safe_title} should be placed inside the closed-loop transition $o_t \\rightarrow \\hat s_t \\rightarrow a_t \\rightarrow o_{{t+1}}$. The important question is which variable, assumption, or constraint changes when this section's mechanism is added.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>We can view the agent at time $t$ as receiving an observation $o_t$, maintaining an internal state estimate $\\hat s_t$, choosing an action $a_t$, and observing a consequence $o_{t+1}$. The section topic changes one part of this loop, but the loop itself stays fixed.</p>",
        f"<p>Formally, {safe_title} should be placed inside the closed-loop transition $o_t \\rightarrow \\hat s_t \\rightarrow a_t \\rightarrow o_{{t+1}}$. The important question is which variable, assumption, or constraint changes when this section's mechanism is added.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>The common mistake is to evaluate a component in isolation and then assume the closed loop will inherit that score. Embodied systems often fail at the interfaces between components.</p>",
        f"<p>The common mistake in {safe_title} is to celebrate the component score before checking the closed-loop handoff. The failure usually appears at the boundary: stale state, wrong frame, delayed action, saturated actuator, or metric that ignores the real task cost.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>Design a method-matched experiment that tests this section's idea in simulation. Specify the environment, observations, actions, metric, and one perturbation.</p>",
        f"<p>Design a method-matched experiment for {safe_title}. Specify the environment, observation schema, action interface, metric, and one perturbation that targets the section's core assumption.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>Ask readers to fill the evidence record before they touch model code. The exercise exposes vague task definitions early, when they are cheap to repair.</p>",
        f"<p>Ask readers to fill the {safe_title} evidence record before they touch model code. The exercise exposes vague task definitions while the schema, metric, and perturbation are still easy to repair.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>Consider a simulated tabletop agent. A camera observation locates a block, a state estimator converts pixels into an approximate pose, a policy selects a motion, and a controller executes that motion. If the block slips, the loop must notice and recover rather than simply report an earlier prediction score.</p>",
        f"<p>For {safe_title}, keep one concrete rollout in view. A sensor reading becomes an estimate, the estimate constrains an action, the action changes the world, and the next observation confirms or contradicts the assumption. The section's idea is useful only if it improves that loop.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>Consider a simulated tabletop agent. A camera observation locates a block, a state estimator converts pixels into an approximate pose, a policy selects a motion, and a controller executes that motion. If the block slips, the loop must notice and recover rather than declare success too early.</p>",
        f"<p>For {safe_title}, keep one concrete rollout in view. A sensor reading becomes an estimate, the estimate constrains an action, the action changes the world, and the next observation confirms or contradicts the assumption. The section's idea is useful only if it improves that loop.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>The key question is practical: what must the agent know, what can it observe, what action is available, and what evidence shows that the action worked?</p>",
        f"<p>The key question in {safe_title} is practical: what must the agent know, what can it observe, what action is available, and what evidence shows that the action worked under the stated conditions?</p>",
    )
    updated = replace_exact(
        updated,
        "<p>Frontier systems increasingly combine learned policies with structured constraints, tool use, large datasets, and simulation-driven evaluation. Claims from vendor releases should be treated as frontier watch items until independent evaluations or reproducible artifacts make them scientific evidence.</p>",
        f"<p>For {safe_title}, treat frontier claims as hypotheses until they expose enough detail to reproduce the result: data boundary, embodiment, controller interface, evaluation panel, and failure cases.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>Frontier systems increasingly combine learned policies with structured constraints, tool use, large datasets, and simulation-driven evaluation. Claims from vendor releases should be treated as frontier watch items until independent evaluations or reproducible artifacts appear.</p>",
        f"<p>For {safe_title}, treat frontier claims as hypotheses until they expose enough detail to reproduce the result: data boundary, embodiment, controller interface, evaluation panel, and failure cases.</p>",
    )
    updated = replace_exact(
        updated,
        "<p class=\"bib-annotation\">Use these sources to verify assumptions, implementation details, expected outputs, and evaluation artifacts.</p>",
        f"<p class=\"bib-annotation\">Use these sources to verify the assumptions, implementation details, expected outputs, and evaluation artifacts behind {safe_title}.</p>",
    )
    updated = replace_exact(
        updated,
        "<p class=\"bib-annotation\">Use official docs for install commands, current APIs, and version caveats before running the chapter lab.</p>",
        f"<p class=\"bib-annotation\">Use official docs to check install commands, current APIs, and version caveats before applying {safe_title} in a lab or project.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>The graduate-level habit is to separate three claims. The conceptual claim explains why the method should help. The systems claim explains which interface it changes. The evidence claim records which measurement would convince a skeptical builder. This separation protects the reader from treating an elegant idea as an evaluated system.</p>",
        f"<p>For {safe_title}, separate the conceptual claim, the systems claim, and the evidence claim. That discipline keeps a plausible mechanism, a convenient interface, and a real closed-loop result from being confused with one another.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>The graduate-level habit is to separate three claims. The conceptual claim explains why the idea should help. The systems claim explains which interface it changes. The evidence claim records which same-config measurement would convince a skeptical reader. Keeping these claims separate prevents a good story, a clean API, or a single rollout from pretending to prove more than it does.</p>",
        f"<p>For {safe_title}, separate the conceptual claim, the systems claim, and the evidence claim. A good explanation, a clean API, and one successful rollout are different kinds of evidence, and the section should keep them distinct.</p>",
    )
    updated = replace_exact(
        updated,
        "<p>The graduate-level habit is to separate three claims. The conceptual claim explains why the method should help. The systems claim explains which interface it changes. The evidence claim records which measurement would convince a skeptical builder. This separation keeps theory, implementation, and evaluation connected without letting any one of them pretend to prove the other two.</p>",
        f"<p>For {safe_title}, separate the conceptual claim, the systems claim, and the evidence claim. A plausible mechanism, a clean interface, and a closed-loop result are different claims; the section should keep their evidence separate.</p>",
    )

    if updated != raw:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(ROOT.glob("part-*/*/*.html")):
        if process(path):
            changed += 1
    print(f"changed_files={changed}")


if __name__ == "__main__":
    main()
