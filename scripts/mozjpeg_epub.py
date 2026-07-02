"""
mozjpeg_epub.py — Lossless MozJPEG (Huffman-optimization) pass over every JPEG in
an EPUB, repacked correctly (mimetype first + STORED). Skips cover.jpg to preserve
its ICC profile (KDP rejects covers with stripped ICC).

Usage: python mozjpeg_epub.py <in.epub> <out.epub>
"""
import sys, zipfile, io
import mozjpeg_lossless_optimization as mz

src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src)
names = zin.namelist()

# mimetype must be first and stored
ordered = [n for n in names if n == "mimetype"] + [n for n in names if n != "mimetype"]

saved = 0
opt_count = 0
with zipfile.ZipFile(dst, "w") as zout:
    for n in ordered:
        data = zin.read(n)
        if n == "mimetype":
            zout.writestr(n, data, compress_type=zipfile.ZIP_STORED)
            continue
        if n.lower().endswith((".jpg", ".jpeg")) and not n.lower().endswith("cover.jpg"):
            try:
                out = mz.optimize(data)
                if len(out) < len(data):
                    saved += len(data) - len(out)
                    opt_count += 1
                    data = out
            except Exception as e:
                print(f"  skip {n}: {e}")
        zout.writestr(n, data, compress_type=zipfile.ZIP_DEFLATED)

import os
print(f"optimized {opt_count} JPEGs, saved {saved/1e6:.1f} MB")
print(f"  {os.path.getsize(src)/1e6:.1f} MB -> {os.path.getsize(dst)/1e6:.1f} MB")
