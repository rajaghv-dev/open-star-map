---
name: Standing behaviors and feedback
description: How to behave every session in this repo
type: feedback
---

## Push to GitHub after every meaningful session
Always commit specific files and push. Never `git add .` (sweeps in .open/ venv artifacts).
**Why:** User explicitly asks to "update github" as a standing instruction.

## Read CLAUDE.md + SESSION.md + context.md before acting
Session cold-start protocol. Do not propose structural changes without reading these first.
**Why:** Architecture is settled. Re-proposing wastes time.

## No individual .md files for non-strategic projects
Tables in README.md and ECOSYSTEM.md only. Deep-dives (projects/) for strategic tier only (~20).
**Why:** User said "no need to write separate md files for all the identified."

## Comprehensive documentation, terse code edits
Deep when task is docs, analysis, or prompts. Terse for file edits and git ops.
**Why:** User accepted and built on thorough reference outputs.

## "Update repo" means
1. Add missing content (files, project entries, ontology edges)
2. Update SESSION.md with current state
3. Commit and push to GitHub
It does NOT mean restructure everything from scratch.

## Memory files stay in sync with repo
memory/ directory is git-tracked and pushed every session.
**Why:** User wants "all files in repo, not just local machine" (same as CFP project).

## Ontology changes flow through seed_concepts.json first
Update seed_concepts.json → schema.cypher together. Never directly edit open_star.owl.
**Why:** Settled design decision. OWL is regenerated from AGE graph, not edited.
