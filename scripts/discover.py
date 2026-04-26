#!/usr/bin/env python3
"""
discover.py — search GitHub for open* projects and score them for contributor-friendliness.

Usage:
    python3 scripts/discover.py [--topic <topic>] [--min-stars <n>] [--token <github-token>]

Requires: requests
    pip install requests
"""

import argparse
import json
import sys
import time
from dataclasses import dataclass, field
from typing import Optional
import urllib.request
import urllib.parse


@dataclass
class Project:
    name: str
    full_name: str
    url: str
    description: str
    language: str
    stars: int
    forks: int
    license: str
    open_issues: int
    has_good_first_issues: bool = False
    good_first_issue_count: int = 0
    score: float = field(default=0.0, init=False)

    def compute_score(self) -> float:
        """Higher = more contributor-friendly."""
        s = 0.0
        # Stars: proxy for impact (log scale)
        if self.stars > 0:
            import math
            s += min(30, math.log10(self.stars) * 10)
        # Good first issues: direct signal
        s += min(30, self.good_first_issue_count * 3)
        # Activity: open issues (not too few, not overwhelming)
        if 10 <= self.open_issues <= 500:
            s += 20
        elif self.open_issues > 0:
            s += 10
        # Has a license
        if self.license and self.license != "NOASSERTION":
            s += 10
        # Forks: proxy for contributor activity
        if self.forks > 50:
            s += 10
        self.score = round(s, 1)
        return self.score


def gh_get(path: str, token: Optional[str] = None) -> dict:
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def search_open_projects(
    token: Optional[str],
    min_stars: int = 500,
    topic: Optional[str] = None,
) -> list[Project]:
    query = f"open in:name stars:>={min_stars} is:public"
    if topic:
        query += f" topic:{topic}"
    encoded = urllib.parse.quote(query)
    path = f"/search/repositories?q={encoded}&sort=stars&per_page=50"

    print(f"Searching GitHub: {query}", file=sys.stderr)
    data = gh_get(path, token)
    items = data.get("items", [])

    projects = []
    for item in items:
        name = item.get("name", "")
        if not name.lower().startswith("open"):
            continue

        license_name = ""
        lic = item.get("license")
        if lic:
            license_name = lic.get("spdx_id") or lic.get("name") or ""

        p = Project(
            name=name,
            full_name=item["full_name"],
            url=item["html_url"],
            description=(item.get("description") or "").strip(),
            language=item.get("language") or "",
            stars=item.get("stargazers_count", 0),
            forks=item.get("forks_count", 0),
            license=license_name,
            open_issues=item.get("open_issues_count", 0),
        )

        # Check good-first-issue label count (costs one API call per repo)
        try:
            label_path = f"/repos/{p.full_name}/labels/good%20first%20issue"
            gh_get(label_path, token)
            # If it didn't 404, the label exists — fetch issue count
            issues_path = (
                f"/search/issues?q=repo:{p.full_name}+label:%22good+first+issue%22"
                f"+is:open+is:issue&per_page=1"
            )
            issue_data = gh_get(issues_path, token)
            count = issue_data.get("total_count", 0)
            p.has_good_first_issues = count > 0
            p.good_first_issue_count = count
            time.sleep(0.3)  # respect rate limit
        except Exception:
            pass

        p.compute_score()
        projects.append(p)

    return sorted(projects, key=lambda x: x.score, reverse=True)


def print_table(projects: list[Project]) -> None:
    print(f"\n{'Rank':<5} {'Score':<7} {'Stars':<8} {'GFI':<5} {'Lang':<12} {'Name':<40} URL")
    print("-" * 110)
    for i, p in enumerate(projects, 1):
        lang = (p.language or "?")[:11]
        name = p.name[:39]
        gfi = p.good_first_issue_count if p.has_good_first_issues else "-"
        print(f"{i:<5} {p.score:<7} {p.stars:<8} {gfi!s:<5} {lang:<12} {name:<40} {p.url}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover open* OSS projects on GitHub")
    parser.add_argument("--token", help="GitHub personal access token (increases rate limit)")
    parser.add_argument("--min-stars", type=int, default=500, help="Minimum star count (default: 500)")
    parser.add_argument("--topic", help="Filter by GitHub topic (e.g. kubernetes, networking)")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of table")
    args = parser.parse_args()

    projects = search_open_projects(
        token=args.token,
        min_stars=args.min_stars,
        topic=args.topic,
    )

    if not projects:
        print("No projects found. Try lowering --min-stars.", file=sys.stderr)
        sys.exit(1)

    if args.json:
        out = [
            {
                "name": p.name,
                "full_name": p.full_name,
                "url": p.url,
                "description": p.description,
                "language": p.language,
                "stars": p.stars,
                "license": p.license,
                "good_first_issues": p.good_first_issue_count,
                "score": p.score,
            }
            for p in projects
        ]
        print(json.dumps(out, indent=2))
    else:
        print_table(projects)
        print(f"Found {len(projects)} open* projects. Scored by contributor-friendliness.")
        print("Tip: re-run with --token <pat> for higher GitHub API rate limits.")


if __name__ == "__main__":
    main()
