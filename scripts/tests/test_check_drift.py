"""Tests for scripts/check_drift.py — runs the real drift check on the repo."""
from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))


class TestDrift(unittest.TestCase):
    def test_repo_has_no_drift(self) -> None:
        import check_drift  # noqa: WPS433
        importlib.reload(check_drift)
        rc = check_drift.main()
        self.assertEqual(rc, 0, "scripts/check_drift.py reported drift on the repo")

    def test_synthetic_drift_detected(self) -> None:
        """Pollute the loaders to confirm drift is actually detected."""
        import check_drift  # noqa: WPS433
        importlib.reload(check_drift)

        original_eco = check_drift.load_ecosystem_names
        original_rel = check_drift.load_relationships_names
        try:
            check_drift.load_ecosystem_names = lambda: {"OpenTelemetry"}
            check_drift.load_relationships_names = lambda: {
                "OpenTelemetry", "GhostProject"
            }
            rc = check_drift.main()
            self.assertEqual(rc, 1)
        finally:
            check_drift.load_ecosystem_names = original_eco
            check_drift.load_relationships_names = original_rel


if __name__ == "__main__":
    unittest.main(verbosity=2)
