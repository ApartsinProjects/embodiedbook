from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "audit" / "ai_fluff.csv"

PHRASES: list[tuple[str, str]] = [
    (r"\bin today'?s (rapidly evolving|fast-paced|ever-changing)\b", "generic opening"),
    (r"\bplays? a (crucial|vital|pivotal) role\b", "inflated importance"),
    (r"\bit is (important|crucial|vital) to (note|understand|recognize)\b", "empty throat clearing"),
    (r"\bdelve into\b", "generic verb"),
    (r"\bunlock(s|ing)? (the )?(power|potential)\b", "marketing phrasing"),
    (r"\bseamless(ly)?\b", "marketing phrasing"),
    (r"\brobust and scalable\b", "unearned quality pair"),
    (r"\bcutting-edge\b", "hype adjective"),
    (r"\brevolutioni[sz]e\b", "hype verb"),
    (r"\bgame[- ]changer\b", "hype noun"),
    (r"\bnot just .{0,80} but\b", "stock contrast"),
    (r"\bjourney\b", "generic metaphor"),
    (r"\blandscape\b", "generic metaphor"),
    (r"\brealm\b", "generic metaphor"),
    (r"\bnavigate the complexities\b", "generic phrase"),
    (r"\bleverage(s|d|ing)?\b", "generic verb"),
]


def strip_tags(text: str) -> str:
    text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text)


def main() -> int:
    rows: list[dict[str, object]] = []
    for path in sorted(ROOT.glob("part-*/*/section-*.html")):
        text = strip_tags(path.read_text(encoding="utf-8", errors="replace"))
        for pattern, reason in PHRASES:
            for match in re.finditer(pattern, text, flags=re.I):
                start = max(0, match.start() - 90)
                end = min(len(text), match.end() + 90)
                rows.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "reason": reason,
                        "match": match.group(0),
                        "context": text[start:end].strip(),
                    }
                )

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "reason", "match", "context"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"issues={len(rows)}")
    print(f"report={REPORT}")
    return 1 if rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
