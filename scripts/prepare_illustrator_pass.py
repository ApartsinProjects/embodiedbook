from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "_illustrator_staging"
PROMPTS = STAGING / "prompts.txt"
MANIFEST = STAGING / "manifest.json"


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def chapter_number(module_dir: Path) -> str:
    match = re.match(r"module-(\d+)-", module_dir.name)
    return str(int(match.group(1))) if match else module_dir.name


def section_number(section_file: Path) -> str:
    match = re.match(r"section-(\d+\.\d+)\.html", section_file.name)
    return match.group(1) if match else section_file.stem


def title_from_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S | re.I)
    if h1:
        return clean_text(h1.group(1))
    title = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
    return clean_text(title.group(1)) if title else path.parent.name


def section_summary(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S | re.I)
    title = clean_text(h1.group(1)) if h1 else section_number(path)
    paragraphs = [clean_text(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", text, re.S | re.I)]
    paragraphs = [p for p in paragraphs if len(p) > 40]
    summary = " ".join(paragraphs[:2])[:650]
    return title, summary


def prompt_for(chapter_title: str, section_title: str, summary: str) -> str:
    return (
        "A witty, cartoon-like educational illustration with clean lines and a warm color palette: "
        "a friendly embodied AI robot learning a physical-world intelligence concept through action and feedback. "
        f"The teaching idea is {section_title}. Context for the artist only, do not depict words from it: {summary} "
        "Use only label-free physical props: blocks, paths, sensors, camera lenses, wheels, robot arms, soft uncertainty clouds, shadows, arrows, and simple motion trails. "
        "Do not include charts, dashboards, monitors, whiteboards, papers, books, signs, labels, speech bubbles, thought bubbles containing words, interface panels, axes, legends, or any object that would normally contain writing. "
        "The image should communicate the mental model through body language and physical arrangement only. "
        "Style: friendly and approachable, clean cartoon textbook art, expressive faces and body language, one clear visual idea, minimal clutter, generous negative space. "
        "Absolute hard constraint: no text, no letters, no numbers, no mathematical symbols, no punctuation, no logos, no watermarks, no readable or unreadable writing anywhere in the image."
    )


def build_manifest() -> list[dict[str, str]]:
    STAGING.mkdir(exist_ok=True)
    entries: list[dict[str, str]] = []
    modules = sorted(ROOT.glob("part-*/module-*"))
    for module in modules:
        if not module.is_dir():
            continue
        sections = sorted(module.glob("section-*.html"))
        if not sections:
            continue
        chap = chapter_number(module)
        chapter_title = title_from_file(module / "index.html") if (module / "index.html").exists() else module.name
        selected = sections[:5]
        (module / "images").mkdir(exist_ok=True)
        for idx, section in enumerate(selected, 1):
            sec_num = section_number(section)
            sec_title, summary = section_summary(section)
            filename = f"chapter-{int(chap):02d}-illustration-{idx:02d}.png" if chap.isdigit() else f"{module.name}-illustration-{idx:02d}.png"
            entries.append(
                {
                    "chapter": chap,
                    "chapter_title": chapter_title,
                    "section": sec_num,
                    "section_title": sec_title,
                    "section_file": str(section.relative_to(ROOT)),
                    "image_file": str((module / "images" / filename).relative_to(ROOT)),
                    "prompt": prompt_for(chapter_title, sec_title, summary),
                }
            )
    PROMPTS.write_text("\n".join(entry["prompt"] for entry in entries), encoding="utf-8")
    MANIFEST.write_text(json.dumps(entries, indent=2), encoding="utf-8")
    return entries


def main() -> None:
    entries = build_manifest()
    print(f"prepared_prompts={len(entries)}")
    print(f"manifest={MANIFEST}")
    print(f"prompts={PROMPTS}")


if __name__ == "__main__":
    main()
