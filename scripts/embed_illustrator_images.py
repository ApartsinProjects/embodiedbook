from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "_illustrator_staging"
MANIFEST = STAGING / "manifest.json"
BATCH_DIR = STAGING / "generated2"


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def first_paragraph_end(text: str) -> int | None:
    match = re.search(r"</p>", text, re.I)
    return match.end() if match else None


def embed(entry: dict[str, str]) -> bool:
    section = ROOT / entry["section_file"]
    image_path = ROOT / entry["image_file"]
    text = section.read_text(encoding="utf-8", errors="ignore")
    rel_src = "images/" + image_path.name
    if rel_src in text:
        return False
    alt = (
        f"Cartoon educational scene for {entry['section_title']}, showing an embodied AI system using perception, "
        "planning, action, and feedback to make the section concept concrete."
    )
    caption = (
        f"{entry['section_title']} becomes easier to reason about when the reader can see the perception, decision, "
        "action, and feedback loop as one physical situation."
    )
    figure = (
        "\n<figure class=\"illustration\">\n"
        f"<img src=\"{rel_src}\" alt=\"{html.escape(alt, quote=True)}\" loading=\"lazy\"/>\n"
        f"<figcaption><strong>Figure {entry['section']}A</strong>: {html.escape(caption)}</figcaption>\n"
        "</figure>\n"
    )
    insert_at = first_paragraph_end(text)
    if insert_at is None:
        return False
    text = text[:insert_at] + figure + text[insert_at:]
    section.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))
    copied = 0
    embedded = 0
    missing = []
    for idx, entry in enumerate(entries, 1):
        src = BATCH_DIR / f"img_{idx:03d}.png"
        dst = ROOT / entry["image_file"]
        if not src.exists():
            missing.append(str(src))
            continue
        dst.parent.mkdir(exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1
        if embed(entry):
            embedded += 1
    print(f"copied={copied}")
    print(f"embedded={embedded}")
    print(f"missing={len(missing)}")
    for item in missing[:20]:
        print(f"missing_file={item}")
    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
