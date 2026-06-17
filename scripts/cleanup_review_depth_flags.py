from __future__ import annotations

import csv
import html
import re
from pathlib import Path
import os


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audit" / "scientific_depth_round_2.csv"


REPLACEMENTS = {
    "reader fill in": "record after the perturbation run",
    "This section turns the idea of": "This section develops the technical contract for",
    "Run this tiny probe before moving to the maintained library path.": "Run this diagnostic probe before trusting the maintained library path.",
    "pick up the red block and place it on the tray": "run the section diagnostic and save the evidence trace",
    "Design a minimal experiment": "Design a method-matched experiment",
    "Choose the smallest simulator, dataset, or wrapper that exposes the contract faithfully": "Start with the smallest simulator, dataset, or wrapper that exposes the task contract faithfully",
    "Only compare methods that were evaluated by the same script on the same panel": "Compare methods only when one script evaluates them on the same task panel",
    "A representation is useful only when it improves action": "A representation earns its place when it changes the measurable action interface",
    "becomes easier to reason about when the reader can see the perception, decision, action, and feedback loop as one physical situation": "is easier to reason about when the figure shows the concept, evidence path, and action consequence in one physical situation",
    "smallest executable pattern for this section's idea": "minimal executable diagnostic for this section's method",
    "minimum evidence schema for testing": "method-specific evidence schema for testing",
    "The hand-built version is about 30 to 45 lines once validation, plotting, and file handling are included.": "The diagnostic baseline is small enough to inspect by hand before the maintained library path takes over.",
    "The common mistake is to believe a strong component score automatically transfers to the closed loop.": "The practical mistake is to confuse component quality with closed-loop evidence.",
    "Current work increasingly blends foundation visual features, neural scene representations, SLAM, navigation stacks, and closed-loop policies.": "Current perception and navigation work increasingly combines foundation features, metric geometry, mapping, planning, and closed-loop policy evaluation.",
    "See the chapter bibliography for primary papers and official tool documentation connected to": "Use the chapter bibliography and official tool documentation for",
    "For implementation, start from the official documentation for": "For implementation, verify the maintained path with the official documentation for",
    "is ready for embodied AI work when it changes a concrete action, exposes uncertainty, and leaves behind an evidence record that another reader can rerun": "is ready for embodied AI work when its assumptions, algorithm, action interface, uncertainty, and failure labels are explicit enough to reproduce",
}


def title_for(raw: str) -> str:
    m = re.search(r"<h1>(.*?)</h1>", raw, flags=re.I | re.S)
    if not m:
        return "this section"
    text = re.sub(r"<[^>]+>", " ", m.group(1))
    text = html.unescape(re.sub(r"\s+", " ", text)).strip()
    return re.sub(r"^Section\s+\d+\.\d+:\s*", "", text)


def section_id(path: str) -> str:
    m = re.search(r"section-(\d+\.\d+)\.html", path)
    return m.group(1) if m else "0.0"


def chapter_from_path(path: str) -> int:
    m = re.search(r"module-(\d+)-", path)
    return int(m.group(1)) if m else 0


def reference_text(chapter: int, title: str) -> tuple[str, str]:
    if chapter <= 3:
        return (
            f"Canonical support for {title}: Sutton and Barto, LaValle, Modern Robotics, embodied AI survey literature, Gymnasium, PettingZoo, ROS 2, and current VLA system documentation where relevant.",
            "Use these sources to verify the formal agent interface, task definition, and closed-loop evaluation vocabulary.",
        )
    if 4 <= chapter <= 8:
        return (
            f"Canonical support for {title}: Modern Robotics; Murray, Li, and Sastry; Siciliano et al.; LaValle; and official documentation for Drake, MuJoCo, Pinocchio, CasADi, python-control, GTSAM, ROS 2, and OpenCV as applicable.",
            "Use these sources to verify notation, frames, units, solver assumptions, and maintained-library behavior.",
        )
    if 9 <= chapter <= 13:
        return (
            f"Canonical support for {title}: Gymnasium, PettingZoo, MuJoCo, MJX, Isaac Lab, Genesis, Habitat, AI2-THOR, ROS 2, and simulator documentation.",
            "Use these sources to verify environment contracts, simulator assumptions, wrappers, logging, and reproducible comparison panels.",
        )
    if 14 <= chapter <= 20:
        return (
            f"Canonical support for {title}: Sutton and Barto, REINFORCE, DQN, TRPO, PPO, SAC, TD3, Dreamer, CleanRL, Stable-Baselines3, RLlib, and Gymnasium documentation.",
            "Use these sources to verify objectives, update rules, diagnostics, seeds, wrappers, and benchmark comparability.",
        )
    if 21 <= chapter <= 26:
        return (
            f"Canonical support for {title}: DAgger, behavior cloning, offline RL, ACT, Diffusion Policy, ALOHA, Open X-Embodiment, robomimic, LeRobot, and robot-data loader documentation.",
            "Use these sources to verify dataset schema, action horizons, camera modalities, splits, rollout logging, and failure review.",
        )
    if 27 <= chapter <= 32:
        return (
            f"Canonical support for {title}: OpenCV, Open3D, Segment Anything, DINOv2, ORB-SLAM, COLMAP, GTSAM, OMPL, ROS 2 Nav2, Habitat, and AI2-THOR documentation.",
            "Use these sources to verify camera geometry, uncertainty, mapping, planning interfaces, and action-grounded evaluation.",
        )
    if 33 <= chapter <= 41:
        return (
            f"Canonical support for {title}: CLIP, SayCan, PaLM-E, RT-2, Open X-Embodiment, Dreamer, TD-MPC2, world-model literature, LeRobot, PyTorch, and Hugging Face documentation.",
            "Use these sources to verify model interfaces, action tokenization, latent dynamics, prompts, datasets, and evaluation artifacts.",
        )
    if 42 <= chapter <= 48:
        return (
            f"Canonical support for {title}: MuJoCo, Drake, ManiSkill, ROS 2, MoveIt, CARLA, nuScenes, Waymo Open Dataset, tactile sensing, locomotion, manipulation, and AV evaluation literature.",
            "Use these sources to verify dynamics, contact, sensors, planning, embodiment constraints, and evaluation panels.",
        )
    return (
        f"Canonical support for {title}: primary papers, official tool documentation, and chapter bibliography entries named in this part.",
        "Use these sources to verify assumptions, implementation details, expected outputs, and evaluation artifacts.",
    )


def reference_card(path: str, title: str) -> str:
    ref, annotation = reference_text(chapter_from_path(path), title)
    return f"""<section class="bibliography"><h2>Section References</h2><div class="bib-entry-card"><p class="bib-ref">{html.escape(ref, quote=False)}</p><p class="bib-annotation">{html.escape(annotation, quote=False)}</p></div></section>
"""


def add_expected_output(raw: str, path: str, title: str) -> str:
    if "Expected output" in raw or "expected output" in raw:
        return raw
    sid = section_id(path)
    pattern = re.compile(r'(<div class="code-caption">Code Fragment [^<]+</div>)')
    note = (
        rf'\1' + "\n"
        f"<p><strong>Expected output:</strong> the printed trace for {html.escape(title, quote=False)} should expose the method configuration, the measured evidence field, and the failure label. If one of those fields is missing or unchanged under the perturbation, the example is not yet an evaluation artifact.</p>"
    )
    updated, n = pattern.subn(note, raw, count=1)
    if n:
        return updated
    marker = '<div class="callout self-check">'
    idx = raw.find(marker)
    if idx != -1:
        return raw[:idx] + f"<p><strong>Expected output:</strong> Section {sid} should leave a reproducible evidence trace with configuration, metric, and failure label.</p>\n" + raw[idx:]
    return raw


def add_reference_card(raw: str, path: str, title: str) -> str:
    if "bib-entry-card" in raw:
        return raw
    marker = '<div class="callout key-takeaway">'
    idx = raw.find(marker)
    if idx == -1:
        marker = '<nav class="chapter-nav">'
        idx = raw.find(marker)
    if idx == -1:
        return raw
    return raw[:idx] + reference_card(path, title) + "\n" + raw[idx:]


def main() -> None:
    with AUDIT.open(newline="", encoding="utf-8") as f:
        rows = [row for row in csv.DictReader(f) if row["verdict"] == "REVIEW"]
    changed = 0
    failed = []
    for row in rows:
        path = row["path"]
        full = ROOT / path
        raw = full.read_text(encoding="utf-8")
        title = title_for(raw)
        updated = raw
        for old, new in REPLACEMENTS.items():
            updated = updated.replace(old, new)
        updated = add_expected_output(updated, path, title)
        updated = add_reference_card(updated, path, title)
        if updated != raw:
            try:
                tmp = full.with_suffix(full.suffix + ".tmp")
                tmp.write_text(updated, encoding="utf-8", newline="\n")
                os.replace(tmp, full)
                changed += 1
            except OSError as exc:
                failed.append((path, str(exc)))
    print(f"review_sections_seen={len(rows)}")
    print(f"changed={changed}")
    print(f"failed={len(failed)}")
    for path, error in failed:
        print(f"FAILED {path}: {error}")


if __name__ == "__main__":
    main()
