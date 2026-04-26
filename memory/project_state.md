---
name: open* repo — current state
description: Repo location, what exists, current phase, key decisions
type: project
---

## Repo
- **Local:** `/home/raja/open`
- **GitHub:** `rajaghv-dev/open-star-map` (public)
- **Branch:** master

## What exists (2026-04-26)

### Core files
| File | Status |
|------|--------|
| `README.md` | Best 70 control plane + open* map + navigation |
| `ECOSYSTEM.md` | Full 430+ project A–K reference tables |
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

### Deep-dive project files (projects/)
OpenTelemetry · OpenBMC · OpenStack · ONNX · OpenVINO · OpenCV · OPA · OpenSearch ·
OpenTofu · OpenTitan · OpenROAD · OpenLineage · OpenSSF Scorecard · Kata Containers ·
OpenEmbedded · OpenSCAP · OpenFeature · OpenAPI · OCI/runc

### Scripts
| File | Status |
|------|--------|
| `scripts/discover.py` | GitHub API search + contributor-friendliness scorer |

## Current phase
**Repository complete. Pre-contribution.**
All reference material is in place. Next step: pick a project, set up dev environment, find a good first issue.

## Key design decisions
- Apache AGE = live ontology; OWL = export-only (same pattern as CFP conference pipeline)
- 430+ projects across 11 categories (A–K) in ECOSYSTEM.md
- Best 70 personal strategy in README.md
- Deep-dives only for strategic/practical tier (~20 files)
- Session continuity: CLAUDE.md + SESSION.md + memory/ (all synced to GitHub)

## How to apply
Read CLAUDE.md and SESSION.md first every session.
Architecture is settled in context.md — do not re-propose alternatives.
