"""Phase A de-scaffolding sweep for Building Embodied AI.

Removes known scaffold blocks from section HTML files while
preserving genuine topic-specific content.

What is REMOVED:
  - <div class="callout pathway"> (entire element; always "Reader Pathway")
  - <h2>What This Section Develops</h2> (heading tag only; content below kept)
  - <h2>Builder's Deep Dive</h2>  (heading tag only)
  - <h2>Implementation Recipe</h2>  (heading tag only)
  - <h2>Failure Analysis Pattern</h2>  (heading tag only)
  - <section class="production-depth-expansion"> wrapper (unwrapped; children kept)
  - <div class="callout tip"> where title is "Teaching Move" or "Instructor And Builder Notes"
  - <div class="comparison-table-title"> that says "Practical Tool Choices For Section..."
  - Template epigraph sentence "...matters when the next action changes the evidence..."
  - The filler sentence "For [Topic], the PPO dependency is concrete:"
  - The filler sentence "should be placed inside the closed-loop transition"
  - <pre><code> blocks that contain banned filler code signatures (+ their output/caption)
  - <div class="callout lab"> or <section> whose title is "Build a Section Evidence Trace"
    or "Build the Chapter Evidence Artifact"
  - Fabricated metric sentences referencing 0.72/0.78/0.82/0.86

What is PRESERVED (explicitly NOT removed):
  - All content paragraphs and code blocks below the banned headings
  - Comparison tables themselves (only the generic title div is removed if applicable)
  - Topic-specific worked examples
  - All fun-note, key-insight, research-frontier, key-takeaway, warning callouts
  - epigraph figure, illustration, and cite elements
  - Bibliography, navigation, header, footer

Run:
    C:\\Python314\\python.exe scripts\\phase_a_descaffold.py [--dry-run]
"""
import argparse
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Comment

ROOT = Path(__file__).resolve().parents[1]

# ── Section file discovery ───────────────────────────────────────────────────
def section_files():
    out = []
    for path in ROOT.rglob("*.html"):
        if "templates" in path.parts or "archive" in path.parts:
            continue
        if "DEEP_CONTENT_AUDIT" in str(path):
            continue
        if path.name.startswith("section-") or (
            path.name == "index.html" and "module-" in str(path)
        ):
            out.append(path)
    return sorted(out)


# ── Banned patterns ──────────────────────────────────────────────────────────

# h2/h3 headings to delete (tag only, not content that follows)
BANNED_HEADINGS = {
    "What This Section Develops",
    "Builder's Deep Dive",
    "Implementation Recipe",
    "Failure Analysis Pattern",
    "Instructor And Builder Notes",
    "Production Notes For Readers",
}

# callout-title text where entire parent callout div is deleted
BANNED_CALLOUT_TITLES_DELETE_ALL = {
    "Reader Pathway",
    "Teaching Move",
    "Instructor And Builder Notes",
    "Production Notes For Readers",
}

# Lab/exercise titles where the entire enclosing callout/section is deleted
BANNED_LAB_TITLES = {
    "Build a Section Evidence Trace",
    "Build the Chapter Evidence Artifact",
    "Hands-On Lab: Build",
}

# Substrings in <p> inside epigraph that mark a template clone
TEMPLATE_EPIGRAPH_SUBSTRINGS = [
    "matters when the next action changes the evidence you thought you had",
    "should be placed inside the closed-loop transition",
]

# Substrings in a standalone <p> (outside code) that mark filler prose
FILLER_PROSE_SUBSTRINGS = [
    "the PPO dependency is concrete",
    "ready for comparison",
    "should be placed inside the closed-loop transition",
]

# Substrings in <pre><code> blocks that identify filler code
FILLER_CODE_SIGNATURES = [
    "plan = [skill for skill in skills]",
    "def missing_contract_fields",
    "def summarize_baseline",
    "def summarize_shortcut",
    "def summarize_perturbed",
    "class EvidenceRecord",
    "def evidence_ready",
    "def embodied_error_ledger",
    'instruction = "run the',
    "class SkillEvidence",
    "class SectionContract",
    "[{\"section\":",
    "EmbodiedStep(",
    "def score_section",
    "[skill for skill in",
]

# Fabricated metric signatures anywhere in text
FABRICATED_METRIC_SIGS = [
    '"value": 0.72',
    '"value": 0.78',
    '"success": 0.82',
    '"success": 0.86',
]


# ── Helper ───────────────────────────────────────────────────────────────────

def callout_title_text(tag):
    """Return the text of the .callout-title child, or '' if absent."""
    ct = tag.find(class_="callout-title")
    return ct.get_text(strip=True) if ct else ""

def is_banned_callout(tag):
    """True if this <div class='callout ...'> should be deleted entirely."""
    if "callout" not in tag.get("class", []):
        return False
    title = callout_title_text(tag)
    return title in BANNED_CALLOUT_TITLES_DELETE_ALL

def is_banned_lab(tag):
    """True if this callout or section is an evidence-artifact lab."""
    title = callout_title_text(tag)
    if not title:
        # also check for h2/h3 inside
        h = tag.find(["h2", "h3"])
        title = h.get_text(strip=True) if h else ""
    for banned in BANNED_LAB_TITLES:
        if title.startswith(banned) or banned in title:
            return True
    return False

def contains_filler_code(pre_tag):
    """True if a <pre><code> block contains any banned filler signature."""
    code = pre_tag.find("code")
    text = code.get_text() if code else pre_tag.get_text()
    return any(sig in text for sig in FILLER_CODE_SIGNATURES)

def contains_fabricated_metric(pre_tag):
    """True if a <pre><code> block contains fabricated metric numbers."""
    code = pre_tag.find("code")
    text = code.get_text() if code else pre_tag.get_text()
    return any(sig in text for sig in FABRICATED_METRIC_SIGS)

def remove_pre_with_siblings(pre_tag):
    """Remove <pre>, its following .code-output and .code-caption siblings."""
    siblings_to_remove = []
    nxt = pre_tag.next_sibling
    while nxt:
        if isinstance(nxt, NavigableString):
            nxt = nxt.next_sibling
            continue
        cls = nxt.get("class", [])
        if "code-output" in cls or "code-caption" in cls:
            siblings_to_remove.append(nxt)
            nxt = nxt.next_sibling
        else:
            break
    pre_tag.decompose()
    for s in siblings_to_remove:
        s.decompose()


# ── Per-file transform ───────────────────────────────────────────────────────

def descaffold(path: Path) -> tuple[bool, list[str]]:
    """
    Apply Phase A de-scaffolding to one HTML file.
    Returns (changed: bool, actions: list[str]).
    """
    original = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")
    actions = []

    main = soup.find("main") or soup.find("body") or soup

    # 1. Remove entire banned callout divs (Reader Pathway, Teaching Move, etc.)
    for tag in main.find_all("div", class_="callout"):
        if is_banned_callout(tag):
            title = callout_title_text(tag)
            tag.decompose()
            actions.append(f"REMOVED callout '{title}'")

    # 2. Remove evidence-artifact lab callouts and sections
    for tag_name in ["div", "section"]:
        for tag in main.find_all(tag_name):
            if tag.decomposed:
                continue
            if "callout" in tag.get("class", []) and is_banned_lab(tag):
                title = callout_title_text(tag)
                tag.decompose()
                actions.append(f"REMOVED lab callout '{title}'")

    # 3. Unwrap <section class="production-depth-expansion"> (keep children)
    for section in main.find_all("section", class_="production-depth-expansion"):
        section.unwrap()
        actions.append("UNWRAPPED production-depth-expansion section")

    # 4. Remove banned h2/h3 headings (heading tag only; content kept)
    for h in main.find_all(["h2", "h3"]):
        if h.decomposed:
            continue
        text = h.get_text(strip=True)
        if text in BANNED_HEADINGS:
            h.decompose()
            actions.append(f"REMOVED heading '{text}'")

    # 5. Remove template epigraph sentence (the <p> inside <blockquote class="epigraph">)
    epigraph = main.find("blockquote", class_="epigraph")
    if epigraph:
        for p in epigraph.find_all("p"):
            p_text = p.get_text()
            if any(sub in p_text for sub in TEMPLATE_EPIGRAPH_SUBSTRINGS):
                p.decompose()
                actions.append("REMOVED template epigraph sentence")

    # 6. Remove filler prose <p> elements (outside code blocks)
    for p in main.find_all("p"):
        if p.decomposed:
            continue
        # skip <p> inside <pre>
        if p.find_parent("pre"):
            continue
        text = p.get_text()
        if any(sub in text for sub in FILLER_PROSE_SUBSTRINGS):
            p.decompose()
            actions.append(f"REMOVED filler prose paragraph")

    # 7. Remove <div class="comparison-table-title"> saying "Practical Tool Choices..."
    for div in main.find_all("div", class_="comparison-table-title"):
        if div.decomposed:
            continue
        text = div.get_text(strip=True)
        if text.startswith("Practical Tool Choices For Section"):
            div.decompose()
            actions.append(f"REMOVED generic tool table title '{text[:60]}'")

    # 8. Remove <pre><code> blocks containing filler code (+ following output/caption)
    for pre in main.find_all("pre"):
        if pre.decomposed:
            continue
        if contains_filler_code(pre) or contains_fabricated_metric(pre):
            remove_pre_with_siblings(pre)
            actions.append("REMOVED filler/fabricated code block")

    # 9. Remove any remaining <p> or inline text with fabricated metric signatures
    #    (catches them outside code blocks, e.g. in narrative)
    for p in main.find_all("p"):
        if p.decomposed:
            continue
        text = p.get_text()
        if any(sig in text for sig in FABRICATED_METRIC_SIGS):
            p.decompose()
            actions.append("REMOVED fabricated metric paragraph")

    if not actions:
        return False, []

    new_html = str(soup)
    if new_html == original:
        return False, []

    path.write_text(new_html, encoding="utf-8")
    return True, actions


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Phase A de-scaffolding sweep")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report what would change without writing files")
    args = parser.parse_args()

    files = section_files()
    print(f"files_found={len(files)}")
    print(f"dry_run={args.dry_run}")
    print()

    changed_count = 0
    action_totals: dict[str, int] = {}

    for path in files:
        rel = path.relative_to(ROOT)
        try:
            if args.dry_run:
                original = path.read_text(encoding="utf-8")
                soup = BeautifulSoup(original, "html.parser")
                # simulate (parse only, no write)
                changed, actions = descaffold.__wrapped__(path) if hasattr(descaffold, "__wrapped__") else (False, [])
                # for dry-run just report what signatures are present
                hits = []
                if "Reader Pathway" in original:
                    hits.append("Reader Pathway")
                if "What This Section Develops" in original:
                    hits.append("What This Section Develops")
                if "Builder's Deep Dive" in original:
                    hits.append("Builder's Deep Dive")
                if "Implementation Recipe" in original:
                    hits.append("Implementation Recipe")
                if "Failure Analysis Pattern" in original:
                    hits.append("Failure Analysis Pattern")
                if hits:
                    print(f"  WOULD CHANGE: {rel} [{', '.join(hits)}]")
                    changed_count += 1
            else:
                changed, actions = descaffold(path)
                if changed:
                    changed_count += 1
                    for a in actions:
                        # normalise action key
                        key = a.split("'")[0].strip()
                        action_totals[key] = action_totals.get(key, 0) + 1
                    if actions:
                        print(f"  changed: {rel} ({len(actions)} actions)")
        except Exception as exc:
            print(f"  ERROR: {rel}: {exc}", file=sys.stderr)

    print()
    if not args.dry_run:
        print("== Action summary ==")
        for k, v in sorted(action_totals.items(), key=lambda x: -x[1]):
            print(f"  {v:>5}  {k}")
    print()
    print(f"files_changed={changed_count}")


if __name__ == "__main__":
    main()
