"""Tests for scripts/journey.py — round-trips on a temp MY_JOURNEY.md."""
from __future__ import annotations

import importlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))


class TestJourney(unittest.TestCase):
    def setUp(self) -> None:
        # Use a temp file for the journey to avoid touching the real one.
        self.tmpdir = Path(tempfile.mkdtemp())
        self.tmp_journey = self.tmpdir / "MY_JOURNEY.md"
        shutil.copy(ROOT / "MY_JOURNEY.md", self.tmp_journey)

        import journey  # noqa: WPS433
        importlib.reload(journey)
        self.j = journey
        self.j.JOURNEY = self.tmp_journey  # redirect

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_add_then_list(self) -> None:
        rc = self.j.main(["add", "OpenTelemetry", "--status", "exploring",
                          "--notes", "starting"])
        self.assertEqual(rc, 0)
        text = self.tmp_journey.read_text()
        self.assertIn("OpenTelemetry", text)
        self.assertIn("exploring", text)

    def test_add_invalid_status_rejected(self) -> None:
        rc = self.j.main(["add", "Foo", "--status", "bogus"])
        self.assertEqual(rc, 2)

    def test_add_then_update(self) -> None:
        self.j.main(["add", "OpenTelemetry", "--status", "exploring"])
        rc = self.j.main(["update", "OpenTelemetry", "--status", "learning"])
        self.assertEqual(rc, 0)
        text = self.tmp_journey.read_text()
        self.assertIn("learning", text)
        # exploring should no longer be there for that row
        active_block = text.split("## Completed")[0]
        self.assertNotIn("exploring", active_block.split("OpenTelemetry")[1].split("|")[2])

    def test_complete_moves_to_completed_table(self) -> None:
        self.j.main(["add", "OpenTelemetry", "--status", "pr-open"])
        rc = self.j.main([
            "complete", "OpenTelemetry",
            "--pr", "https://github.com/x/y/pull/1",
            "--learned", "OTLP basics",
            "--date", "2026-04-29",
        ])
        self.assertEqual(rc, 0)
        text = self.tmp_journey.read_text()
        active_part, completed_part = text.split("## Completed contributions", 1)
        self.assertNotIn("OpenTelemetry", active_part.split("## Active projects")[1])
        self.assertIn("OpenTelemetry", completed_part)
        self.assertIn("2026-04-29", completed_part)

    def test_remove(self) -> None:
        self.j.main(["add", "OpenFeature", "--status", "exploring"])
        rc = self.j.main(["remove", "OpenFeature"])
        self.assertEqual(rc, 0)
        self.assertNotIn("OpenFeature", self.tmp_journey.read_text())

    def test_idempotent_add_rejected(self) -> None:
        self.j.main(["add", "Foo", "--status", "exploring"])
        rc = self.j.main(["add", "Foo", "--status", "exploring"])
        self.assertEqual(rc, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
