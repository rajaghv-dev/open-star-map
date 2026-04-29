"""Tests for ontology/queries.py — Cypher generation (no DB needed)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT.parent))
from ontology import queries  # noqa: E402


class TestQueryGeneration(unittest.TestCase):
    def test_demo_chain(self) -> None:
        c = queries.q_demo_chain("g")
        self.assertIn("MATCH (p:Project)-[:RUNS_ON]->(l:StackLayer)", c)
        self.assertIn("ORDER BY l.order", c)
        self.assertIn("'g'", c)

    def test_beginner_by_layer(self) -> None:
        c = queries.q_beginner_by_layer("g")
        self.assertIn("p.difficulty = 'beginner'", c)

    def test_complements_of_with_quote(self) -> None:
        c = queries.q_complements_of("g", "Foo's Project")
        self.assertIn("Foo\\'s Project", c)

    def test_forks_and_supersessions(self) -> None:
        c = queries.q_forks_and_supersessions("g")
        self.assertIn(":SUPERSEDES|MERGES_INTO", c)

    def test_governed_by(self) -> None:
        c = queries.q_governed_by("g", "Linux Foundation")
        self.assertIn(":GOVERNED_BY", c)
        self.assertIn("Linux Foundation", c)

    def test_teaches(self) -> None:
        c = queries.q_teaches("g", "rust")
        self.assertIn(":TEACHES", c)
        self.assertIn("rust", c)

    def test_all_queries_registered(self) -> None:
        self.assertGreaterEqual(len(queries.QUERIES), 6)
        for name in queries.QUERIES:
            self.assertIsInstance(name, str)


class TestCLI(unittest.TestCase):
    def test_main_no_dsn_prints_cypher(self) -> None:
        # Should not raise; without --dsn it prints to stdout.
        rc = queries.main(["demo-chain"])
        self.assertEqual(rc, 0)

    def test_arg_required_for_complements(self) -> None:
        with self.assertRaises(SystemExit):
            queries.main(["complements-of"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
