"""
prep_kdp_cover.py — Produce a KDP-compliant cover from images/book-cover.jpg.

KDP cover spec targeted:
  - 1600 x 2560 px (ideal; 1.6:1 height:width)
  - baseline (NOT progressive) JPEG
  - sRGB color, embedded sRGB ICC profile (KDP silently rejects covers w/ stripped/absent ICC)
  - high quality, well under 50 MB

Output: KDP/cover/book-cover-kdp.jpg
"""
from pathlib import Path
from PIL import Image, ImageCms
import io

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "images" / "book-cover.jpg"
OUTDIR = ROOT / "KDP" / "cover"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "book-cover-kdp.jpg"

TARGET_W, TARGET_H = 1600, 2560

img = Image.open(SRC)
print(f"source: {img.width}x{img.height} {img.mode}")

if img.mode != "RGB":
    img = img.convert("RGB")

# Preserve 1.6:1 — source is already 1000x1600 (=1.6), so a straight resize is exact.
ratio = TARGET_H / TARGET_W
if abs(img.height / img.width - ratio) > 0.01:
    print(f"  WARN: source aspect {img.width}x{img.height} != 1.6:1; center-cropping to fit")
    # center-crop to 1.6:1 before upscale
    if img.width * ratio > img.height:
        new_w = int(img.height / ratio)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, img.height))
    else:
        new_h = int(img.width * ratio)
        top = (img.height - new_h) // 2
        img = img.crop((0, top, img.width, top + new_h))

up = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)

# Embed a standard sRGB ICC profile
srgb = ImageCms.createProfile("sRGB")
icc_bytes = ImageCms.ImageCmsProfile(srgb).tobytes()

up.save(
    OUT,
    "JPEG",
    quality=92,
    optimize=True,
    progressive=False,   # baseline, required for KFX/KDP reliability
    icc_profile=icc_bytes,
    dpi=(300, 300),
)

# Verify
v = Image.open(OUT)
size_mb = OUT.stat().st_size / 1e6
has_icc = "icc_profile" in v.info and bool(v.info["icc_profile"])
# progressive check
raw = OUT.read_bytes()
is_progressive = b"\xff\xc2" in raw[:2000] or (b"\xff\xc2" in raw)
print(f"\nwrote {OUT}")
print(f"  {v.width}x{v.height} {v.mode}, {size_mb:.2f} MB")
print(f"  baseline JPEG: {not is_progressive}")
print(f"  sRGB ICC embedded: {has_icc}")
print(f"  KDP-ideal 1600x2560: {v.width==TARGET_W and v.height==TARGET_H}")
