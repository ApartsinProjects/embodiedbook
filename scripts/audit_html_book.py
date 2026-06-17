from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse


ROOT = Path(__file__).resolve().parents[1]

BANNED_PATTERNS = [
    "\u2014",
    "\u2013",
    "--",
    "honestly",
    "frankly",
    "candidly",
    "to be honest",
    "in truth",
]

REQUIRED_CHAPTER_SNIPPETS = [
    'class="epigraph"',
    "callout big-picture",
    "callout key-insight",
    "Chapter Overview",
    "Prerequisites",
    "Chapter Roadmap",
    "Hands-On Lab",
    "Bibliography",
]

REQUIRED_SECTION_SNIPPETS = [
    "callout big-picture",
    "callout key-insight",
    "callout library-shortcut",
    "callout warning",
    "callout practical-example",
    "callout research-frontier",
    "callout self-check",
    "callout key-takeaway",
    "callout exercise",
    "code-caption",
]


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)


def generated_html_files():
    return [
        path for path in ROOT.rglob("*.html")
        if "templates" not in path.parts
    ]


def check_links(files):
    checked = 0
    missing = []
    for path in files:
        parser = LinkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        for raw_link in parser.links:
            if raw_link.startswith(("http://", "https://", "mailto:", "javascript:")):
                continue
            if raw_link.startswith("#"):
                continue
            link, _ = urldefrag(raw_link)
            if not link:
                continue
            parsed = urlparse(link)
            if parsed.scheme:
                continue
            target = (path.parent / link).resolve()
            checked += 1
            if not target.exists():
                missing.append((path, raw_link))
    return checked, missing


def check_banned(files):
    hits = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for pattern in BANNED_PATTERNS:
            haystack = lower if pattern.isascii() else text
            needle = pattern.lower() if pattern.isascii() else pattern
            if needle in haystack:
                hits.append((path, pattern))
    return hits


def check_required(files, snippets, label):
    failures = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in text:
                failures.append((label, path, snippet))
    return failures


def check_bibliography_markup(files):
    failures = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        if '<div class="bib-ref">' in text:
            failures.append((path, "bib-ref uses div instead of p"))
    return failures


def main():
    files = generated_html_files()
    chapter_files = [
        path for path in files
        if path.name == "index.html" and "\\module-" in str(path)
    ]
    section_files = [path for path in files if path.name.startswith("section-")]
    checked, missing = check_links(files)
    banned = check_banned(files)
    required = []
    required.extend(check_required(chapter_files, REQUIRED_CHAPTER_SNIPPETS, "chapter"))
    required.extend(check_required(section_files, REQUIRED_SECTION_SNIPPETS, "section"))
    bib = check_bibliography_markup(files)
    print(f"html_files={len(files)}")
    print(f"chapter_files={len(chapter_files)}")
    print(f"section_files={len(section_files)}")
    print(f"links_checked={checked}")
    print(f"missing_links={len(missing)}")
    print(f"banned_hits={len(banned)}")
    print(f"required_failures={len(required)}")
    print(f"bibliography_markup_failures={len(bib)}")
    for path, link in missing[:20]:
        print(f"MISSING_LINK {path.relative_to(ROOT)} {link}")
    for path, pattern in banned[:20]:
        print(f"BANNED {path.relative_to(ROOT)} {pattern}")
    for label, path, snippet in required[:20]:
        print(f"REQUIRED {label} {path.relative_to(ROOT)} {snippet}")
    for path, issue in bib[:20]:
        print(f"BIB {path.relative_to(ROOT)} {issue}")
    raise SystemExit(1 if missing or banned or required or bib else 0)


if __name__ == "__main__":
    main()
