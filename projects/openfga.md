---
name: OpenFGA
url: https://github.com/openfga/openfga
license: Apache-2.0
language: Go
difficulty: intermediate
status: active
---

## What it does

CNCF sandbox project implementing fine-grained authorization based on Google's Zanzibar paper. Stores relationship tuples (`user → relation → object`) and answers `check`, `list-objects`, and `expand` queries with strong consistency. Production-grade alternative to writing custom RBAC/ABAC every time.

## Why contribute

- Touches a clean, well-tested Go codebase with explicit interfaces between API, storage, and graph engine
- Authorization is a hot area — Zanzibar-style systems are now table stakes
- SDKs in Go, JS, Python, Java, .NET — pick your contribution surface
- Roadmap is public; "good first issue" labels are real entry points, not aspirational

## Dev environment setup

```bash
git clone https://github.com/openfga/openfga
cd openfga
make build
make test

# Run server with in-memory storage
./openfga run --datastore-engine memory

# In another shell: try the playground
docker run -p 3000:3000 openfga/playground
```

## Where to find good first issues

- https://github.com/openfga/openfga/labels/good%20first%20issue
- SDK gaps: https://github.com/openfga (each language SDK has its own backlog)
- Sample stores and example apps: https://github.com/openfga/sample-stores

## Community

- CNCF Slack: `#openfga`
- Bi-weekly community calls
- Roadmap: https://github.com/orgs/openfga/projects

## Learning resources

- Concepts: https://openfga.dev/docs/concepts
- Modeling guide: https://openfga.dev/docs/modeling
- Original Zanzibar paper (read first): https://research.google/pubs/pub48190/
- Read order in repo: `pkg/server/commands/check.go` → `pkg/storage/` → `internal/graph/`
