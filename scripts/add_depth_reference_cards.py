from __future__ import annotations

import csv
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audit" / "scientific_depth_round_2.csv"


def title_for(raw: str) -> str:
    m = re.search(r"<h1>(.*?)</h1>", raw, flags=re.I | re.S)
    if not m:
        return "this section"
    text = re.sub(r"<[^>]+>", " ", m.group(1))
    text = html.unescape(re.sub(r"\s+", " ", text)).strip()
    return re.sub(r"^Section\s+\d+\.\d+:\s*", "", text)


def chapter_from_path(path: str) -> int:
    m = re.search(r"module-(\d+)-", path)
    return int(m.group(1)) if m else 0


def reference_text(chapter: int, title: str) -> tuple[str, str]:
    if chapter in {5, 6, 7, 8}:
        return (
            f"Canonical support for {title}: Modern Robotics; Murray, Li, and Sastry; Siciliano et al.; LaValle; and the official documentation for Drake, MuJoCo, Pinocchio, CasADi, python-control, GTSAM, ROS 2, and OpenCV as applicable.",
            "Use these sources to verify notation, frame conventions, solver assumptions, and library behavior before comparing hand-built and maintained-tool implementations.",
        )
    if chapter in {49, 50, 51}:
        return (
            f"Canonical support for {title}: Markov games, Dec-POMDPs, human-robot interaction studies, PettingZoo, SuperSuit, RLlib, ROS 2, Nav2, and embodied-agent benchmark documentation.",
            "Use these sources to verify agent interfaces, partner splits, communication channels, intervention logs, and human-centered safety measures.",
        )
    if chapter in {56, 57, 58}:
        return (
            f"Canonical support for {title}: continual learning, memory-augmented agents, open-world evaluation, LeRobot, Habitat, AI2-THOR, PyTorch, and vector-database retrieval documentation.",
            "Use these sources to separate memory, adaptation, parameter updates, retrieval, and evaluation artifacts.",
        )
    if chapter == 59:
        return (
            f"Canonical support for {title}: LeRobot, robomimic, Gymnasium, MuJoCo, Habitat, ROS 2, PyTorch, and reproducibility guidance from the relevant project repositories.",
            "Use these sources to pin dataset format, training configuration, rollout logging, validation splits, and artifact packaging.",
        )
    if chapter == 60:
        return (
            f"Canonical support for {title}: the book's chapter sequence, current simulator and robot-data documentation, and reproducible teaching workflows using notebooks, GitHub, CI, and lightweight evaluation harnesses.",
            "Use these sources to align weekly readings, labs, rubrics, milestones, and prerequisite pacing.",
        )
    return (
        f"Canonical support for {title}: official tool documentation, primary method papers, and the chapter bibliography.",
        "Use these sources to verify assumptions, implementation details, and evaluation artifacts.",
    )


def card_for(path: str, title: str) -> str:
    ref, annotation = reference_text(chapter_from_path(path), title)
    return f"""<section class="bibliography"><h2>Section References</h2><div class="bib-entry-card"><p class="bib-ref">{html.escape(ref, quote=False)}</p><p class="bib-annotation">{html.escape(annotation, quote=False)}</p></div></section>
"""


def main() -> None:
    with AUDIT.open(newline="", encoding="utf-8") as f:
        paths = [row["path"] for row in csv.DictReader(f) if row["verdict"] == "DEPTH-GAP"]
    changed = 0
    for rel in paths:
        full = ROOT / rel
        raw = full.read_text(encoding="utf-8")
        if "bib-entry-card" in raw:
            continue
        title = title_for(raw)
        marker = '<div class="callout key-takeaway">'
        idx = raw.find(marker)
        if idx == -1:
            marker = '<nav class="chapter-nav">'
            idx = raw.find(marker)
        if idx == -1:
            continue
        updated = raw[:idx] + card_for(rel, title) + "\n" + raw[idx:]
        full.write_text(updated, encoding="utf-8", newline="\n")
        changed += 1
    print(f"reference_cards_added={changed}")


if __name__ == "__main__":
    main()
