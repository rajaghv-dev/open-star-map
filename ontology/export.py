#!/usr/bin/env python3
"""
export.py — Export the open_star_graph AGE graph to OWL for Protégé inspection.

This is the INSPECTION-ONLY layer. The graph (Apache AGE) is the source of truth.
Never edit the .owl file directly — regenerate it from the graph.

Usage:
    python3 ontology/export.py --dsn "postgresql://user:pass@localhost/dbname" \
                                --output ontology/open_star.owl

Requires: psycopg (psycopg3), owlready2, rdflib
    pip install psycopg owlready2 rdflib
"""

import argparse
import sys
from pathlib import Path

try:
    import psycopg
    from owlready2 import get_ontology, Thing, ObjectProperty, DataProperty, AllDisjoint
    from rdflib import Graph as RDFGraph
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("pip install psycopg owlready2 rdflib")
    sys.exit(1)


IRI_BASE = "https://rajaghv-dev.github.io/open-star/ontology#"


def fetch_nodes(conn, graph: str, label: str) -> list[dict]:
    q = f"""
        SELECT * FROM cypher('{graph}', $$
          MATCH (n:{label}) RETURN n
        $$) AS (n agtype);
    """
    rows = conn.execute(q).fetchall()
    import json
    return [json.loads(r[0]) for r in rows]


def fetch_edges(conn, graph: str, edge_type: str) -> list[dict]:
    q = f"""
        SELECT * FROM cypher('{graph}', $$
          MATCH (a)-[r:{edge_type}]->(b) RETURN a.name, type(r), b.name, r
        $$) AS (a agtype, rel agtype, b agtype, props agtype);
    """
    rows = conn.execute(q).fetchall()
    import json
    return [
        {"from": json.loads(r[0]), "type": json.loads(r[1]), "to": json.loads(r[2])}
        for r in rows
    ]


def build_owl(projects: list, edges: list, output_path: str) -> None:
    onto = get_ontology(IRI_BASE)

    with onto:
        class OpenProject(Thing): pass
        class StackLayer(Thing): pass
        class TechnicalSkill(Thing): pass
        class OpenFoundation(Thing): pass
        class OntologyConcept(Thing): pass
        class Tier(Thing): pass

        class runsOn(OpenProject >> StackLayer, ObjectProperty): pass
        class governedBy(OpenProject >> OpenFoundation, ObjectProperty): pass
        class dependsOn(OpenProject >> OpenProject, ObjectProperty): pass
        class complements(OpenProject >> OpenProject, ObjectProperty, ): pass
        class supersedes(OpenProject >> OpenProject, ObjectProperty): pass
        class mergesInto(OpenProject >> OpenProject, ObjectProperty): pass
        class implementsSpec(OpenProject >> OntologyConcept, ObjectProperty): pass
        class teaches(OpenProject >> TechnicalSkill, ObjectProperty): pass
        class inTier(OpenProject >> Tier, ObjectProperty): pass

        class hasName(DataProperty): range = [str]
        class hasUrl(DataProperty): range = [str]
        class hasLicense(DataProperty): range = [str]
        class hasDifficulty(DataProperty): range = [str]
        class isOSS(DataProperty): range = [bool]

    owl_instances: dict[str, OpenProject] = {}
    for p in projects:
        name = p.get("name", "")
        if not name:
            continue
        safe = name.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        inst = OpenProject(safe, namespace=onto)
        inst.hasName = [name]
        if p.get("url"):
            inst.hasUrl = [p["url"]]
        if p.get("license"):
            inst.hasLicense = [p["license"]]
        if p.get("difficulty"):
            inst.hasDifficulty = [p["difficulty"]]
        inst.isOSS = [bool(p.get("is_oss", True))]
        owl_instances[name] = inst

    for e in edges:
        a = owl_instances.get(e["from"])
        b = owl_instances.get(e["to"])
        if not a or not b:
            continue
        etype = e["type"]
        if etype == "DEPENDS_ON":
            a.dependsOn.append(b)
        elif etype == "COMPLEMENTS":
            a.complements.append(b)
        elif etype == "SUPERSEDES":
            a.supersedes.append(b)
        elif etype == "MERGES_INTO":
            a.mergesInto.append(b)

    onto.save(file=output_path, format="rdfxml")
    print(f"Saved OWL ontology → {output_path}")
    print(f"  Classes: 6, Instances: {len(owl_instances)}, Object properties: 8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export open_star_graph to OWL")
    parser.add_argument("--dsn",    required=True, help="PostgreSQL DSN")
    parser.add_argument("--graph",  default="open_star_graph", help="AGE graph name")
    parser.add_argument("--output", default="ontology/open_star.owl", help="Output .owl path")
    args = parser.parse_args()

    with psycopg.connect(args.dsn, autocommit=True) as conn:
        conn.execute("LOAD 'age';")
        conn.execute("SET search_path = ag_catalog, \"$user\", public;")

        projects = fetch_nodes(conn, args.graph, "Project")
        edges = []
        for edge_type in ("DEPENDS_ON", "COMPLEMENTS", "SUPERSEDES", "MERGES_INTO"):
            edges.extend(fetch_edges(conn, args.graph, edge_type))

    build_owl(projects, edges, args.output)


if __name__ == "__main__":
    main()
