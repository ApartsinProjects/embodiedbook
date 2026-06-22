"""Prepare a human-readable batch of section HTML for manual review.

This script is only a display aid. It strips navigation and layout HTML so the
section prose, examples, callouts, figures, and references can be read directly.
It does not score, classify, or decide whether content is good.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def section_key(path: Path) -> tuple[int, int, str]:
    match = re.search(r"section-(\d+)\.(\d+)\.html$", path.name)
    if not match:
        return (10_000, 10_000, str(path))
    return (int(match.group(1)), int(match.group(2)), str(path))


def section_files() -> list[Path]:
    return sorted(ROOT.rglob("section-*.html"), key=section_key)


def strip_layout(text: str) -> str:
    text = re.sub(r"(?is)<head\b.*?</head>", "", text)
    text = re.sub(r"(?is)<script\b.*?</script>", "", text)
    text = re.sub(r"(?is)<style\b.*?</style>", "", text)
    text = re.sub(r"(?is)<nav\b.*?</nav>", "", text)
    text = re.sub(r"(?is)<footer\b.*?</footer>", "", text)
    return text


def readable_html(text: str) -> str:
    text = strip_layout(text)
    text = re.sub(
        r'(?is)<pre[^>]*>\s*<code[^>]*>',
        "\n\n```text\n",
        text,
    )
    text = re.sub(r"(?is)</code>\s*</pre>", "\n```\n\n", text)

    replacements = [
        (r"(?is)<h1[^>]*>", "\n\n# "),
        (r"(?is)</h1>", "\n"),
        (r"(?is)<h2[^>]*>", "\n\n## "),
        (r"(?is)</h2>", "\n"),
        (r"(?is)<h3[^>]*>", "\n\n### "),
        (r"(?is)</h3>", "\n"),
        (r"(?is)<h4[^>]*>", "\n\n#### "),
        (r"(?is)</h4>", "\n"),
        (r'(?is)<div[^>]*class="[^"]*callout-title[^"]*"[^>]*>', "\n\n**CALLOUT:** "),
        (r'(?is)<div[^>]*class="[^"]*code-caption[^"]*"[^>]*>', "\n\n**CODE CAPTION:** "),
        (r'(?is)<div[^>]*class="[^"]*code-output[^"]*"[^>]*>', "\n\n**CODE OUTPUT:** "),
        (r"(?is)<figcaption[^>]*>", "\n\n**FIGURE:** "),
        (r"(?is)</figcaption>", "\n"),
        (r"(?is)<p[^>]*>", "\n\n"),
        (r"(?is)</p>", "\n"),
        (r"(?is)<li[^>]*>", "\n- "),
        (r"(?is)</li>", "\n"),
        (r"(?is)<br\s*/?>", "\n"),
        (r"(?is)</div>", "\n"),
        (r"(?is)</section>", "\n"),
    ]
    for pattern, value in replacements:
        text = re.sub(pattern, value, text)

    text = re.sub(r"(?is)<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True, help="1-based section index")
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    files = section_files()
    start = args.start - 1
    chosen = files[start : start + args.count]
    args.out.parent.mkdir(parents=True, exist_ok=True)

    chunks = [
        f"# Manual Reading Batch\n\nSections {args.start}-{args.start + len(chosen) - 1} of {len(files)}\n"
    ]
    for index, path in enumerate(chosen, start=args.start):
        rel = path.relative_to(ROOT)
        raw = path.read_text(encoding="utf-8")
        chunks.append("\n\n" + "=" * 88)
        chunks.append(f"\n\n## [{index:03d}] {rel}\n\n")
        chunks.append(readable_html(raw))

    args.out.write_text("\n".join(chunks) + "\n", encoding="utf-8")
    print(args.out)


if __name__ == "__main__":
    main()
