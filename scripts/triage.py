#!/usr/bin/env python3
"""
triage.py — find open* GitHub projects not yet in ECOSYSTEM.md and rank them
for triage. Wraps scripts/discover.py and filters against the existing roster.

Usage:
    python3 scripts/triage.py --token <pat> [--min-stars 500] [--topic kubernetes]

Outputs Markdown ready to paste into a triage PR.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ECOSYSTEM_MD = REPO / "ECOSYSTEM.md"

sys.path.insert(0, str(REPO / "scripts"))
import discover  # noqa: E402


def existing_names() -> set[str]:
    text = ECOSYSTEM_MD.read_text()
    row = re.compile(r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
    names = {m.group(1).strip() for m in row.finditer(text)}
    return {n.lower() for n in names}


def name_already_known(name: str, known: set[str]) -> bool:
    n = name.lower()
    if n in known:
        return True
    # also match common variants: "open-foo" vs "openfoo" vs "Open Foo"
    n_compact = n.replace("-", "").replace(" ", "").replace("_", "")
    for k in known:
        k_compact = k.replace("-", "").replace(" ", "").replace("_", "")
        if n_compact == k_compact:
            return True
    return False


def render_markdown(candidates: list[discover.Project]) -> str:
    if not candidates:
        return "No new candidates above the threshold.\n"
    out = [
        "## Triage candidates",
        "",
        "Open* GitHub projects above star threshold that are NOT yet in ECOSYSTEM.md.",
        "Sorted by `discover.py` contributor-friendliness score.",
        "",
        "| Score | Stars | GFI | Lang | Project | License | URL |",
        "|------:|------:|----:|------|---------|---------|-----|",
    ]
    for p in candidates:
        gfi = p.good_first_issue_count if p.has_good_first_issues else "-"
        out.append(
            f"| {p.score} | {p.stars} | {gfi} | {p.language or '?'} | "
            f"{p.name} | {p.license or '?'} | {p.url} |"
        )
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--token", help="GitHub PAT (recommended for higher rate limits)")
    p.add_argument("--min-stars", type=int, default=500)
    p.add_argument("--topic", help="GitHub topic filter")
    p.add_argument("--top", type=int, default=20, help="Show top N candidates")
    args = p.parse_args(argv)

    found = discover.search_open_projects(
        token=args.token,
        min_stars=args.min_stars,
        topic=args.topic,
    )
    known = existing_names()
    new = [p for p in found if not name_already_known(p.name, known)]
    new.sort(key=lambda x: x.score, reverse=True)
    sys.stdout.write(render_markdown(new[: args.top]))
    print(
        f"\n_Searched: {len(found)} repos. Already in ECOSYSTEM: "
        f"{len(found) - len(new)}. New candidates: {len(new)}._\n",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
