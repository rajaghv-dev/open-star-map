"""Tests for scripts/triage.py — name-matching + Markdown rendering."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import triage  # noqa: E402
import discover  # noqa: E402


class TestNameMatching(unittest.TestCase):
    def test_exact_match(self) -> None:
        self.assertTrue(triage.name_already_known(
            "OpenTelemetry", {"opentelemetry"}
        ))

    def test_case_insensitive(self) -> None:
        self.assertTrue(triage.name_already_known(
            "openTELEMETRY", {"opentelemetry"}
        ))

    def test_dash_vs_no_dash(self) -> None:
        self.assertTrue(triage.name_already_known(
            "open-telemetry", {"opentelemetry"}
        ))

    def test_unknown(self) -> None:
        self.assertFalse(triage.name_already_known(
            "OpenBrandNew", {"opentelemetry"}
        ))


class TestRender(unittest.TestCase):
    def _make(self, name: str, score: float, stars: int) -> discover.Project:
        p = discover.Project(
            name=name, full_name=f"o/{name}", url=f"https://x/{name}",
            description="", language="Go", stars=stars, forks=10,
            license="Apache-2.0", open_issues=20,
        )
        p.score = score
        return p

    def test_empty(self) -> None:
        out = triage.render_markdown([])
        self.assertIn("No new candidates", out)

    def test_table_columns(self) -> None:
        cands = [self._make("OpenAlpha", 50.0, 2000), self._make("OpenBeta", 40.0, 800)]
        out = triage.render_markdown(cands)
        self.assertIn("OpenAlpha", out)
        self.assertIn("OpenBeta", out)
        self.assertIn("| Score | Stars |", out)

    def test_existing_names_loads_real_repo(self) -> None:
        """The real ECOSYSTEM.md should yield >300 known names."""
        names = triage.existing_names()
        self.assertGreater(len(names), 300)
        # spot-check
        self.assertIn("opentelemetry", names)


if __name__ == "__main__":
    unittest.main(verbosity=2)
