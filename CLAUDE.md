# CLAUDE.md — open* repo session instructions

Auto-loaded by Claude Code at session start. Read this before touching any file.

## Purpose

This repo is a personal learning and contribution tracker for open-source projects
whose name starts with **open*** — covering the full stack from silicon root-of-trust
to data governance. Goal: learn deeply → become a contributor to each strategic project.

## Session cold-start

1. Read `SESSION.md` — single source of truth for current state and next tasks
2. Read `README.md` — full 100-project map with tier annotations
3. Read `ontology/README.md` — graph schema (add relationships there, not inline)
4. Check `projects/` — deep-dive files exist for: OpenTelemetry, OpenBMC, OpenStack,
   ONNX, OpenVINO, OpenCV, OPA, OpenSearch, OpenTofu, OpenTitan, OpenROAD,
   OpenLineage, OpenSSF Scorecard, Kata Containers, OpenEmbedded, OpenSCAP,
   OpenFeature, OpenAPI, OCI/runc

## Standing rules

- **Never add a project without verifying**: OSI-approved license, public repo, active commits
- **Never edit `ontology/open_star.owl` directly** — regenerate via `ontology/export.py`
- **Deep-dive files** go in `projects/<slug>.md` and use the template in `CONTRIBUTING.md`
- **Ontology changes** (new node labels, edge types, concepts) → update `ontology/seed_concepts.json`
  and `ontology/schema.cypher` together
- **SESSION.md** must be updated at end of every session
- Commit specific files — never `git add .` (avoids sweeping in `.open/` venv artifacts)

## Repo layout

```
README.md              100-project map + tier annotations
SESSION.md             Current state + ordered task list
CONTRIBUTING.md        Criteria + project file template
MY_JOURNEY.md          Personal contribution tracker
ontology/              Knowledge graph schema and seed data
  README.md            Node labels, edge types, stack layer order
  seed_concepts.json   Hand-authored taxonomy (edit here first)
  schema.cypher        Apache AGE DDL + query examples
  bootstrap.cypher     One-time idempotent graph init
  relationships.json   Known project↔project edges
  export.py            AGE → owlready2 → open_star.owl
projects/              Deep-dive contribution guides (one per project)
scripts/discover.py    GitHub API search + contributor-friendliness scorer
```

## What "update repo" means in this context

- Add missing deep-dive files for strategic/practical tier projects
- Update `SESSION.md` to reflect current state
- Add new `ontology/relationships.json` entries when project interactions are discovered
- Keep `README.md` accurate — flag archived or relicensed projects
