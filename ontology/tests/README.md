# Ontology tests

Two suites:

| Suite | Requires | Runs in CI? |
|-------|----------|-------------|
| `test_static.py` | stdlib only | yes |
| `test_age_integration.py` | `psycopg` + Apache AGE Postgres + `OPEN_STAR_AGE_DSN` env var | no — auto-skips |

## Run

```bash
# static (always works)
python3 -m unittest discover -s ontology/tests -v

# integration (needs AGE)
docker run --rm -d --name age -p 5455:5432 \
    -e POSTGRES_PASSWORD=postgres apache/age:PG16_latest
sleep 5
export OPEN_STAR_AGE_DSN="postgresql://postgres:postgres@localhost:5455/postgres"
python3 -m unittest ontology.tests.test_age_integration -v
docker stop age
```

## What the integration test does

1. Creates an **ephemeral** AGE graph named `open_star_test_<uuid>` so it cannot
   collide with the real `open_star_graph`.
2. Inserts dummy nodes (StackLayer, Tier, 3 Projects) and edges
   (`RUNS_ON`, `DEPENDS_ON`, `COMPLEMENTS`, `IN_TIER`).
3. Runs assertion queries — node counts, traversals, demo-chain ordering.
4. **Cleanup:** drops the entire test graph via `SELECT drop_graph(..., true)`.
   Cleanup runs in `tearDown`, so it executes even on test failure.

No data is left behind in `open_star_graph` or in any other graph.
