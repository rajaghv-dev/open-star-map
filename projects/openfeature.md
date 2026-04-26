---
name: OpenFeature
url: https://github.com/open-feature
license: Apache-2.0
language: Go, TypeScript, Java, Python, .NET, PHP, Ruby
difficulty: beginner
status: active
---

## What it does

Vendor-neutral standard and SDK for feature flags. Define a common interface so your code isn't locked to any one feature flag provider (LaunchDarkly, Flagsmith, etc.). CNCF incubating project. Each language SDK is a separate repo under the `open-feature` GitHub org.

## Why contribute

- Easiest CNCF project to make a first contribution to — small, isolated SDKs
- Pick your language: Go, TypeScript, Python, Java — all follow the same spec
- Teaches SDK design: interface-first, provider pattern, context propagation
- Good first issue label is actively maintained

## Dev environment setup

```bash
# Pick one SDK — Go example:
git clone https://github.com/open-feature/go-sdk
cd go-sdk
go test ./...

# TypeScript:
git clone https://github.com/open-feature/js-sdk
cd js-sdk
npm install && npm test

# Python:
git clone https://github.com/open-feature/python-sdk
cd python-sdk
pip install -e ".[dev]" && pytest
```

## Where to find good first issues

- https://github.com/open-feature/go-sdk/labels/good%20first%20issue
- https://github.com/open-feature/js-sdk/labels/good%20first%20issue
- Spec conformance tests are always needed
- Provider implementations for open-source flag backends

## Community

- Slack: https://cloud-native.slack.com → `#openfeature`
- Bi-weekly calls: https://github.com/open-feature/community
- Spec repo: https://github.com/open-feature/spec

## Learning resources

- Spec: https://openfeature.dev/specification/
- Provider guide: https://openfeature.dev/docs/reference/concepts/provider
- Start with: add a missing SDK hook test, or write a provider for an open-source flag service
