from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_RUNNER = Path(r"E:\Projects\claude-skills\book-skills\scripts\audit\run.py")


def build_argv(args: argparse.Namespace) -> list[str]:
    argv = [str(SKILL_RUNNER), "--root", str(REPO_ROOT)]
    if args.priority:
        argv.extend(["--priority", args.priority])
    if args.checks:
        argv.extend(["--checks", args.checks])
    if args.files:
        argv.append("--files")
        argv.extend(args.files)
    if args.json:
        argv.append("--json")
    if args.list:
        argv.append("--list")
    return argv


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the canonical book-skills audit runner against this book."
    )
    parser.add_argument("--priority", help="Filter by priority, for example P0 or P0+P1")
    parser.add_argument("--checks", help="Comma-separated check IDs to run")
    parser.add_argument("--files", nargs="*", help="Only scan files matching these substrings")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parser.add_argument("--list", action="store_true", help="List available checks")
    args = parser.parse_args()

    if not SKILL_RUNNER.exists():
        raise SystemExit(f"book-skills audit runner not found: {SKILL_RUNNER}")

    old_argv = sys.argv[:]
    try:
        sys.argv = build_argv(args)
        runpy.run_path(str(SKILL_RUNNER), run_name="__main__")
    finally:
        sys.argv = old_argv


if __name__ == "__main__":
    main()
