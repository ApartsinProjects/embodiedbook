"""Anti-boilerplate audit for Building Embodied AI.

This audit inverts the old depth audit. The old gate (audit_book_depth.py) FAILED
sections for being short, which incentivized template padding. This gate FAILS the
build when template scaffolding is duplicated across the corpus or when known filler
code appears at all.

A signature is "boilerplate" if rewriting the section's topic name would leave the
text unchanged. Such text must appear in at most TEMPLATE_MAX_FILES sections.
Filler code must appear in zero sections.

Run:
    C:\\Python314\\python.exe scripts\\audit_boilerplate.py
Exit code is nonzero when any gate fails.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Template prose / structure signatures. These are instantiated per section with the
# topic name slotted in, so they read identically across the book. Allowed in a few
# files only (a signature may legitimately survive in a handful of places).
TEMPLATE_SIGNATURES = [
    "Reader Pathway",
    "Use this section to make",
    "Builder's Deep Dive",
    "Implementation Recipe",
    "Failure Analysis Pattern",
    "Practical Tool Choices For Section",
    "What This Section Develops",
    "should be placed inside the closed-loop transition",
    "ready for comparison",
    "Build a Section Evidence Trace",
    "Build the Chapter Evidence Artifact",
    "Production Notes For Readers",
    "Instructor And Builder Notes",
]

# Filler code signatures. These functions/identifiers are topic-agnostic dictionary
# bookkeeping or non-sequitur snippets. They must not appear anywhere.
FILLER_CODE_SIGNATURES = [
    "plan = [skill for skill in skills]",
    "def missing_contract_fields",
    "def summarize_baseline",
    "def summarize_shortcut",
    "def summarize_perturbed",
    "class EvidenceRecord",
    "def evidence_ready",
    "def embodied_error_ledger",
    'instruction = "run the',  # "run the <topic> diagnostic" filler
]

# Fabricated metric pairs used in the cloned toy labs.
FABRICATED_METRIC_SIGNATURES = [
    '"value": 0.72',
    '"value": 0.78',
    '"success": 0.82',
    '"success": 0.86',
]

# A template signature may survive in at most this many files before it is a defect.
TEMPLATE_MAX_FILES = 3


def section_files():
    out = []
    for path in ROOT.rglob("*.html"):
        if "templates" in path.parts or "archive" in path.parts:
            continue
        if path.name.startswith("section-") or (
            path.name == "index.html" and "module-" in str(path)
        ):
            out.append(path)
    return sorted(out)


def main():
    files = section_files()
    template_hits = {sig: [] for sig in TEMPLATE_SIGNATURES}
    filler_hits = {sig: [] for sig in FILLER_CODE_SIGNATURES}
    fabricated_hits = {sig: [] for sig in FABRICATED_METRIC_SIGNATURES}

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for sig in TEMPLATE_SIGNATURES:
            if sig in text:
                template_hits[sig].append(rel)
        for sig in FILLER_CODE_SIGNATURES:
            if sig in text:
                filler_hits[sig].append(rel)
        for sig in FABRICATED_METRIC_SIGNATURES:
            if sig in text:
                fabricated_hits[sig].append(rel)

    print(f"files_scanned={len(files)}")
    print(f"template_max_files={TEMPLATE_MAX_FILES}")
    print("")

    failures = 0

    print("== template prose signatures (defect when count > template_max_files) ==")
    for sig in TEMPLATE_SIGNATURES:
        n = len(template_hits[sig])
        status = "FAIL" if n > TEMPLATE_MAX_FILES else "ok"
        if n > TEMPLATE_MAX_FILES:
            failures += 1
        print(f"[{status}] {n:>4}  {sig}")

    print("")
    print("== filler code signatures (defect when count > 0) ==")
    for sig in FILLER_CODE_SIGNATURES:
        n = len(filler_hits[sig])
        status = "FAIL" if n > 0 else "ok"
        if n > 0:
            failures += 1
        print(f"[{status}] {n:>4}  {sig}")

    print("")
    print("== fabricated metric signatures (defect when count > 0) ==")
    for sig in FABRICATED_METRIC_SIGNATURES:
        n = len(fabricated_hits[sig])
        status = "FAIL" if n > 0 else "ok"
        if n > 0:
            failures += 1
        print(f"[{status}] {n:>4}  {sig}")

    # Show a few example files for the worst offenders to make remediation actionable.
    print("")
    print("== worst offenders (examples) ==")
    ranked = sorted(
        ((len(v), k, v) for k, v in template_hits.items() if len(v) > TEMPLATE_MAX_FILES),
        reverse=True,
    )
    for n, sig, hits in ranked[:5]:
        print(f"{sig} ({n} files), e.g.:")
        for rel in hits[:3]:
            print(f"    {rel}")

    print("")
    print(f"total_gate_failures={failures}")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
