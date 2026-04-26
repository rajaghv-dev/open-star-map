# Contributing to this list

## Adding a project

1. Verify the project meets all criteria (see below)
2. Add a row to the correct category table in `README.md`
3. Create `projects/<project-slug>.md` using the template below
4. Open a PR

## Criteria checklist

- [ ] Name starts with **open** (case-insensitive)
- [ ] License is OSI-approved (Apache-2.0, MIT, GPL, MPL, BSD, etc.)
- [ ] Source code is publicly readable (GitHub, GitLab, opendev.org, etc.)
- [ ] Project accepts external contributions (has CONTRIBUTING.md or equivalent)
- [ ] Last commit within 12 months (active, not abandoned)
- [ ] Not a vendor fork with a closed contribution process

## Project file template

Copy this to `projects/<slug>.md`:

```markdown
---
name: Project Name
url: https://github.com/org/repo
license: Apache-2.0
language: Go
difficulty: beginner | intermediate | advanced
status: active
---

## What it does

One paragraph.

## Why contribute

- What skills you'll build
- Scale / impact of the project

## Dev environment setup

\`\`\`bash
# minimal steps to get a working local build
\`\`\`

## Where to find good first issues

- GitHub label: `good first issue`
- Link: https://github.com/org/repo/labels/good%20first%20issue

## Community

- Mailing list / Slack / IRC / Discord
- Meeting cadence

## Learning resources

- Docs link
- Architecture overview link
- Recommended reading order
```

## Difficulty definitions

| Level | Meaning |
|-------|---------|
| Beginner | Docs, tests, small bug fixes. No deep domain knowledge needed. |
| Intermediate | Feature work; requires understanding the codebase and domain basics. |
| Advanced | Core subsystems, performance, security, protocol work. |
