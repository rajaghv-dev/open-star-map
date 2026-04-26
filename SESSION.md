# SESSION.md — open* repo current state

Last updated: 2026-04-26

---

## What exists and works

| Item | Status |
|------|--------|
| `README.md` | 100 open* projects, 16 categories, strategic/practical/watchlist tiers, demo chain |
| `ontology/` | Full AGE graph schema, seed concepts (8 layers, 16 categories, 30 concepts), relationships.json, bootstrap.cypher, export.py |
| `CONTRIBUTING.md` | Criteria checklist + project file template |
| `MY_JOURNEY.md` | Personal contribution tracker (empty — fill in as you start) |
| `scripts/discover.py` | GitHub API search with contributor-friendliness scoring |
| `CLAUDE.md` | Session instructions (auto-loaded by Claude Code) |

## Deep-dive project files (`projects/`)

| File | Project | Tier |
|------|---------|------|
| `opentelemetry.md` | OpenTelemetry | Strategic + Practical |
| `openbmc.md` | OpenBMC | Strategic |
| `openstack.md` | OpenStack | Strategic |
| `onnx.md` | ONNX | Strategic + Practical |
| `openvino.md` | OpenVINO | Strategic + Practical |
| `opencv.md` | OpenCV | Strategic + Practical |
| `open-policy-agent.md` | OPA | Strategic + Practical |
| `opensearch.md` | OpenSearch | Strategic + Practical |
| `opentofu.md` | OpenTofu | — |
| `opentitan.md` | OpenTitan | Strategic + Watchlist |
| `openroad.md` | OpenROAD | Strategic + Watchlist |
| `openlineage.md` | OpenLineage | Watchlist |
| `openssf-scorecard.md` | OpenSSF Scorecard | Strategic + Practical |
| `kata-containers.md` | Kata Containers | Strategic |
| `openembedded.md` | OpenEmbedded | Strategic |
| `openscap.md` | OpenSCAP | Strategic + Practical |
| `openfeature.md` | OpenFeature | Practical (beginner) |
| `openapi.md` | OpenAPI | Strategic |
| `open-container-initiative.md` | OCI / runc | Strategic |

---

## Strategic projects still needing deep-dive files

High priority — these are in Strategic or Practical tier:

| Project | Tier | Why urgent |
|---------|------|------------|
| StarlingX | Strategic | Edge/telco cloud — complex, unique skills |
| OpenChain | Strategic | Compliance standard — beginner-friendly contribution |
| OpenSSF (umbrella) | Strategic | Multiple working groups, many beginner issues |
| OpenEBS | Practical | Kubernetes storage — active CNCF project |
| OpenFGA | Watchlist | Fine-grained authz — Go, growing fast |
| OpenBao | Watchlist | Vault fork — Go, active migration from HashiCorp |
| OpenDataHub | Watchlist | AI/data platform on K8s |
| OpenMetadata | Watchlist | Pairs with OpenLineage |

---

## Next tasks (ordered by priority)

### P0 — Start contributing
- [ ] Pick one Beginner project from Practical tier
  - Best options: OpenTelemetry, OpenFeature, OpenSSF Scorecard, OpenRefine
- [ ] Set up dev environment (follow the project's `.md` file)
- [ ] Find a `good first issue`, assign yourself
- [ ] Update `MY_JOURNEY.md` with status

### P1 — Fill remaining deep-dive files
- [ ] `projects/starlingx.md`
- [ ] `projects/openchain.md`
- [ ] `projects/openssf.md`
- [ ] `projects/openfga.md`
- [ ] `projects/openbao.md`

### P2 — Bootstrap the knowledge graph
- [ ] Install Apache AGE: `docker run -p 5432:5432 apache/age:PG16_latest`
- [ ] Run `ontology/bootstrap.cypher` to seed the graph
- [ ] Load full project list via a Python loader script
- [ ] Run `ontology/export.py` to generate `open_star.owl`
- [ ] Open in Protégé and verify the ontology hierarchy

### P3 — Discovery automation
- [ ] Run `scripts/discover.py --token <pat> --min-stars 100` to find new open* projects
- [ ] Triage results against criteria in `CONTRIBUTING.md`
- [ ] Add qualified projects to `README.md` and `ontology/relationships.json`

### P4 — Push to GitHub
- [ ] `gh repo create open-star-map --public --source=. --push`
- [ ] Add GitHub Actions CI: validate JSON files, check dead links in README

---

## Key design decisions (do not re-debate)

| Decision | Rationale |
|----------|-----------|
| Apache AGE = live ontology | Graph IS the ontology; OWL is export-only |
| OWL / owlready2 = inspection only | Same pattern as CFP conference pipeline |
| `seed_concepts.json` is hand-authored | Bootstrapped before any automation |
| `relationships.json` = explicit edges | Not inferred — human-verified connections only |
| 100-project scope | User-provided list; non-OSS projects flagged clearly |
| Difficulty ratings | beginner/intermediate/advanced — conservative, not aspirational |
