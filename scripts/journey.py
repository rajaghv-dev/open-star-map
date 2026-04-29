#!/usr/bin/env python3
"""
journey.py — idempotent CLI for editing MY_JOURNEY.md.

Commands:
    list                                   show current active rows
    add    <name> --status S [--notes N] [--link L]
    update <name> --status S [--notes N]
    complete <name> --pr URL --learned "..." [--date YYYY-MM-DD]
    remove <name>

Status values: exploring, learning, good-first-issue, pr-open, merged
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JOURNEY = REPO / "MY_JOURNEY.md"

VALID_STATUS = {"exploring", "learning", "good-first-issue", "pr-open", "merged"}

ACTIVE_HEADER = "## Active projects"
COMPLETED_HEADER = "## Completed contributions"
QUEUE_HEADER = "## Queue (next to explore)"

ACTIVE_TABLE_HEADER = (
    "| Project | Status | Notes | Link |\n"
    "|---------|--------|-------|------|\n"
)
COMPLETED_TABLE_HEADER = (
    "| Project | PR / Contribution | Date | What I learned |\n"
    "|---------|-------------------|------|----------------|\n"
)


def load() -> str:
    return JOURNEY.read_text()


def save(text: str) -> None:
    JOURNEY.write_text(text)


def split_sections(text: str) -> dict[str, list[str]]:
    """Return {header: lines_inside_section} for the three top-level headers."""
    headers = [ACTIVE_HEADER, COMPLETED_HEADER, QUEUE_HEADER]
    sections: dict[str, list[str]] = {h: [] for h in headers}
    cur: str | None = None
    for line in text.splitlines():
        if line.strip() in headers:
            cur = line.strip()
            continue
        if cur is not None:
            if line.startswith("## ") and line.strip() not in headers:
                cur = None
                continue
            sections[cur].append(line)
    return sections


def parse_table_rows(lines: list[str]) -> list[list[str]]:
    """Yield cell-lists for data rows of a Markdown table (skips header + divider)."""
    rows: list[list[str]] = []
    in_table = False
    for line in lines:
        s = line.strip()
        if s.startswith("|---"):
            in_table = True
            continue
        if not s.startswith("|"):
            in_table = False
            continue
        if not in_table:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if any(cells):
            rows.append(cells)
    return rows


def render_active(rows: list[list[str]]) -> str:
    out = [ACTIVE_HEADER, "", ACTIVE_TABLE_HEADER.rstrip()]
    for r in rows:
        # pad to 4 cells
        cells = (r + [""] * 4)[:4]
        out.append("| " + " | ".join(cells) + " |")
    out.append("")
    return "\n".join(out)


def render_completed(rows: list[list[str]]) -> str:
    out = [COMPLETED_HEADER, "", COMPLETED_TABLE_HEADER.rstrip()]
    for r in rows:
        cells = (r + [""] * 4)[:4]
        out.append("| " + " | ".join(cells) + " |")
    out.append("")
    return "\n".join(out)


def render_queue(items: list[str]) -> str:
    out = [QUEUE_HEADER, ""]
    for it in items:
        out.append(f"- [ ] {it}" if not it.startswith("- ") else it)
    out.append("")
    return "\n".join(out)


HEADER_RE = re.compile(r"^# My Contribution Journey", re.MULTILINE)


def rebuild(active: list[list[str]],
            completed: list[list[str]],
            queue: list[str]) -> str:
    head = (
        "# My Contribution Journey\n\n"
        "Track your learning and contributions here.\n\n"
        "---\n\n"
        "## Status legend\n\n"
        "- `exploring` — reading docs, setting up dev env\n"
        "- `learning` — running examples, reading code\n"
        "- `good-first-issue` — assigned a beginner issue\n"
        "- `pr-open` — pull request submitted\n"
        "- `merged` — first merged contribution 🎉\n\n"
        "---\n\n"
    )
    return (
        head
        + render_active(active) + "\n---\n\n"
        + render_completed(completed) + "\n---\n\n"
        + render_queue(queue)
    )


def find_row(rows: list[list[str]], name: str) -> int:
    for i, r in enumerate(rows):
        if r and r[0].strip() == name:
            return i
    return -1


# -------- commands --------

def cmd_list(args: argparse.Namespace) -> int:
    sections = split_sections(load())
    active = parse_table_rows(sections[ACTIVE_HEADER])
    completed = parse_table_rows(sections[COMPLETED_HEADER])
    print(f"Active ({len(active)}):")
    for r in active:
        print(f"  - {r[0]} [{r[1] if len(r) > 1 else ''}]")
    print(f"\nCompleted ({len(completed)}):")
    for r in completed:
        print(f"  - {r[0]} [{r[1] if len(r) > 1 else ''}]")
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    if args.status not in VALID_STATUS:
        print(f"Invalid status: {args.status}; valid: {sorted(VALID_STATUS)}", file=sys.stderr)
        return 2
    sections = split_sections(load())
    active = parse_table_rows(sections[ACTIVE_HEADER])
    if find_row(active, args.name) >= 0:
        print(f"'{args.name}' already in Active — use update", file=sys.stderr)
        return 1
    active.append([args.name, args.status, args.notes or "", args.link or ""])
    completed = parse_table_rows(sections[COMPLETED_HEADER])
    queue = [l.strip() for l in sections[QUEUE_HEADER] if l.strip().startswith("- ")]
    save(rebuild(active, completed, queue))
    print(f"Added '{args.name}' [{args.status}]")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    if args.status not in VALID_STATUS:
        print(f"Invalid status: {args.status}", file=sys.stderr)
        return 2
    sections = split_sections(load())
    active = parse_table_rows(sections[ACTIVE_HEADER])
    idx = find_row(active, args.name)
    if idx < 0:
        print(f"'{args.name}' not in Active", file=sys.stderr)
        return 1
    active[idx][1] = args.status
    if args.notes is not None:
        active[idx] = (active[idx] + [""] * 4)[:4]
        active[idx][2] = args.notes
    completed = parse_table_rows(sections[COMPLETED_HEADER])
    queue = [l.strip() for l in sections[QUEUE_HEADER] if l.strip().startswith("- ")]
    save(rebuild(active, completed, queue))
    print(f"Updated '{args.name}' → [{args.status}]")
    return 0


def cmd_complete(args: argparse.Namespace) -> int:
    sections = split_sections(load())
    active = parse_table_rows(sections[ACTIVE_HEADER])
    idx = find_row(active, args.name)
    if idx < 0:
        print(f"'{args.name}' not in Active", file=sys.stderr)
        return 1
    active.pop(idx)
    completed = parse_table_rows(sections[COMPLETED_HEADER])
    date = args.date or dt.date.today().isoformat()
    completed.append([args.name, args.pr, date, args.learned or ""])
    queue = [l.strip() for l in sections[QUEUE_HEADER] if l.strip().startswith("- ")]
    save(rebuild(active, completed, queue))
    print(f"Marked '{args.name}' completed on {date}")
    return 0


def cmd_remove(args: argparse.Namespace) -> int:
    sections = split_sections(load())
    active = parse_table_rows(sections[ACTIVE_HEADER])
    idx = find_row(active, args.name)
    if idx < 0:
        print(f"'{args.name}' not in Active", file=sys.stderr)
        return 1
    active.pop(idx)
    completed = parse_table_rows(sections[COMPLETED_HEADER])
    queue = [l.strip() for l in sections[QUEUE_HEADER] if l.strip().startswith("- ")]
    save(rebuild(active, completed, queue))
    print(f"Removed '{args.name}' from Active")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list").set_defaults(func=cmd_list)

    a = sub.add_parser("add")
    a.add_argument("name")
    a.add_argument("--status", required=True)
    a.add_argument("--notes")
    a.add_argument("--link")
    a.set_defaults(func=cmd_add)

    u = sub.add_parser("update")
    u.add_argument("name")
    u.add_argument("--status", required=True)
    u.add_argument("--notes")
    u.set_defaults(func=cmd_update)

    c = sub.add_parser("complete")
    c.add_argument("name")
    c.add_argument("--pr", required=True)
    c.add_argument("--learned")
    c.add_argument("--date")
    c.set_defaults(func=cmd_complete)

    r = sub.add_parser("remove")
    r.add_argument("name")
    r.set_defaults(func=cmd_remove)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
