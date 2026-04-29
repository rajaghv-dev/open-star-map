#!/usr/bin/env python3
"""
run_prompt.py — execute a numbered prompt from prompts.md against the Anthropic API.

Usage:
    export ANTHROPIC_API_KEY=...
    python3 scripts/run_prompt.py PROMPT_01 \\
        --var project_name=Foo --var description="bar" --var stars=1234

    # Dry-run (just substitute and print, don't call API)
    python3 scripts/run_prompt.py PROMPT_01 --var project_name=Foo --dry-run

Prompts are looked up by header (## PROMPT_NN). Variables substitute {{name}} placeholders.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROMPTS_MD = REPO / "prompts.md"

DEFAULT_MODEL = "claude-haiku-4-5-20251001"
PROMPT_HEADER_RE = re.compile(r"^##\s+(PROMPT_\d+)\b.*?$", re.MULTILINE)
CODE_FENCE_RE = re.compile(r"```\s*\n(.*?)\n```", re.DOTALL)


def load_prompt(prompt_id: str) -> str:
    """Return the body inside the first ``` fence under '## PROMPT_NN'."""
    text = PROMPTS_MD.read_text()
    headers = list(PROMPT_HEADER_RE.finditer(text))
    if not headers:
        raise ValueError(f"No prompts found in {PROMPTS_MD}")
    span: tuple[int, int] | None = None
    for i, m in enumerate(headers):
        if m.group(1) == prompt_id:
            start = m.end()
            end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
            span = (start, end)
            break
    if span is None:
        valid = ", ".join(m.group(1) for m in headers)
        raise ValueError(f"Prompt '{prompt_id}' not found. Valid: {valid}")
    chunk = text[span[0]:span[1]]
    fence = CODE_FENCE_RE.search(chunk)
    if not fence:
        raise ValueError(f"Prompt '{prompt_id}' has no fenced code block")
    return fence.group(1).strip()


def substitute(template: str, vars: dict[str, str]) -> str:
    out = template
    for k, v in vars.items():
        out = out.replace("{{" + k + "}}", v)
    leftover = re.findall(r"\{\{(\w+)\}\}", out)
    if leftover:
        print(f"Warning: unsubstituted variables: {sorted(set(leftover))}",
              file=sys.stderr)
    return out


def parse_var_args(items: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"--var must be name=value, got '{item}'")
        k, v = item.split("=", 1)
        out[k.strip()] = v
    return out


def call_anthropic(prompt: str, model: str) -> str:
    try:
        import anthropic
    except ImportError:
        print("Install anthropic SDK: pip install anthropic", file=sys.stderr)
        sys.exit(2)
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(2)
    client = anthropic.Anthropic(api_key=api_key)
    # Prompt caching on the system prompt would go here if we had a long static
    # preamble; the prompts in prompts.md are short, so we send them inline.
    msg = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in msg.content if hasattr(b, "text"))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("prompt_id", help="e.g. PROMPT_01")
    p.add_argument("--var", action="append", default=[], help="name=value")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    template = load_prompt(args.prompt_id)
    vars = parse_var_args(args.var)
    final = substitute(template, vars)

    if args.dry_run:
        sys.stdout.write(final + "\n")
        return 0

    response = call_anthropic(final, args.model)
    sys.stdout.write(response + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
