"""
audit_render_kpf.py — Render N random content chapters from the KFX-clean Kindle EPUB
(the exact content packed into the .kpf) to PNG for a visual audit of math, layout,
typesetting, and callouts. Serves over local HTTP so Chromium loads fonts/images.

Usage: python audit_render_kpf.py <kindle.epub> [N] [seed]
Output: KDP/output/audit/page_NN_<chapter>.png
"""
import sys, zipfile, shutil, threading, functools, http.server, socketserver, random
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
EPUB = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "KDP/output/building-embodied-ai-kindle-mz.epub"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 10
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 42
WORK = ROOT / "KDP/output/_audit_extract"
OUT = ROOT / "KDP/output/audit"

if WORK.exists():
    shutil.rmtree(WORK)
WORK.mkdir(parents=True)
OUT.mkdir(parents=True, exist_ok=True)
for p in OUT.glob("*.png"):
    p.unlink()

with zipfile.ZipFile(EPUB) as z:
    z.extractall(WORK)

chapters_dir = WORK / "EPUB" / "chapters"
all_ch = sorted(chapters_dir.glob("*.xhtml"))
# keep content chapters: drop front-matter, index, nav, appendix TOC-only
content = [c for c in all_ch if not any(k in c.name.lower()
           for k in ("front-matter", "nav", "index", "cover", "toc"))]
random.seed(SEED)
picks = sorted(random.sample(content, min(N, len(content))), key=lambda p: p.name)
print("chapters chosen:")
for p in picks:
    print("  ", p.name)

# serve WORK over HTTP
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(WORK))
httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
port = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()

results = []
with sync_playwright() as pw:
    br = pw.chromium.launch()
    # e-reader-ish content width, 2x for crispness
    page = br.new_page(viewport={"width": 840, "height": 1400}, device_scale_factor=2)
    for i, ch in enumerate(picks, 1):
        url = f"http://127.0.0.1:{port}/EPUB/chapters/{ch.name}"
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(400)
        try:
            page.evaluate("() => Promise.all(document.fonts ? [...document.fonts].map(f=>f.load()) : [])")
        except Exception:
            pass
        page.wait_for_timeout(200)
        out = OUT / f"page_{i:02d}_{ch.stem[:40]}.png"
        page.screenshot(path=str(out), full_page=True)
        results.append(out.name)
        print(f"  [{i}/{len(picks)}] {out.name}")
    br.close()

httpd.shutdown()
print("\nwrote", len(results), "audit renders to", OUT)
