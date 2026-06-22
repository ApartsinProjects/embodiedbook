from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "magic constants": "unexplained constants",
    "magic knob": "free tuning knob",
    "anti-magic scaffolding": "stronger grounding scaffolding",
    "magic transfer": "automatic transfer",
    "magic speed labels": "automatic speed labels",
    "unexplained magic": "opaque behavior",
    "magic acceleration": "automatic acceleration",
    "magically solve robotics": "solve robotics by itself",
    "magical replacement": "drop-in replacement",
    "magically substitutes for physics": "substitutes for physics",
    "magic simulator score library": "automatic simulator-score library",
    "model as magic": "model as an oracle",
    "magic label": "self-sufficient label",
    "magic training label": "self-sufficient training label",
    "magic oracle": "oracle",
    "toy examples": "compact examples",
    "toy example": "compact example",
    "pretty pictures": "latent-space visualizations",
    "pretty picture wearing a hard hat": "visualization rather than embodied evidence",
    "repo_id</code> placeholder marks": "repo_id</code> field marks",
}


def process(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8", errors="replace")
    updated = raw
    for old, new in REPLACEMENTS.items():
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
