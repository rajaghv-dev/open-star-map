---
name: OpenSearch
url: https://github.com/opensearch-project/OpenSearch
license: Apache-2.0
language: Java
difficulty: intermediate
status: active
---

## What it does

Open-source fork of Elasticsearch 7.10, maintained by AWS and community. Full-text search, log analytics, and observability platform. Includes OpenSearch Dashboards (Kibana fork).

## Why contribute

- Teaches distributed search engine internals (Lucene, sharding, replication)
- Large, modular Java codebase — many isolated areas to contribute to
- Active community with defined SIG structure
- Real-world scale: petabytes of data in production

## Dev environment setup

```bash
git clone https://github.com/opensearch-project/OpenSearch
cd OpenSearch

# Build (requires JDK 17+)
./gradlew assemble

# Run a local node
./gradlew run

# REST API
curl http://localhost:9200/
```

## Where to find good first issues

- https://github.com/opensearch-project/OpenSearch/labels/good%20first%20issue
- https://github.com/opensearch-project/OpenSearch/labels/help%20wanted
- Dashboards (UI): https://github.com/opensearch-project/OpenSearch-Dashboards/labels/good%20first%20issue

## Community

- Forum: https://forum.opensearch.org/
- Slack: https://opensearch.org/slack.html
- GitHub Discussions: https://github.com/opensearch-project/OpenSearch/discussions

## Learning resources

- Docs: https://opensearch.org/docs/
- Architecture: https://opensearch.org/docs/latest/about/
- Lucene basics: https://lucene.apache.org/core/documentation.html
- Start with: a REST API test or documentation fix
