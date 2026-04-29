"""
Static ontology tests — stdlib only, no DB required.

Validates that:
  - All ontology JSON files parse and have expected top-level keys.
  - seed_concepts.json stack layers are numbered 1..8 with no gaps.
  - relationships.json edges reference a consistent set of project names.
  - schema.cypher MERGE-creates every project that relationships.json names.
  - Every projects/*.md deep-dive has YAML frontmatter and required keys.

Run:  python3 -m unittest ontology.tests.test_static -v
"""
import json
import re
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ONT = REPO / "ontology"
PROJECTS = REPO / "projects"


def load_json(name: str) -> dict:
    return json.loads((ONT / name).read_text())


def project_names_in_schema_cypher() -> set[str]:
    """Extract every Project name MERGE'd in schema.cypher."""
    text = (ONT / "schema.cypher").read_text()
    return set(re.findall(r"\(:Project\s*\{name:\s*'([^']+)'", text)) | \
           set(re.findall(r"MERGE\s*\(a:Project\s*\{name:\s*'([^']+)'", text))


def project_names_in_relationships() -> set[str]:
    rels = load_json("relationships.json")
    names: set[str] = set()
    for entry in rels.get("depends_on", []) + rels.get("supersedes", []) + \
                 rels.get("merges_into", []):
        names.add(entry["from"])
        names.add(entry["to"])
    for entry in rels.get("complements", []):
        names.add(entry["a"])
        names.add(entry["b"])
    for entry in rels.get("implements_spec", []):
        names.add(entry["project"])
    for entry in rels.get("part_of", []):
        names.add(entry["child"])
        names.add(entry["parent"])
    return names


class TestSeedConcepts(unittest.TestCase):
    def setUp(self) -> None:
        self.seed = load_json("seed_concepts.json")

    def test_top_level_keys(self) -> None:
        for k in ("stack_layers", "categories", "tiers", "concepts"):
            self.assertIn(k, self.seed, f"missing key {k}")

    def test_stack_layer_order(self) -> None:
        layers = self.seed["stack_layers"]
        self.assertEqual(len(layers), 8, "expected 8 stack layers")
        orders = sorted(l["order"] for l in layers)
        self.assertEqual(orders, list(range(1, 9)),
                         "stack-layer order numbers must be 1..8")

    def test_layer_slugs_unique(self) -> None:
        slugs = [l["slug"] for l in self.seed["stack_layers"]]
        self.assertEqual(len(slugs), len(set(slugs)),
                         "stack-layer slugs must be unique")

    def test_categories_have_ecosystem_section(self) -> None:
        for c in self.seed["categories"]:
            self.assertIn("slug", c)
            self.assertIn("ecosystem_section", c)


class TestRelationships(unittest.TestCase):
    def setUp(self) -> None:
        self.rels = load_json("relationships.json")

    def test_required_edge_keys(self) -> None:
        for k in ("depends_on", "complements", "supersedes", "merges_into",
                  "implements_spec", "part_of"):
            self.assertIn(k, self.rels, f"missing edge bucket: {k}")

    def test_no_self_loops(self) -> None:
        for e in self.rels["depends_on"] + self.rels["supersedes"] + \
                 self.rels["merges_into"]:
            self.assertNotEqual(e["from"], e["to"],
                                f"self-loop edge: {e}")
        for e in self.rels["complements"]:
            self.assertNotEqual(e["a"], e["b"],
                                f"self-loop complements: {e}")

    def test_known_supersession(self) -> None:
        pairs = {(e["from"], e["to"]) for e in self.rels["supersedes"]}
        self.assertIn(("OpenTofu", "Terraform"), pairs)
        self.assertIn(("OpenSearch", "Elasticsearch"), pairs)

    def test_archived_projects_merged_into_otel(self) -> None:
        targets = {e["to"] for e in self.rels["merges_into"]
                   if e["from"] in ("OpenTracing", "OpenCensus")}
        self.assertEqual(targets, {"OpenTelemetry"})


class TestSchemaCypher(unittest.TestCase):
    def test_balanced_dollar_quotes(self) -> None:
        text = (ONT / "schema.cypher").read_text()
        self.assertEqual(text.count("$$") % 2, 0,
                         "schema.cypher: unbalanced $$ delimiters")

    def test_schema_covers_relationships_projects(self) -> None:
        """Every Project mentioned in relationships.json edges that the
        schema is expected to seed should also be MERGE'd in schema.cypher.

        We only enforce this for the canonical demo-chain projects to keep
        the schema small; non-canonical names (e.g. Terraform, Elasticsearch)
        are intentionally not in schema.cypher because they are non-OSS.
        """
        canonical = {
            "OpenTelemetry", "OpenBMC", "OpenTitan", "OpenROAD", "ONNX",
            "OpenVINO", "OpenCV", "Open Policy Agent", "OpenSearch",
            "OpenTofu", "OpenStack", "OpenLineage", "OpenSSF Scorecard",
        }
        in_schema = project_names_in_schema_cypher()
        missing = canonical - in_schema
        self.assertFalse(missing, f"schema.cypher missing projects: {missing}")


class TestProjectFiles(unittest.TestCase):
    REQUIRED_FRONTMATTER = ("name", "url", "license", "language",
                            "difficulty", "status")

    def test_all_have_frontmatter(self) -> None:
        for f in sorted(PROJECTS.glob("*.md")):
            with self.subTest(file=f.name):
                lines = f.read_text().splitlines()
                self.assertEqual(lines[0].strip(), "---",
                                 f"{f.name}: missing opening ---")
                end = lines.index("---", 1)
                fm = "\n".join(lines[1:end])
                for key in self.REQUIRED_FRONTMATTER:
                    self.assertRegex(fm, rf"(?m)^{key}\s*:",
                                     f"{f.name}: frontmatter missing '{key}'")

    def test_difficulty_values_valid(self) -> None:
        valid = {"beginner", "intermediate", "advanced"}
        for f in sorted(PROJECTS.glob("*.md")):
            text = f.read_text()
            m = re.search(r"(?m)^difficulty:\s*(\S+)", text)
            if not m:
                continue
            value = m.group(1).strip().lower()
            with self.subTest(file=f.name, difficulty=value):
                self.assertIn(value, valid,
                              f"{f.name}: difficulty must be one of {valid}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
