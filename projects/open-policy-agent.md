---
name: Open Policy Agent
url: https://github.com/open-policy-agent/opa
license: Apache-2.0
language: Go
difficulty: intermediate
status: active
---

## What it does

General-purpose policy engine. You write policies in Rego (a declarative language), and OPA evaluates them. Used for Kubernetes admission control, API authorization, infrastructure compliance.

## Why contribute

- Teaches policy-as-code and authorization system design
- Go codebase is clean and well-documented
- CNCF graduated project — rigorous review process teaches good practices
- Rego language interpreter is a fascinating compiler/eval target to study

## Dev environment setup

```bash
git clone https://github.com/open-policy-agent/opa
cd opa
make build
./opa_linux_amd64 version

# Run tests
make test

# Try the REPL
./opa_linux_amd64 run --repl
```

## Where to find good first issues

- https://github.com/open-policy-agent/opa/labels/good%20first%20issue
- https://github.com/open-policy-agent/opa/labels/help%20wanted
- Rego playground improvements: https://github.com/open-policy-agent/opa/tree/main/rego

## Community

- Slack: https://slack.openpolicyagent.org/
- Monthly community meetings: https://github.com/open-policy-agent/community
- Blog: https://blog.openpolicyagent.org/

## Learning resources

- Rego language: https://www.openpolicyagent.org/docs/latest/policy-language/
- How OPA works: https://www.openpolicyagent.org/docs/latest/philosophy/
- Start with: adding a Rego built-in function or fixing a docs example
