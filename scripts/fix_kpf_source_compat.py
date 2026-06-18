from __future__ import annotations

import argparse
import re
import textwrap
from pathlib import Path

from bs4 import BeautifulSoup


DEFAULT_SKIP = (
    "node_modules",
    ".git",
    "output",
    "backup",
    "pagefind",
    "temp_epub",
    "templates/",
    "KDP/build",
    "KDP/html2epub",
)

WRAPPER_CLASSES = {
    "comparison-table",
    "table-wrapper",
    "table-container",
    "wide-table",
    "complex-table-wrap",
    "table-wide-wrap",
}

KW_STRING = re.compile(r'^(\s*[A-Za-z_][A-Za-z0-9_]*\s*=\s*)"([^"]*)"(,?)\s*$')
CALL_LINE = re.compile(r"^(\s*)([A-Za-z_][A-Za-z0-9_]*)\((.*)\)(,?)\s*$")
DICT_STRING = re.compile(r'^(\s*)"([^"]+)":\s*"([^"]*)"(,?)\s*$')
DICT_OBJECT = re.compile(r'^(\s*)"([^"]+)":\s*(\{.*\})(,?)\s*$')


def skipped(path: Path, skip: tuple[str, ...]) -> bool:
    text = str(path).replace("\\", "/")
    return any(item in text for item in skip)


def wrap_comment(line: str, width: int) -> list[str]:
    indent = line[: len(line) - len(line.lstrip())]
    body = line.lstrip()[1:].strip()
    wrapped = textwrap.wrap(
        body,
        width=max(24, width - len(indent) - 2),
        break_long_words=False,
        break_on_hyphens=False,
    )
    return [f"{indent}# {part}" for part in wrapped] or [line]


def wrap_kw_string(line: str, width: int) -> list[str] | None:
    match = KW_STRING.match(line)
    if not match:
        return None
    prefix, value, comma = match.groups()
    indent = prefix[: len(prefix) - len(prefix.lstrip())]
    child_indent = indent + "    "
    chunk_width = max(24, width - len(child_indent) - 2)
    chunks = textwrap.wrap(
        value,
        width=chunk_width,
        break_long_words=False,
        break_on_hyphens=False,
    )
    if len(chunks) <= 1 and len(line) <= width:
        return [line]
    out = [f"{prefix}("]
    out.extend(f'{child_indent}"{chunk}"' for chunk in chunks)
    out.append(f"{indent}){comma}")
    return out


def split_args(text: str) -> list[str]:
    args: list[str] = []
    current: list[str] = []
    quote = ""
    depth = 0
    escape = False
    for char in text:
        if escape:
            current.append(char)
            escape = False
            continue
        if char == "\\":
            current.append(char)
            escape = True
            continue
        if quote:
            current.append(char)
            if char == quote:
                quote = ""
            continue
        if char in ("'", '"'):
            quote = char
            current.append(char)
            continue
        if char in "([{":
            depth += 1
            current.append(char)
            continue
        if char in ")]}":
            depth -= 1
            current.append(char)
            continue
        if char == "," and depth == 0:
            args.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    tail = "".join(current).strip()
    if tail:
        args.append(tail)
    return args


def wrap_call_line(line: str, width: int) -> list[str] | None:
    if len(line) <= width or "," not in line:
        return None
    match = CALL_LINE.match(line)
    if not match:
        return None
    indent, name, args_text, comma = match.groups()
    args = split_args(args_text)
    if len(args) < 2:
        return None
    child_indent = indent + "    "
    out = [f"{indent}{name}("]
    out.extend(f"{child_indent}{arg}," for arg in args)
    out.append(f"{indent}){comma}")
    return out


def wrap_dict_entry(line: str, width: int) -> list[str] | None:
    if len(line) <= width:
        return None
    string_match = DICT_STRING.match(line)
    if string_match:
        indent, key, value, comma = string_match.groups()
        child_indent = indent + "    "
        chunks = textwrap.wrap(
            value,
            width=max(24, width - len(child_indent) - 2),
            break_long_words=False,
            break_on_hyphens=False,
        )
        out = [f'{indent}"{key}": (']
        out.extend(f'{child_indent}"{chunk}"' for chunk in chunks)
        out.append(f"{indent}){comma}")
        return out

    object_match = DICT_OBJECT.match(line)
    if object_match:
        indent, key, value, comma = object_match.groups()
        inner = value.strip()[1:-1]
        parts = split_args(inner)
        if len(parts) < 2:
            return None
        child_indent = indent + "    "
        out = [f'{indent}"{key}": {{']
        out.extend(f"{child_indent}{part}," for part in parts)
        out.append(f"{indent}}}{comma}")
        return out
    return None


def wrap_print_dict(line: str, width: int) -> list[str] | None:
    if len(line) <= width or not line.strip().startswith("print({"):
        return None
    indent = line[: len(line) - len(line.lstrip())]
    stripped = line.strip()
    if not stripped.startswith("print({") or not stripped.endswith("})"):
        return None
    inner = stripped[len("print({") : -len("})")]
    parts = split_args(inner)
    if len(parts) < 2:
        return None
    child_indent = indent + "    "
    out = [f"{indent}print({{"]
    out.extend(f"{child_indent}{part}," for part in parts)
    out.append(f"{indent}}})")
    return out


def wrap_code_text(text: str, width: int) -> tuple[str, bool]:
    changed = False
    out: list[str] = []
    for line in text.split("\n"):
        if len(line) <= width:
            out.append(line)
            continue
        if line.lstrip().startswith("#"):
            out.extend(wrap_comment(line, width))
            changed = True
            continue
        wrapped_kw = wrap_kw_string(line, width)
        if wrapped_kw:
            out.extend(wrapped_kw)
            changed = True
            continue
        wrapped_call = wrap_call_line(line, width)
        if wrapped_call:
            out.extend(wrapped_call)
            changed = True
            continue
        wrapped_dict = wrap_dict_entry(line, width)
        if wrapped_dict:
            out.extend(wrapped_dict)
            changed = True
            continue
        wrapped_print = wrap_print_dict(line, width)
        if wrapped_print:
            out.extend(wrapped_print)
            changed = True
            continue
        out.append(line)
    return "\n".join(out), changed


def table_is_wrapped(table) -> bool:
    parent = table.parent
    for _ in range(2):
        if not parent:
            return False
        if parent.name == "div" and WRAPPER_CLASSES.intersection(parent.get("class", [])):
            return True
        parent = parent.parent
    return False


def details_to_static_block(soup: BeautifulSoup, details) -> bool:
    summary = details.find("summary", recursive=False)
    title = summary.get_text(" ", strip=True) if summary else "Details"

    block = soup.new_tag("div")
    classes = ["kindle-disclosure"]
    classes.extend(details.get("class", []))
    block["class"] = classes

    heading = soup.new_tag("p")
    heading["class"] = "kindle-disclosure-title"
    heading.string = title
    block.append(heading)

    for child in list(details.contents):
        if child is summary:
            child.extract()
            continue
        block.append(child.extract())

    details.replace_with(block)
    return True


def fix_file(path: Path, width: int) -> bool:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    changed = False

    for details in soup.find_all("details"):
        changed = details_to_static_block(soup, details) or changed

    for table in soup.find_all("table"):
        for code in table.find_all("code"):
            code.name = "span"
            classes = [c for c in code.get("class", []) if not c.startswith("language-")]
            classes.append("code-inline")
            code["class"] = classes
            changed = True
        if not table_is_wrapped(table):
            wrapper = soup.new_tag("div")
            wrapper["class"] = "table-wrapper"
            table.wrap(wrapper)
            changed = True

    for code in soup.select("pre code"):
        fixed, code_changed = wrap_code_text(code.get_text(), width)
        if code_changed:
            code.clear()
            code.append(fixed)
            changed = True

    if changed:
        path.write_text(str(soup), encoding="utf-8", newline="\n")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--width", type=int, default=100)
    args = parser.parse_args()

    root = args.root.resolve()
    changed = []
    for path in root.rglob("*.html"):
        if skipped(path, DEFAULT_SKIP):
            continue
        if fix_file(path, args.width):
            changed.append(path.relative_to(root))

    print(f"Updated {len(changed)} HTML files for KPF source compatibility.")
    for path in changed[:40]:
        print(f"  {path}")
    if len(changed) > 40:
        print(f"  ... {len(changed) - 40} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
