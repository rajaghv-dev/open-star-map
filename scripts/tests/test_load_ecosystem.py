"""Tests for scripts/load_ecosystem.py — pure-Python parsing + Cypher generation."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import load_ecosystem as le  # noqa: E402

SAMPLE = """\
# Sample

## A. Languages, runtimes, compilers

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 1 | Linux kernel | OS foundation | GPL-2.0 | [kernel.org](https://kernel.org) |
| 2 | Python | Language | PSF-2.0 | [python.org](https://python.org) |

## B. AI/ML deep learning

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 51 | PyTorch | Deep learning | BSD | [pytorch.org](https://pytorch.org) |

## L. Additions (2026-04-29)

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 431 | OpenFPGA | FPGA fabric | MIT | [github.com/lnis-uofu/OpenFPGA](https://github.com/lnis-uofu/OpenFPGA) |
"""


class TestParse(unittest.TestCase):
    def test_parses_three_projects(self) -> None:
        projects = le.parse_ecosystem(SAMPLE)
        self.assertEqual(len(projects), 4)

    def test_section_letters_assigned(self) -> None:
        projects = le.parse_ecosystem(SAMPLE)
        sections = [p.section for p in projects]
        self.assertEqual(sections, ["A", "A", "B", "L"])

    def test_url_extraction(self) -> None:
        projects = le.parse_ecosystem(SAMPLE)
        urls = [p.url for p in projects]
        self.assertIn("https://kernel.org", urls)
        self.assertIn("https://github.com/lnis-uofu/OpenFPGA", urls)

    def test_category_mapping(self) -> None:
        projects = le.parse_ecosystem(SAMPLE)
        cats = {p.name: p.category for p in projects}
        self.assertEqual(cats["Linux kernel"], "languages")
        self.assertEqual(cats["PyTorch"], "ai-ml")
        self.assertEqual(cats["OpenFPGA"], "additions")


class TestCypher(unittest.TestCase):
    def setUp(self) -> None:
        self.projects = le.parse_ecosystem(SAMPLE)
        self.rels = {
            "depends_on": [{"from": "OpenFPGA", "to": "PyTorch", "note": "fake edge"}],
            "complements": [],
            "supersedes": [],
            "merges_into": [],
            "part_of": [],
            "implements_spec": [],
        }

    def test_cypher_uses_merge(self) -> None:
        out = le.generate_cypher(self.projects, self.rels, graph="g_test")
        self.assertIn("MERGE (p:Project {name: 'Linux kernel'})", out)
        self.assertIn("MERGE (p)-[:BELONGS_TO]->(c)", out)
        self.assertIn("[:RUNS_ON]->(l)", out)

    def test_cypher_escapes_quotes(self) -> None:
        proj = le.Project(
            number=999, name="O'Foo", role="r", license="MIT",
            url="http://x", section="A",
        )
        s = le.cypher_for_project(proj, "g")
        self.assertIn("O\\'Foo", s)

    def test_edge_includes_note(self) -> None:
        out = le.generate_cypher(self.projects, self.rels, graph="g_test")
        self.assertIn("DEPENDS_ON {note: 'fake edge'}", out)

    def test_proprietary_marked_not_oss(self) -> None:
        proj = le.Project(
            number=1000, name="OpenAI", role="LLM",
            license="Proprietary", url="https://openai.com", section="B",
        )
        s = le.cypher_for_project(proj, "g")
        self.assertIn("p.is_oss = false", s)


class TestRealEcosystem(unittest.TestCase):
    """Sanity: the actual ECOSYSTEM.md parses cleanly."""

    def test_real_file_parses(self) -> None:
        text = (ROOT / "ECOSYSTEM.md").read_text()
        projects = le.parse_ecosystem(text)
        self.assertGreater(len(projects), 400, "expected >400 projects")
        # at least one in every section A–L
        sections = {p.section for p in projects}
        for letter in "ABCDEFGHIJKL":
            self.assertIn(letter, sections, f"section {letter} produced no rows")

    def test_real_relationships_generates(self) -> None:
        import json
        text = (ROOT / "ECOSYSTEM.md").read_text()
        projects = le.parse_ecosystem(text)
        rels = json.loads((ROOT / "ontology" / "relationships.json").read_text())
        out = le.generate_cypher(projects, rels)
        self.assertIn("LOAD 'age';", out)
        self.assertIn("MERGE (p:Project", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
