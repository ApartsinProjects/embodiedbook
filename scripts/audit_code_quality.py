from __future__ import annotations

import ast
import csv
import html
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audit" / "code_quality.csv"


PLACEHOLDER_RE = re.compile(
    r"\b(todo|placeholder|example_value|value_example|metric_example|section_example|fill in|dummy)\b",
    re.I,
)


def code_blocks(path: Path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for i, code in enumerate(soup.select("pre code"), start=1):
        text = html.unescape(code.get_text("\n"))
        klass = " ".join(code.get("class", []))
        yield i, klass, text


def ast_shape(src: str) -> dict[str, int | bool]:
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"syntax_error": True, "defs": 0, "calls": 0, "asserts": 0, "classes": 0, "assigns": 0}
    calls = sum(isinstance(n, ast.Call) for n in ast.walk(tree))
    defs = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in ast.walk(tree))
    asserts = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
    classes = sum(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
    assigns = sum(isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)) for n in ast.walk(tree))
    return {
        "syntax_error": False,
        "defs": defs,
        "calls": calls,
        "asserts": asserts,
        "classes": classes,
        "assigns": assigns,
    }


def flag_block(src: str, klass: str) -> list[str]:
    stripped = src.strip()
    lines = [ln for ln in stripped.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]
    flags: list[str] = []
    if re.match(r"^(pip|uv|conda|python -m pip|npm|git)\s+", stripped):
        return flags
    if PLACEHOLDER_RE.search(stripped):
        flags.append("placeholder_text")
    is_python = "language-python" in klass or re.search(
        r"^\s*(from |import |@dataclass|class |def |print\(|assert |for |if )", stripped, re.M
    )
    if len(lines) < 4 and is_python:
        flags.append("too_short")
    if is_python:
        shape = ast_shape(stripped)
        if shape["syntax_error"]:
            flags.append("python_syntax_error")
        else:
            if shape["classes"] and not shape["defs"] and shape["calls"] <= 2:
                flags.append("class_or_dataclass_only")
            has_observable = "print(" in stripped or re.search(r"^\s*assert\s+", stripped, re.M)
            if shape["assigns"] and not shape["defs"] and not shape["asserts"] and shape["calls"] <= 1 and not has_observable:
                flags.append("assignment_only")
            if shape["calls"] == 0 and shape["asserts"] == 0 and shape["defs"] == 0:
                flags.append("no_computation_or_check")
            if "print(" not in stripped and "assert " not in stripped and shape["defs"] == 0 and shape["calls"] <= 1:
                flags.append("no_observable_output")
    return flags


def main() -> int:
    rows = []
    for path in sorted(ROOT.glob("part-*/*/section-*.html")):
        for index, klass, src in code_blocks(path):
            flags = flag_block(src, klass)
            if flags:
                rows.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "block": index,
                        "class": klass,
                        "flags": ";".join(sorted(set(flags))),
                        "preview": " ".join(src.strip().split())[:220],
                    }
                )
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "block", "class", "flags", "preview"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"issues={len(rows)}")
    print(f"report={OUT}")
    return 1 if rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
