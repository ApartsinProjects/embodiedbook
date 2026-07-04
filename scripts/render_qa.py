r"""render_qa.py - visual QA cycle for a built EPUB.

Extracts the EPUB, serves it over HTTP (so KaTeX web fonts + images load exactly
as a reader would), auto-selects the HARDEST pages by heuristic (most math, most
images, tables, code, widest callout variety), and renders each full chapter to a
PNG for eyeball inspection. Also always includes any pages named on the CLI.

This is the "render actual output, don't trust the source" discipline: browser
audits of source HTML miss reader-only artifacts (unloaded lazy images, missing
math fonts, leaked web chrome, KFX black boxes).

Usage:
  python scripts/render_qa.py KDP/output/building-embodied-ai.epub            # auto-pick 12 hardest
  python scripts/render_qa.py KDP/output/building-embodied-ai.epub -n 20
  python scripts/render_qa.py KDP/output/building-embodied-ai.epub --match 1.8 33.2
Output PNGs land in <epub_dir>/_renderqa/.
"""
import sys, re, zipfile, shutil, functools, http.server, socketserver, threading, argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("epub")
ap.add_argument("-n", type=int, default=12, help="how many auto-selected hard pages")
ap.add_argument("--match", nargs="*", default=[], help="substrings; always render chapters whose name/text matches")
ap.add_argument("--width", type=int, default=720)
a = ap.parse_args()

EPUB = Path(a.epub)
WORK = EPUB.parent / "_renderqa"
if WORK.exists():
    shutil.rmtree(WORK)
WORK.mkdir(parents=True)
with zipfile.ZipFile(EPUB) as z:
    z.extractall(WORK)

chap_dir = WORK / "EPUB" / "chapters"
chapters = sorted(chap_dir.glob("*.xhtml"))


def score(text):
    """Difficulty heuristic: reward math, images, tables, code, callout variety."""
    katex = text.count('class="katex')
    imgs = text.count("<img")
    tables = text.count("<table")
    code = text.count("<pre")
    callouts = len(set(re.findall(r'callout\s+([a-z-]+)', text)))
    svgs = text.count("<svg")
    # weight so a page that combines several hard features ranks highest
    return katex * 1 + imgs * 40 + tables * 60 + code * 15 + callouts * 25 + svgs * 20


scored = []
for c in chapters:
    t = c.read_text(encoding="utf-8")
    scored.append((score(t), c, t))
scored.sort(key=lambda x: -x[0])

picked, seen = [], set()
# always-include CLI matches
for s, c, t in scored:
    if any(m.lower() in c.name.lower() or m.lower() in t.lower()[:4000] for m in a.match):
        picked.append(c); seen.add(c.name)
# then top-N hardest
for s, c, t in scored:
    if len(picked) >= a.n + len(a.match):
        break
    if c.name not in seen:
        picked.append(c); seen.add(c.name)

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(WORK))
class TS(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True; daemon_threads = True
httpd = TS(("127.0.0.1", 0), Handler)
PORT = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()

print(f"rendering {len(picked)} pages to {WORK}")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=2, viewport={"width": a.width, "height": 1100})
    for i, c in enumerate(picked):
        pg.goto(f"http://127.0.0.1:{PORT}/EPUB/chapters/{c.name}", wait_until="networkidle")
        pg.evaluate("""async()=>{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>{})));await document.fonts.ready;}""")
        pg.wait_for_timeout(400)
        out = WORK / f"qa_{i:02d}_{c.name[:40]}.png"
        pg.screenshot(path=str(out), full_page=True)
        print(f"  [{i+1}/{len(picked)}] {c.name[:60]}")
    b.close()
httpd.shutdown()
print("done ->", WORK)
