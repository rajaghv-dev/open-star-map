# SESSION.md — open* repo current state

Last updated: 2026-04-29

---

## What exists and works

| Item | Status |
|------|--------|
| `README.md` | Best 70 personal strategy + open* map + navigation |
| `ECOSYSTEM.md` | Full 445+ project A–L reference (languages, AI/ML, cloud, security, EDA, networking, RAN, ASWF, etc.) |
| `context.md` | Architecture decisions, scope, ontology design, demo chains |
| `prompts.md` | 8 LLM prompts (classify, GFI strategy, verify OSS, deep-dive gen, score, map relations, Cypher gen, cold-start) |
| `SESSION.md` | This file |
| `CLAUDE.md` | Session instructions (auto-loaded) |
| `MY_JOURNEY.md` | Personal contribution tracker (fill as you go) |
| `CONTRIBUTING.md` | Criteria + project file template |
| `memory/MEMORY.md` | Memory index |
| `memory/user_profile.md` | Background, fluency, goals |
| `memory/project_state.md` | Repo state, decisions |
| `memory/feedback.md` | Standing behaviors |
| `ontology/README.md` | Node labels, edge types, stack layer order |
| `ontology/seed_concepts.json` | v2.0: 8 layers, A-K categories, 9 strategy groups, 17 skills, 42 concepts |
| `ontology/relationships.json` | Known project edges |
| `ontology/schema.cypher` | Apache AGE DDL |
| `ontology/bootstrap.cypher` | One-time graph init |
| `ontology/export.py` | AGE → OWL |
| `scripts/discover.py` | GitHub search + contributor scoring |

## Deep-dive project files (24 total)

OpenTelemetry · OpenBMC · OpenStack · ONNX · OpenVINO · OpenCV · OPA · OpenSearch ·
OpenTofu · OpenTitan · OpenROAD · OpenLineage · OpenSSF Scorecard · Kata Containers ·
OpenEmbedded · OpenSCAP · OpenFeature · OpenAPI · OCI/runc · StarlingX · OpenChain ·
OpenFGA · OpenBao · OpenMetadata

## CI

`.github/workflows/validate.yml` — validates JSON, compiles Python, lints with ruff,
runs ontology static tests, checks relative .md links, verifies projects/*.md
frontmatter on push/PR to master.

## Tests

| File | Type | Runs in CI |
|------|------|------------|
| `ontology/tests/test_static.py` | stdlib unittest — JSON/Cypher/frontmatter checks | yes (12 tests) |
| `ontology/tests/test_age_integration.py` | psycopg + AGE — ephemeral graph round-trip | auto-skip without DB (7 tests) |

Integration test creates `open_star_test_<uuid>`, inserts dummy `test-*` projects
and edges, asserts traversal and demo-chain ordering, drops the graph in tearDown.
See `ontology/tests/README.md` for the local Docker recipe.

---

## Next tasks (ordered)

### P0 — Start contributing NOW
Pick one project from Practical tier. Best entry points:
| Project | Why start here | Good first issue URL |
|---------|---------------|----------------------|
| OpenTelemetry | Largest CNCF community, Go, fastest PR reviews | [→](https://github.com/open-telemetry/opentelemetry-collector/labels/good%20first%20issue) |
| OpenFeature | Small SDKs, pick your language, spec-driven | [→](https://github.com/open-feature/go-sdk/labels/good%20first%20issue) |
| OpenSSF Scorecard | Go, isolated check modules, security focus | [→](https://github.com/ossf/scorecard/labels/good%20first%20issue) |
| RAGAS | Python, evaluation focus, AI-adjacent | [→](https://github.com/explodinggradients/ragas/labels/good%20first%20issue) |

Steps:
- [ ] Pick one project above
- [ ] Follow its `projects/*.md` dev setup
- [ ] Assign yourself a `good first issue`
- [ ] Update `MY_JOURNEY.md` status → `exploring`

### P1 — Bootstrap the knowledge graph
- [ ] `docker run -p 5432:5432 apache/age:PG16_latest`
- [ ] `psql -f ontology/bootstrap.cypher`
- [ ] Load all projects from ECOSYSTEM.md via Python loader
- [ ] Run `python3 ontology/export.py --dsn ... --output ontology/open_star.owl`
- [ ] Open `open_star.owl` in Protégé

### P2 — Run discovery
- [ ] `python3 scripts/discover.py --token <pat> --min-stars 100 --json > /tmp/discovered.json`
- [ ] Triage against criteria in `CONTRIBUTING.md`
- [ ] Add qualified projects to ECOSYSTEM.md and `ontology/relationships.json`

### P3 — Fill remaining deep-dives (strategic/watchlist) — DONE 2026-04-29
- [x] `projects/starlingx.md`
- [x] `projects/openchain.md`
- [x] `projects/openfga.md`
- [x] `projects/openbao.md`
- [x] `projects/openmetadata.md`

### P4 — GitHub Actions CI — DONE 2026-04-29
- [x] `.github/workflows/validate.yml` — JSON validation, Python compile, ruff lint,
      relative-link check, frontmatter check on every push/PR to master

### P5 — Ontology test harness — DONE 2026-04-29
- [x] `ontology/tests/test_static.py` — 12 stdlib unittest checks
- [x] `ontology/tests/test_age_integration.py` — ephemeral-graph round-trip
- [x] CI wired: `python -m unittest discover -s ontology/tests`

### P6 — Ecosystem expansion (Section L) — DONE 2026-04-29
- [x] OpenFPGA, OpenAirInterface, OKD, Open vSwitch, OVN, OpenConfig
- [x] OpenHands, Open Interpreter (AI agents)
- [x] OpenUSD, OpenEXR, OpenColorIO (ASWF film/VFX)
- [x] OpenZFS, OpenNebula, OpenStreetMap, OpenAlex
- [x] Watchlist tier expanded; relationships.json edges added (OVN→OVS,
      OpenAirInterface↔StarlingX, OVS↔OpenStack, OpenHands→OpenTelemetry, etc.)

### P7 — Future improvements (open)
- [ ] Project loader: parse ECOSYSTEM.md tables → ontology Cypher INSERTs
- [ ] First entry in `MY_JOURNEY.md` after picking a P0 project
- [ ] Add badges (CI status, license, contributors) to README.md
- [ ] Move "Best 70" personal strategy out of README into its own `STRATEGY.md`
- [ ] Optional CI matrix: integration test job that spins up an AGE container

---

## Key decisions (settled — do not re-debate)

| Decision | See |
|----------|-----|
| Apache AGE = live ontology, OWL = export-only | context.md §Ontology design |
| No individual .md for non-strategic projects | context.md §File structure |
| Best 70 personal strategy groups | README.md + context.md |
| Commit specific files only, never git add . | memory/feedback.md |
| Push to GitHub after every session | memory/feedback.md |
