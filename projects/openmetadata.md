---
name: OpenMetadata
url: https://github.com/open-metadata/OpenMetadata
license: Apache-2.0
language: Java, Python, TypeScript
difficulty: intermediate
status: active
---

## What it does

Unified metadata platform: data catalog, lineage, data quality, glossary, and observability across data sources (databases, dashboards, pipelines, ML models, messaging systems). Built around a JSON-Schema-defined entity model, served through a REST API and a React UI. Pairs naturally with OpenLineage for runtime lineage events.

## Why contribute

- Metadata is where data, AI, and governance converge — crucial for compliance and AI workload provenance
- Polyglot codebase (Java backend, Python ingestion connectors, TS frontend) lets you pick a surface
- Connector ecosystem is the easiest entry: each new source adapter is self-contained
- Active CNCF-adjacent governance, real "good first issue" pipeline

## Dev environment setup

```bash
git clone https://github.com/open-metadata/OpenMetadata
cd OpenMetadata

# Backend (Java + Maven)
mvn clean install -DskipTests

# Ingestion framework (Python)
cd ingestion
pip install -e ".[dev]"
pytest tests/unit

# UI (React + Yarn)
cd ../openmetadata-ui/src/main/resources/ui
yarn install
yarn start

# Or use Docker compose for full stack
docker compose -f docker/docker-compose-quickstart/docker-compose.yml up
```

## Where to find good first issues

- https://github.com/open-metadata/OpenMetadata/labels/good%20first%20issue
- Connector requests: https://github.com/open-metadata/OpenMetadata/labels/connector
- Documentation: https://github.com/open-metadata/OpenMetadata/labels/documentation

## Community

- Slack: https://slack.open-metadata.org
- Monthly community meeting (calendar on website)
- Discussions: https://github.com/open-metadata/OpenMetadata/discussions

## Learning resources

- Concept docs: https://docs.open-metadata.org/main-concepts
- Entity schemas: https://github.com/open-metadata/OpenMetadata/tree/main/openmetadata-spec/src/main/resources/json/schema
- Suggested read order: `entity/data/table.json` schema → `ingestion/src/metadata/ingestion/source/` for a connector → `openmetadata-service/` for the API
- Pairs with OpenLineage for runtime lineage events (see `projects/openlineage.md`)
