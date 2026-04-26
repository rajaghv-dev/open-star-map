---
name: OpenTofu
url: https://github.com/opentofu/opentofu
license: MPL-2.0
language: Go
difficulty: intermediate
status: active
---

## What it does

Community-driven open-source fork of Terraform, governed by the Linux Foundation. Fully compatible with Terraform configurations. Actively diverging with new features. Fast-growing contributor base.

## Why contribute

- One of the most-watched new Go projects — very active PR review
- IaC is a core devops skill; contributing means you understand it deeply
- Large, well-organized codebase with clear module boundaries
- Welcoming to new contributors — explicit "good first issue" program

## Dev environment setup

```bash
git clone https://github.com/opentofu/opentofu
cd opentofu
go build ./...

# Run the CLI
go run ./cmd/tofu version

# Run tests
go test ./internal/...
```

## Where to find good first issues

- https://github.com/opentofu/opentofu/labels/good%20first%20issue
- https://github.com/opentofu/opentofu/labels/help%20wanted
- RFC discussions: https://github.com/opentofu/opentofu/discussions

## Community

- Slack: https://opentofu.org/slack
- Weekly community calls: listed in repo
- Governance: https://github.com/opentofu/opentofu/blob/main/GOVERNANCE.md

## Learning resources

- Docs: https://opentofu.org/docs/
- How the Terraform/OpenTofu graph engine works: read `internal/dag/`
- Start by reading `internal/command/` — each CLI subcommand is a file
