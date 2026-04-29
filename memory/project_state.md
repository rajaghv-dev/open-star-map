---
name: open* repo — current state
description: Repo location, what exists, current phase, key decisions
type: project
---

## Repo
- **Local:** `/home/raja/open`
- **GitHub:** `rajaghv-dev/open-star-map` (public)
- **Branch:** master

## What exists (2026-04-29)

### Core files
| File | Status |
|------|--------|
| `README.md` | Best 70 control plane + open* map + navigation |
| `ECOSYSTEM.md` | Full 445+ project A–L reference tables (Section L added 2026-04-29: networking, RAN, AI agents, ASWF) |
| `context.md` | Architecture decisions, scope, ontology design, demo chains |
| `prompts.md` | 8 LLM prompts for classification, contribution planning, ontology |
| `SESSION.md` | Current state + ordered task list |
| `CLAUDE.md` | Session instructions (auto-loaded) |
| `MY_JOURNEY.md` | Personal contribution tracker |
| `CONTRIBUTING.md` | Criteria + project file template |
| `memory/` | This directory — synced to repo |

### Ontology files
| File | Status |
|------|--------|
| `ontology/README.md` | Node labels, edge types, stack layer order |
| `ontology/seed_concepts.json` | 8 stack layers, 16 categories, skills, foundations, 30 concepts |
| `ontology/relationships.json` | Known project edges (DEPENDS_ON, COMPLEMENTS, SUPERSEDES, etc.) |
| `ontology/schema.cypher` | Apache AGE DDL + query examples |
| `ontology/bootstrap.cypher` | One-time idempotent graph init |
| `ontology/export.py` | AGE → owlready2 → open_star.owl |

### Deep-dive project files (projects/) — 24 total
OpenTelemetry · OpenBMC · OpenStack · ONNX · OpenVINO · OpenCV · OPA · OpenSearch ·
OpenTofu · OpenTitan · OpenROAD · OpenLineage · OpenSSF Scorecard · Kata Containers ·
OpenEmbedded · OpenSCAP · OpenFeature · OpenAPI · OCI/runc · StarlingX · OpenChain ·
OpenFGA · OpenBao · OpenMetadata

### Scripts
| File | Status |
|------|--------|
| `scripts/discover.py` | GitHub API search + contributor-friendliness scorer |

### CI
| File | Status |
|------|--------|
| `.github/workflows/validate.yml` | JSON / Python compile / ruff / unittest / link / frontmatter checks |
| `.github/ISSUE_TEMPLATE.md` | Issue template |

### Tests
| File | Status |
|------|--------|
| `ontology/tests/test_static.py` | 12 stdlib unittest checks — runs in CI |
| `ontology/tests/test_age_integration.py` | 7 AGE round-trip tests — auto-skip without `OPEN_STAR_AGE_DSN` |
| `ontology/tests/README.md` | How to run + Docker recipe for AGE |

## Current phase
**Repository complete. Pre-contribution.**
All reference material is in place; deep-dives cover every Strategic and named Watchlist
project; CI validates JSON, Python, links, and frontmatter on every push.
Next step: pick a P0 project (OpenTelemetry / OpenFeature / OpenSSF Scorecard),
set up the dev environment, claim a `good first issue`.

## Key design decisions
- Apache AGE = live ontology; OWL = export-only (same pattern as CFP conference pipeline)
- 430+ projects across 11 categories (A–K) in ECOSYSTEM.md
- Best 70 personal strategy in README.md
- Deep-dives only for strategic/practical tier (~20 files)
- Session continuity: CLAUDE.md + SESSION.md + memory/ (all synced to GitHub)

## How to apply
Read CLAUDE.md and SESSION.md first every session.
Architecture is settled in context.md — do not re-propose alternatives.
