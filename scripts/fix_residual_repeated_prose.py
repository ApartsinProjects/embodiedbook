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


def page_title(raw: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", raw, flags=re.I | re.S)
    if not match:
        match = re.search(r"<title>(.*?)</title>", raw, flags=re.I | re.S)
    title = strip_text(match.group(1)) if match else "this topic"
    title = re.sub(r"^Section\s+\d+\.\d+:\s*", "", title)
    title = re.sub(r"^Chapter\s+\d+:\s*", "", title)
    title = title.split("|")[0].strip()
    return html.escape(title)


def process(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8", errors="replace")
    title = page_title(raw)
    updated = raw

    replacements = {
        "<p>A robust implementation starts with a tiny, inspectable baseline and only then moves to a maintained tool. The baseline should log observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The library version should produce the same artifact schema, so the comparison is construct-matched rather than assembled from separate experiments.</p>":
            f"<p>For {title}, a robust implementation starts with one inspectable baseline whose artifact records observations, actions, units, timestamps, seeds, termination reasons, and the perturbation applied. The maintained-tool version is useful only if it preserves that schema and lets the comparison remain construct-matched.</p>",
        "<p>A robust implementation starts with a tiny, inspectable baseline and only then moves to Gymnasium or PettingZoo. The baseline should log inputs, outputs, units, timestamps, and termination conditions. The library version should produce the same artifact schema, so the comparison is a same-task comparison rather than a story assembled from separate experiments.</p>":
            f"<p>For {title}, start with a small baseline that logs inputs, outputs, units, timestamps, and termination conditions before moving to Gymnasium or PettingZoo. The library run should keep the same artifact schema, so the comparison remains a same-task evaluation.</p>",
        "<p>A robust implementation starts with a tiny, inspectable baseline and only then moves to the maintained tool. The baseline and library version should produce the same artifact schema, so the comparison is co-computed on one task panel instead of assembled from incompatible runs.</p>":
            f"<p>For {title}, the baseline and maintained-tool version should produce the same artifact schema and run on one task panel. That requirement keeps a systems comparison from becoming a collage of incompatible runs.</p>",
        "<p>The common mistake is to evaluate a component in isolation and then assume the closed-loop will inherit that score. Embodied systems often fail at the interfaces between components.</p>":
            f"<p>The common mistake in {title} is to trust a component score before checking the closed-loop interface. The failure usually appears where state, timing, authority, or evaluation context crosses a module boundary.</p>",
        "<p>Before leaving this section, the reader should be able to explain what the printed artifact proves, what it leaves uncertain, and what the next experiment would change. If that explanation is missing, the section has not yet become an executable research or teaching unit.</p>":
            f"<p>Before leaving {title}, the reader should be able to explain what the printed artifact proves, what uncertainty remains, and which next experiment would stress the section's central assumption.</p>",
        "<p>Figure 31.1 gives this page a compact map of the interface. Read it left to right, then check whether the surrounding prose names the same observation, action, and evidence contract.</p>":
            f"<p>For {title}, read the figure as an interface map: instruction, grounded state, executable action, verifier, and evidence artifact should all appear in the surrounding prose.</p>",
        "<p>Name the language interface, the grounded world state, the executable action contract, and the evidence artifact before trusting any claimed improvement.</p>":
            f"<p>For {title}, name the language interface, grounded world state, executable action contract, and evidence artifact before trusting any claimed improvement.</p>",
        "<p>Write one row that records instruction, world state estimate, chosen action, verifier result, and failure label. Then explain which field would change first if the agent misunderstood the command.</p>":
            f"<p>For {title}, write one evidence row recording instruction, world-state estimate, chosen action, verifier result, and failure label. Then identify which field would change first under command misunderstanding.</p>",
        "<p>If the perception result cannot answer what action changed, what uncertainty changed, and what log would reproduce the decision, it is still a pretty picture wearing a hard hat.</p>":
            f"<p>For {title}, the perception result must answer what action changed, what uncertainty changed, and what log would reproduce the decision. Otherwise the output is still visualization, not embodied evidence.</p>",
        "<p>Evaluate the representation inside the same action loop that will use it. The report should include the sensor stream, calibration version, frame transform, model checkpoint or library version, latency distribution, action candidate set, chosen action, and failure label.</p>":
            f"<p>Evaluate {title} inside the same action loop that will use it. The report should include the sensor stream, calibration version, frame transform, model checkpoint or library version, latency distribution, action candidate set, chosen action, and failure label.</p>",
        "<p>A good debugging run varies one factor at a time. Perturb lighting, occlusion, calibration, motion blur, viewpoint, object pose, or update rate, then record whether the action changed for the right reason. That single-factor habit is what turns a failed rollout into a diagnosis rather than a mystery.</p>":
            f"<p>For {title}, a good debugging run varies one factor at a time. Perturb lighting, occlusion, calibration, motion blur, viewpoint, object pose, or update rate, then record whether the action changed for the right reason.</p>",
    }

    for old, new in replacements.items():
        updated = updated.replace(old, new)

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
