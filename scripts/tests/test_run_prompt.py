"""Tests for scripts/run_prompt.py — substitution + lookup (no API calls)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import run_prompt  # noqa: E402


class TestPromptLoad(unittest.TestCase):
    def test_load_prompt_01_exists(self) -> None:
        body = run_prompt.load_prompt("PROMPT_01")
        self.assertIn("{{project_name}}", body)
        self.assertIn("stack_layer", body)

    def test_unknown_prompt_raises(self) -> None:
        with self.assertRaises(ValueError):
            run_prompt.load_prompt("PROMPT_99_DOES_NOT_EXIST")


class TestSubstitute(unittest.TestCase):
    def test_basic_substitution(self) -> None:
        out = run_prompt.substitute("hello {{name}}!", {"name": "world"})
        self.assertEqual(out, "hello world!")

    def test_unsubstituted_warns(self) -> None:
        out = run_prompt.substitute("a={{x}} b={{y}}", {"x": "1"})
        self.assertEqual(out, "a=1 b={{y}}")  # leftover preserved

    def test_parse_var_args(self) -> None:
        d = run_prompt.parse_var_args(["a=1", "b=hello world", "c=x=y"])
        self.assertEqual(d, {"a": "1", "b": "hello world", "c": "x=y"})

    def test_parse_var_invalid(self) -> None:
        with self.assertRaises(ValueError):
            run_prompt.parse_var_args(["no_equals_sign"])


class TestDryRun(unittest.TestCase):
    def test_main_dry_run(self) -> None:
        rc = run_prompt.main([
            "PROMPT_01",
            "--var", "project_name=Foo",
            "--var", "description=Bar",
            "--var", "language=Go",
            "--var", "license=Apache-2.0",
            "--var", "stars=100",
            "--var", "gfi_count=5",
            "--var", "topics=cloud",
            "--dry-run",
        ])
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
