---
name: OpenLineage
url: https://github.com/OpenLineage/OpenLineage
license: Apache-2.0
language: Python, Java
difficulty: intermediate
status: active
---

## What it does

Standard for data pipeline lineage metadata. Integrates with Spark, Airflow, dbt, Flink, and more. Emits lineage events (dataset inputs/outputs, job runs) in a common schema. Pairs with OpenMetadata for a complete data governance stack.

## Why contribute

- Teaches data lineage concepts: provenance, impact analysis, data quality
- Python integrations with popular frameworks are easy entry points
- Java core + Python integrations — choose your comfort zone
- Growing ecosystem: Marquez (server), Atlan, DataHub all consume OpenLineage events

## Dev environment setup

```bash
git clone https://github.com/OpenLineage/OpenLineage
cd OpenLineage

# Python client
cd client/python
pip install -e ".[dev]"
pytest

# Airflow integration
cd integration/airflow
pip install -e ".[dev]"
```

## Where to find good first issues

- https://github.com/OpenLineage/OpenLineage/labels/good%20first%20issue
- New integration adapters for frameworks
- Spec documentation improvements

## Community

- Slack: https://bit.ly/OpenLineageSlack
- GitHub Discussions: https://github.com/OpenLineage/OpenLineage/discussions
- Meetings: listed in repo README

## Learning resources

- Spec: https://openlineage.io/spec/
- Marquez (reference server): https://github.com/MarquezProject/marquez
- Demo: Airflow DAG → OpenLineage events → Marquez → OpenMetadata catalog
