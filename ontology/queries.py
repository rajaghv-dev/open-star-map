#!/usr/bin/env python3
"""
queries.py — pre-canned Cypher queries against the open_star_graph AGE graph.

Usage:
    python3 -m ontology.queries demo-chain
    python3 -m ontology.queries beginner-by-layer
    python3 -m ontology.queries complements-of OpenTelemetry
    python3 -m ontology.queries forks-and-supersessions
    python3 -m ontology.queries governed-by "Linux Foundation"

Without --dsn, prints the Cypher (no execution).
With    --dsn postgresql://..., executes via psycopg.
"""
from __future__ import annotations

import argparse
import sys
from typing import Callable


# ---------------------------------------------------------------------------
# Query templates — all parameterised by the graph name.
# ---------------------------------------------------------------------------


def q_demo_chain(graph: str) -> str:
    return (
        f"SELECT * FROM cypher('{graph}', $$\n"
        f"  MATCH (p:Project)-[:RUNS_ON]->(l:StackLayer)\n"
        f"  RETURN p.name, l.name, l.order\n"
        f"  ORDER BY l.order, p.name\n"
        f"$$) AS (project agtype, layer agtype, ord agtype);"
    )


def q_beginner_by_layer(graph: str) -> str:
    return (
        f"SELECT * FROM cypher('{graph}', $$\n"
        f"  MATCH (p:Project)-[:RUNS_ON]->(l:StackLayer)\n"
        f"  WHERE p.difficulty = 'beginner'\n"
        f"  RETURN p.name, l.name\n"
        f"  ORDER BY l.order\n"
        f"$$) AS (project agtype, layer agtype);"
    )


def q_complements_of(graph: str, name: str) -> str:
    safe = name.replace("'", "\\'")
    return (
        f"SELECT * FROM cypher('{graph}', $$\n"
        f"  MATCH (p:Project {{name: '{safe}'}})-[:COMPLEMENTS]-(q:Project)\n"
        f"  RETURN q.name\n"
        f"  ORDER BY q.name\n"
        f"$$) AS (peer agtype);"
    )


def q_forks_and_supersessions(graph: str) -> str:
    return (
        f"SELECT * FROM cypher('{graph}', $$\n"
        f"  MATCH (a:Project)-[:SUPERSEDES|MERGES_INTO]->(b:Project)\n"
        f"  RETURN a.name, b.name\n"
        f"  ORDER BY a.name\n"
        f"$$) AS (a agtype, b agtype);"
    )


def q_governed_by(graph: str, foundation: str) -> str:
    safe = foundation.replace("'", "\\'")
    return (
        f"SELECT * FROM cypher('{graph}', $$\n"
        f"  MATCH (p:Project)-[:GOVERNED_BY]->(f:Foundation {{name: '{safe}'}})\n"
        f"  RETURN p.name\n"
        f"  ORDER BY p.name\n"
        f"$$) AS (project agtype);"
    )


def q_teaches(graph: str, skill: str) -> str:
    safe = skill.replace("'", "\\'")
    return (
        f"SELECT * FROM cypher('{graph}', $$\n"
        f"  MATCH (p:Project)-[:TEACHES]->(s:Skill {{name: '{safe}'}})\n"
        f"  RETURN p.name\n"
        f"  ORDER BY p.name\n"
        f"$$) AS (project agtype);"
    )


QUERIES: dict[str, Callable[..., str]] = {
    "demo-chain": q_demo_chain,
    "beginner-by-layer": q_beginner_by_layer,
    "complements-of": q_complements_of,
    "forks-and-supersessions": q_forks_and_supersessions,
    "governed-by": q_governed_by,
    "teaches": q_teaches,
}


# ---------------------------------------------------------------------------
# Execution + CLI
# ---------------------------------------------------------------------------


def execute(cypher: str, dsn: str) -> list[tuple]:
    try:
        import psycopg
    except ImportError:
        print("psycopg not installed; install: pip install psycopg[binary]", file=sys.stderr)
        sys.exit(2)
    with psycopg.connect(dsn, autocommit=True) as conn:
        conn.execute("LOAD 'age';")
        conn.execute('SET search_path = ag_catalog, "$user", public;')
        return conn.execute(cypher).fetchall()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("query", choices=sorted(QUERIES), help="query name")
    p.add_argument("arg", nargs="?", help="argument for queries that need one")
    p.add_argument("--graph", default="open_star_graph")
    p.add_argument("--dsn", help="execute against this Postgres DSN")
    args = p.parse_args(argv)

    fn = QUERIES[args.query]
    needs_arg = args.query in {"complements-of", "governed-by", "teaches"}
    if needs_arg and not args.arg:
        p.error(f"query '{args.query}' requires an argument")
    cypher = fn(args.graph, args.arg) if needs_arg else fn(args.graph)

    if not args.dsn:
        sys.stdout.write(cypher + "\n")
        return 0

    rows = execute(cypher, args.dsn)
    for r in rows:
        print(" | ".join(str(c) for c in r))
    print(f"\n({len(rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
