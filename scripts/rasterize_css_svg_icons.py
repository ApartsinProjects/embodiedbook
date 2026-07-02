"""
rasterize_css_svg_icons.py — Fix KFX E06405 + W14010/W14012 by rasterizing every
SVG-as-CSS-background in book.css to a transparent PNG and rewriting the url().

- 4 file-based icons:  url('icons/callout-X.svg')  -> url('icons/callout-X.png')
- 5 inline data-URIs:  background-image:url("data:image/svg+xml,...") for classes
  under-the-hood, cross-ref, whats-next, looking-back, production-pattern
  -> rasterized to icons/callout-<class>.png and rewritten to url('icons/callout-<class>.png')

Renders at 128x128 with transparent background (Playwright/Chromium).
"""
import re
import sys
import urllib.parse
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "styles" / "book.css"
ICONS = ROOT / "styles" / "icons"
SIZE = 128

FILE_SVGS = [
    "callout-key-takeaway",
    "callout-lab",
    "callout-self-check",
    "callout-library-shortcut",
]

# class name -> png stem, for the 5 data-uri backgrounds
DATAURI_CLASSES = {
    "under-the-hood": "callout-under-the-hood",
    "cross-ref": "callout-cross-ref",
    "whats-next": "callout-whats-next",
    "looking-back": "callout-looking-back",
    "production-pattern": "callout-production-pattern",
}


def svg_to_png(page, svg_markup, out_path):
    # Force explicit pixel size so viewBox-only SVGs get real intrinsic dims.
    svg_sized = re.sub(r"<svg\b", f'<svg width="{SIZE}" height="{SIZE}"', svg_markup, count=1)
    html = (
        "<!doctype html><html><head><style>"
        "*{margin:0;padding:0}html,body{background:transparent}"
        f"#w{{width:{SIZE}px;height:{SIZE}px}}"
        "</style></head><body>"
        f'<div id="w">{svg_sized}</div></body></html>'
    )
    page.set_content(html, wait_until="networkidle")
    el = page.query_selector("#w")
    el.screenshot(path=str(out_path), omit_background=True)


def main():
    css = CSS.read_text(encoding="utf-8")

    # Collect data-uri SVG markup per class from the CSS.
    datauri_markup = {}
    for cls in DATAURI_CLASSES:
        # match .callout.<cls> .callout-title::before { ... url("data:image/svg+xml,....") ... }
        pat = re.compile(
            r"\.callout\." + re.escape(cls) + r"\s+\.callout-title::before\s*\{[^}]*?"
            r'url\(\s*"data:image/svg\+xml,(?P<data>[^"]+)"\s*\)',
            re.DOTALL,
        )
        m = pat.search(css)
        if not m:
            print(f"  WARN: data-uri for .{cls} not found")
            continue
        raw = m.group("data")
        # data-uri payload is URL-encoded SVG markup
        datauri_markup[cls] = urllib.parse.unquote(raw)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": SIZE, "height": SIZE})

        # 1) file-based svg icons -> png
        for stem in FILE_SVGS:
            svg_file = ICONS / f"{stem}.svg"
            if not svg_file.exists():
                print(f"  WARN: {svg_file} missing")
                continue
            svg_to_png(page, svg_file.read_text(encoding="utf-8"), ICONS / f"{stem}.png")
            print(f"  rasterized {stem}.svg -> {stem}.png")

        # 2) data-uri svgs -> png
        for cls, markup in datauri_markup.items():
            stem = DATAURI_CLASSES[cls]
            svg_to_png(page, markup, ICONS / f"{stem}.png")
            print(f"  rasterized data-uri .{cls} -> {stem}.png")

        browser.close()

    # Rewrite CSS: file .svg -> .png
    for stem in FILE_SVGS:
        css = css.replace(f"icons/{stem}.svg", f"icons/{stem}.png")

    # Rewrite CSS: data-uri -> file png (per class)
    for cls, stem in DATAURI_CLASSES.items():
        pat = re.compile(
            r'(\.callout\.' + re.escape(cls) + r'\s+\.callout-title::before\s*\{[^}]*?background-image:\s*)'
            r'url\(\s*"data:image/svg\+xml,[^"]+"\s*\)',
            re.DOTALL,
        )
        css, n = pat.subn(rf"\1url('icons/{stem}.png')", css)
        if n:
            print(f"  css: .{cls} data-uri -> icons/{stem}.png")

    # Sanity: no SVG backgrounds should remain
    remaining_svg = len(re.findall(r"url\(\s*['\"]?[^'\")]*\.svg", css))
    remaining_datauri = css.count("data:image/svg")
    CSS.write_text(css, encoding="utf-8")
    print(f"\nDONE. remaining .svg url refs: {remaining_svg}, remaining data-uri svg: {remaining_datauri}")
    if remaining_svg or remaining_datauri:
        print("  (nonzero -> inspect book.css manually)")
        sys.exit(1)


if __name__ == "__main__":
    main()
