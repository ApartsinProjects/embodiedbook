from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENRICH = ROOT / "scripts" / "enrich_depth_gap_sections.py"


spec = importlib.util.spec_from_file_location("enrich_depth_gap_sections", ENRICH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def main() -> None:
    paths = sorted((ROOT / "part-6-embodied-perception").glob("module-*/section-*.html"))
    changed = 0
    skipped = 0
    for full in paths:
        rel = str(full.relative_to(ROOT)).replace("\\", "/")
        raw = full.read_text(encoding="utf-8")
        updated, did = module.insert_core(raw, rel)
        if did:
            full.write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
        else:
            skipped += 1
    print(f"part_vi_sections={len(paths)}")
    print(f"changed={changed}")
    print(f"skipped={skipped}")


if __name__ == "__main__":
    main()
