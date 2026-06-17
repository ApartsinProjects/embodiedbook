from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SCAFFOLD_PHRASES = [
    "This section builds",
    "By the end of this section",
    "practical payoff",
    "library handles internally",
]

MIN_SECTION_BYTES = 11000
MIN_CHAPTER_BYTES = 13000


def html_files():
    return [path for path in ROOT.rglob("*.html") if "templates" not in path.parts]


def main():
    section_gaps = []
    chapter_gaps = []
    scaffold_hits = []
    for path in html_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if path.name.startswith("section-") and path.stat().st_size < MIN_SECTION_BYTES:
            section_gaps.append((rel, path.stat().st_size))
        if path.name == "index.html" and "module-" in str(path) and path.stat().st_size < MIN_CHAPTER_BYTES:
            chapter_gaps.append((rel, path.stat().st_size))
        for phrase in SCAFFOLD_PHRASES:
            if phrase in text:
                scaffold_hits.append((rel, phrase))
                break

    print(f"section_depth_gaps={len(section_gaps)}")
    print(f"chapter_depth_gaps={len(chapter_gaps)}")
    print(f"scaffold_phrase_hits={len(scaffold_hits)}")
    for rel, size in section_gaps[:50]:
        print(f"SECTION_DEPTH {rel} {size}")
    for rel, size in chapter_gaps[:50]:
        print(f"CHAPTER_DEPTH {rel} {size}")
    for rel, phrase in scaffold_hits[:50]:
        print(f"SCAFFOLD_PHRASE {rel} {phrase}")
    raise SystemExit(1 if section_gaps or chapter_gaps or scaffold_hits else 0)


if __name__ == "__main__":
    main()
