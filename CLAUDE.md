# CLAUDE.md — open* repo session instructions

Auto-loaded by Claude Code at session start. Read this before touching any file.

## Purpose

Personal learning and contribution tracker for truly open-source projects.
Scope: 445+ projects (open* + languages + AI/ML + cloud + security + EDA + networking + RAN + ASWF) curated for
**SuryaOS + AI systems + compliance + hardware/software acceleration**.

Goal: learn deeply → become a contributor to each strategic/practical project.

## Session cold-start protocol

1. Read `SESSION.md` — single source of truth for current state and next tasks
2. Read `context.md` — settled decisions; do not re-propose alternatives
3. Check `memory/` — user profile, feedback, project state
4. Start work only after this three-file read

## Repository layout

```
README.md           Best 70 personal strategy + open* map + navigation
ECOSYSTEM.md        Full 445+ project A–L reference tables
context.md          Architecture decisions, scope, ontology design, demo chains
prompts.md          8 LLM prompts for classification, contribution, ontology
SESSION.md          Current state + ordered task list
CLAUDE.md           This file
MY_JOURNEY.md       Personal contribution tracker
CONTRIBUTING.md     Criteria + project file template
memory/             Session memory (synced to GitHub)
ontology/           Knowledge graph schema and seed data (Apache AGE + OWL export)
projects/           Deep-dive contribution guides (strategic/practical tier only, ~20 files)
scripts/            Discovery tooling
```

## Deep-dive files that exist (projects/) — 24 total

OpenTelemetry · OpenBMC · OpenStack · ONNX · OpenVINO · OpenCV · OPA · OpenSearch ·
OpenTofu · OpenTitan · OpenROAD · OpenLineage · OpenSSF Scorecard · Kata Containers ·
OpenEmbedded · OpenSCAP · OpenFeature · OpenAPI · OCI/runc · StarlingX · OpenChain ·
OpenFGA · OpenBao · OpenMetadata

## Standing rules

- **Never add a project without verifying**: OSI license, public repo, active commits
- **No individual .md files for non-strategic projects** — tables only (user instruction)
- **Never edit `ontology/open_star.owl` directly** — regenerate via `ontology/export.py`
- **Ontology changes**: update `seed_concepts.json` + `schema.cypher` together
- **SESSION.md** updated at every session end
- **Commit specific files** — never `git add .` (avoids sweeping in `.open/` venv)
- **Push to GitHub** after every meaningful change

## "Update repo" means

1. Add missing content (files, entries, ontology edges)
2. Update SESSION.md with current state
3. Commit specific files + push to GitHub

## GitHub

Repo: `rajaghv-dev/open-star-map` (public)
Push command: `git push origin master`
