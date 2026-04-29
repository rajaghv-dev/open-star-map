#!/usr/bin/env python3
"""
check_drift.py — detect inconsistencies between ECOSYSTEM.md, relationships.json,
projects/*.md, and seed_concepts.json. Exits 0 if clean, 1 on drift.

Run:
    python3 scripts/check_drift.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ECOSYSTEM_MD = REPO / "ECOSYSTEM.md"
RELATIONSHIPS_JSON = REPO / "ontology" / "relationships.json"
SEED_CONCEPTS_JSON = REPO / "ontology" / "seed_concepts.json"
PROJECTS_DIR = REPO / "projects"
SCHEMA_CYPHER = REPO / "ontology" / "schema.cypher"

# Names that legitimately appear in relationships.json but are NOT in ECOSYSTEM
# (legacy/superseded projects, foundations, sub-projects, specs).
ALLOWED_OUT_OF_ECOSYSTEM: set[str] = {
    # superseded non-OSS targets
    "Terraform", "Elasticsearch", "HashiCorp Vault", "OpenDevin",
    # foundations / orgs (not code projects)
    "OpenSSF",
    # OpenStack sub-projects (PART_OF children)
    "OpenStack Nova", "OpenStack Neutron", "OpenStack Cinder",
    "OpenStack Swift", "OpenStack Ironic", "OpenStack Keystone",
    "OpenStack Heat", "OpenStack Magnum",
    # Other sub-projects
    "OpenSSF Scorecard", "OpenSSF SLSA", "OpenSearch Dashboards",
    "OpenLane",
    # archived (in spec map only)
    "OpenTracing", "OpenCensus",
    # spec-only entries (project column happens to be a spec name)
    "Open Container Initiative runc", "OpenMetrics", "OpenID Connect",
}


def load_ecosystem_names() -> set[str]:
    text = ECOSYSTEM_MD.read_text()
    # Accept "| 1 |" and "| 200a |" / "| 296b |" sub-numbered rows.
    row = re.compile(r"^\|\s*\d+[a-z]?\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
    return {m.group(1).strip() for m in row.finditer(text)}


def load_relationships_names() -> set[str]:
    rels = json.loads(RELATIONSHIPS_JSON.read_text())
    names: set[str] = set()
    for k in ("depends_on", "supersedes", "merges_into"):
        for e in rels.get(k, []):
            names.add(e["from"])
            names.add(e["to"])
    for e in rels.get("complements", []):
        names.add(e["a"])
        names.add(e["b"])
    for e in rels.get("part_of", []):
        names.add(e["child"])
        names.add(e["parent"])
    for e in rels.get("implements_spec", []):
        names.add(e["project"])
    return names


def load_project_md_names() -> set[str]:
    names: set[str] = set()
    for f in PROJECTS_DIR.glob("*.md"):
        text = f.read_text()
        m = re.search(r"(?m)^name:\s*(.+?)\s*$", text)
        if m:
            names.add(m.group(1).strip())
    return names


def load_seed_slugs() -> set[str]:
    seed = json.loads(SEED_CONCEPTS_JSON.read_text())
    slugs: set[str] = set()
    for layer in seed.get("stack_layers", []):
        slugs.add(layer["slug"])
    for cat in seed.get("categories", []):
        slugs.add(cat["slug"])
    return slugs


def main() -> int:
    eco = load_ecosystem_names()
    rels = load_relationships_names()
    proj_md = load_project_md_names()
    slugs = load_seed_slugs()
    schema = SCHEMA_CYPHER.read_text()

    errors: list[str] = []

    # 1. Every name in relationships.json must be in ECOSYSTEM or allowlisted
    missing = (rels - eco) - ALLOWED_OUT_OF_ECOSYSTEM
    for name in sorted(missing):
        errors.append(
            f"relationships.json references '{name}' but it is not in ECOSYSTEM.md "
            f"(add the row, or extend ALLOWED_OUT_OF_ECOSYSTEM in scripts/check_drift.py)"
        )

    # 2. Every projects/*.md must have a matching ECOSYSTEM row
    for name in sorted(proj_md - eco):
        errors.append(
            f"projects/ deep-dive '{name}' has no matching row in ECOSYSTEM.md"
        )

    # 3. seed_concepts slugs must be referenced in schema.cypher OR bootstrap.cypher
    bootstrap = (REPO / "ontology" / "bootstrap.cypher").read_text()
    cypher_text = schema + "\n" + bootstrap
    layer_slugs = {layer["slug"] for layer
                   in json.loads(SEED_CONCEPTS_JSON.read_text()).get("stack_layers", [])}
    for slug in sorted(layer_slugs):
        if f"slug: '{slug}'" not in cypher_text and f'slug: "{slug}"' not in cypher_text:
            errors.append(
                f"seed_concepts stack layer slug '{slug}' is not referenced "
                f"in schema.cypher or bootstrap.cypher"
            )

    # 4. ECOSYSTEM rows that are duplicated (same name, two rows)
    text = ECOSYSTEM_MD.read_text()
    dup_counter: dict[str, int] = {}
    row_re = re.compile(r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
    for m in row_re.finditer(text):
        n = m.group(1).strip()
        dup_counter[n] = dup_counter.get(n, 0) + 1
    for name, count in sorted(dup_counter.items()):
        if count > 1:
            errors.append(f"ECOSYSTEM.md has '{name}' duplicated ({count} rows)")

    if errors:
        print(f"DRIFT DETECTED ({len(errors)} issues):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(
        f"OK — ECOSYSTEM rows: {len(eco)}, relationships names: {len(rels)}, "
        f"projects/*.md: {len(proj_md)}, seed slugs: {len(slugs)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
