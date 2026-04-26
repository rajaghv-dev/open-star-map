---
name: OpenSSF Scorecard
url: https://github.com/ossf/scorecard
license: Apache-2.0
language: Go
difficulty: beginner
status: active
---

## What it does

Automated security scoring for open-source repositories. Checks for branch protection, dependency pinning, signed releases, code review enforcement, CI/CD security, and more. Run it against any GitHub repo.

## Why contribute

- Clean, modular Go codebase — each check is an isolated file
- Adding a new security check is self-contained and beginner-friendly
- Real-world impact: used by GitHub, OpenSSF, and enterprise security teams
- Teaches supply-chain security concepts deeply

## Dev environment setup

```bash
git clone https://github.com/ossf/scorecard
cd scorecard
go build ./...

# Run against a repo (needs GITHUB_AUTH_TOKEN)
export GITHUB_AUTH_TOKEN=<your-pat>
./scorecard --repo github.com/ossf/scorecard --show-details
```

## Where to find good first issues

- https://github.com/ossf/scorecard/labels/good%20first%20issue
- Adding a new security check: look in `checks/` — each check follows the same interface
- Improving test coverage is always welcome

## Community

- Slack: https://openssf.slack.com → `#scorecard`
- Weekly call: https://github.com/ossf/scorecard#contributing
- OpenSSF security reviews: https://github.com/ossf/wg-security-reviews

## Learning resources

- How checks work: read `checks/internal/utils/` and any existing check file
- SLSA levels: https://slsa.dev/
- Supply chain security overview: https://openssf.org/blog/
