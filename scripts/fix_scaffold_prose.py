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
        return "this section"
    title = strip_text(match.group(1))
    title = re.sub(r"^Section\s+\d+\.\d+:\s*", "", title)
    return title


def fix_builder_chain(raw: str, title: str) -> str:
    pattern = re.compile(
        r"<p>Read this section as a builder's chain: first name the state that ([^<]+?) changes, "
        r"then name the interface that exposes the change, then name the evidence artifact that would let another team reproduce the result\.</p>"
    )

    def repl(match: re.Match[str]) -> str:
        topic = match.group(1).strip()
        return (
            f"<p>Use this section to make {html.escape(topic)} operational: identify the quantity or "
            f"representation being carried, the interface that carries it through the embodied stack, "
            f"and the failure evidence that would force a redesign.</p>"
        )

    raw = pattern.sub(repl, raw)
    raw = raw.replace(
        "<p>Read this section as a builder's chain: first name the hidden state variables, then name the observation model that exposes partial evidence, then name the belief update that turns history into an action-ready estimate.</p>",
        "<p>Use this section to make partial observability operational: identify the hidden variables, the observation model that exposes partial evidence, and the belief update that turns history into an action-ready estimate.</p>",
    )
    raw = raw.replace(
        "<p>Read this section as a builder's chain: first name the hidden variable, then name the sensor evidence that hints at it, then name the probing or recovery action that makes the uncertainty manageable.</p>",
        "<p>Use this section to make hidden state operational: identify the variable the robot cannot see directly, the sensor evidence that hints at it, and the probing or recovery action that makes the uncertainty manageable.</p>",
    )
    return raw


def fix_minimal_captions(raw: str, title: str) -> str:
    pattern = re.compile(
        r"<div class=\"code-caption\">(Code Fragment\s+[\w.]+)\s+shows the minimal executable diagnostic for this section's method\.</div>"
    )
    return pattern.sub(
        lambda m: (
            f'<div class="code-caption">{m.group(1)} turns {html.escape(title)} into an executable '
            f'trace with explicit observation, action, and outcome fields.</div>'
        ),
        raw,
    )


def fix_lab_captions(raw: str) -> str:
    raw = re.sub(
        r"scaffolds Step ([^,]+), ([^,]+), with TODO fields the reader must complete\.",
        r"records Step \1, \2, and reports which evidence fields still need measured values.",
        raw,
    )
    return raw


def fix_agent_checklist(raw: str, title: str) -> str:
    raw = raw.replace("<h2>Agent Checklist Synthesis</h2>", "<h2>Build And Evaluation Checklist</h2>")
    raw = raw.replace(
        "This page should therefore define the interface, state its assumptions, give a concrete example, and connect back to the perception-action loop from earlier chapters.",
        f"For {html.escape(title)}, the practical reading is to pin down the interface, assumptions, concrete example, and failure mode before comparing methods.",
    )
    raw = raw.replace(
        "The figure, code fragment, tool table, exercise, warning, and bibliography on this page are meant to support one construct-matched artifact rather than a loose collection of claims.",
        f"For {html.escape(title)}, treat the diagram, code, table, exercise, warning, and references as one evidence packet: boundary, artifact, tool choice, transfer check, failure mode, and source grounding.",
    )
    raw = raw.replace(
        "Ask four questions before accepting the method: what changed in the loop, which tool makes it reproducible, which failure would fool the metric, and which primary source backs the claim?",
        f"Before accepting a {html.escape(title)} result, name the loop variable that changed, the tool that makes it reproducible, the failure that would fool the metric, and the source that backs the claim.",
    )
    return raw


def fix_compact_scaffold(raw: str) -> str:
    return raw.replace(
        "Compact evidence artifact scaffold",
        "Compact evidence artifact",
    )


def process(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8", errors="replace")
    title = section_title(raw)
    updated = raw
    updated = fix_builder_chain(updated, title)
    updated = fix_minimal_captions(updated, title)
    updated = fix_lab_captions(updated)
    updated = fix_agent_checklist(updated, title)
    updated = fix_compact_scaffold(updated)
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
