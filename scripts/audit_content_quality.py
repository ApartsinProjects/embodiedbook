from __future__ import annotations

import csv
import html
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audit" / "content_quality.csv"
TAG_RE = re.compile(r"<[^>]+>")
PARA_RE = re.compile(r"<p\b[^>]*>([\s\S]*?)</p>", re.IGNORECASE)
BIBLIO_RE = re.compile(r"<section\b[^>]*class=\"[^\"]*bibliography[^\"]*\"[\s\S]*?</section>", re.IGNORECASE)
NAV_RE = re.compile(r"<nav\b[\s\S]*?</nav>", re.IGNORECASE)
FOOTER_RE = re.compile(r"<footer\b[\s\S]*?</footer>", re.IGNORECASE)

SCAFFOLD_PATTERNS = [
    "Read this section as a builder's chain",
    "first name the state that",
    "shows the minimal executable diagnostic for this section's method",
    "Agent Checklist Synthesis",
    "This page should therefore define the interface",
    "figure, code fragment, tool table, exercise, warning, and bibliography",
    "Ask four questions before accepting the method",
    "scaffolds Step",
    "TODO fields the reader must complete",
    "Compact evidence artifact scaffold",
    "smallest inspectable probe",
]


def strip_text(raw: str) -> str:
    text = TAG_RE.sub(" ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def norm_para(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\d+(?:\.\d+)*", "N", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main_prose(raw: str) -> str:
    raw = BIBLIO_RE.sub(" ", raw)
    raw = NAV_RE.sub(" ", raw)
    raw = FOOTER_RE.sub(" ", raw)
    return raw


def main() -> None:
    rows: list[dict[str, object]] = []
    para_locations: dict[str, list[tuple[str, int, str]]] = defaultdict(list)

    for path in sorted(ROOT.glob("part-*/*/*.html")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        scan_raw = main_prose(raw)
        rel = str(path.relative_to(ROOT))
        text = strip_text(scan_raw)
        for pattern in SCAFFOLD_PATTERNS:
            count = scan_raw.count(pattern) + text.count(pattern)
            if count:
                rows.append({
                    "kind": "scaffold_pattern",
                    "path": rel,
                    "line": raw[: raw.find(pattern)].count("\n") + 1 if pattern in raw else 1,
                    "count": count,
                    "detail": pattern,
                })
        if not path.name.startswith("section-"):
            continue
        for idx, match in enumerate(PARA_RE.finditer(scan_raw), start=1):
            para = strip_text(match.group(1))
            if len(para.split()) < 12:
                continue
            key = norm_para(para)
            para_locations[key].append((rel, raw[: match.start()].count("\n") + 1, para))

    for key, locations in para_locations.items():
        if len(locations) < 5:
            continue
        sample = locations[0][2]
        rows.append({
            "kind": "repeated_paragraph",
            "path": "; ".join(loc[0] for loc in locations[:5]),
            "line": locations[0][1],
            "count": len(locations),
            "detail": sample[:260],
        })

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["kind", "path", "line", "count", "detail"])
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["kind"] for row in rows)
    print(f"issues={len(rows)}")
    for kind, count in counts.most_common():
        print(f"{kind}={count}")
    print(f"report={OUT}")

    raise SystemExit(1 if rows else 0)


if __name__ == "__main__":
    main()
