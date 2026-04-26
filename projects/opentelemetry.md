---
name: OpenTelemetry
url: https://github.com/open-telemetry/opentelemetry-collector
license: Apache-2.0
language: Go (collector), multi-language SDKs
difficulty: beginner
status: active
---

## What it does

Vendor-neutral framework for collecting, processing, and exporting traces, metrics, and logs. Backed by CNCF. Used by every major cloud vendor and observability tool.

## Why contribute

- Teaches distributed systems observability concepts (traces, spans, metrics)
- Go codebase is well-structured and heavily tested
- Very active community — PRs get reviewed fast
- Real impact: runs in millions of production systems

## Dev environment setup

```bash
git clone https://github.com/open-telemetry/opentelemetry-collector-contrib
cd opentelemetry-collector-contrib
go build ./...
make test
```

For the core collector:
```bash
git clone https://github.com/open-telemetry/opentelemetry-collector
cd opentelemetry-collector
make build
./bin/otelcol --config examples/demo/otel-collector-config.yaml
```

## Where to find good first issues

- https://github.com/open-telemetry/opentelemetry-collector/labels/good%20first%20issue
- https://github.com/open-telemetry/opentelemetry-collector-contrib/labels/good%20first%20issue
- Look for `help wanted` + `easy` labels

## Community

- Slack: https://cloud-native.slack.com → `#otel-collector`
- SIG meetings: https://github.com/open-telemetry/community#special-interest-groups
- Weekly community calls (recorded on YouTube)

## Learning resources

- Docs: https://opentelemetry.io/docs/
- Architecture: https://opentelemetry.io/docs/collector/architecture/
- Start here: read `receiver → processor → exporter` pipeline concepts
- Good intro blog: "OpenTelemetry Collector in practice"
