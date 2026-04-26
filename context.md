# context.md — architecture decisions and scope

Auto-loaded via CLAUDE.md. Read before proposing any structural changes.

---

## Project scope

This repo is a **personal learning and contribution tracker** for truly open-source projects.
Scope: 500+ projects across languages, AI/ML, agent frameworks, cloud, observability, security,
firmware, hardware/EDA, and developer tools — curated for SuryaOS + AI systems + compliance +
hardware/software acceleration.

Not a documentation project. Not a one-project deep-dive. A **map** of the full open-source
control plane and a tracker for personal progression through it.

---

## Settled decisions (do not re-debate)

### 1. Ontology design
- **Apache AGE (Cypher) = live ontology.** The graph is always current and queryable.
- **OWL / owlready2 = export-only.** Never edited directly. Regenerated from graph by `ontology/export.py`.
- **`seed_concepts.json` = hand-authored first.** Automation (discover.py) adds RawTags; those normalize to Concepts.
- **`relationships.json` = human-verified edges only.** No inferred edges.
- Stack layers are ordered 1–8 (Silicon → Data). This ordering drives demo chain sequencing.
- Same design as the CFP conference knowledge pipeline (AGE + owlready2 + seed-first pattern).

### 2. Scope boundary
- "Truly open source" = OSI-approved or equivalent recognized license (Apache-2.0, MIT, BSD, GPL, LGPL, MPL, EPL, AGPL, ISC, PSF, etc.)
- Source-available but non-OSI projects (BUSL, proprietary) are listed under "Not truly open" sections only.
- OpenAI is NOT open source. Listed for awareness only with that label.
- Archived projects (OpenTracing, OpenCensus) listed with clear archive note.

### 3. File structure
- No individual .md deep-dive files for the 430+ non-strategic projects. Only tables in README + ECOSYSTEM.md.
- Deep-dive files (`projects/`) exist only for the ~20 strategic/practical tier projects.
- `ECOSYSTEM.md` = full 430+ project reference (A–K categories). README = summary + Best 70 + navigation.
- `prompts.md` = LLM prompts. `context.md` = this file. `SESSION.md` = current state.

### 4. Best 70 personal strategy
The 70-project control plane is organized into 9 themed groups (not a flat list):
Systems foundation → Languages → AI/ML core → LLM+agents → Cloud/containers → Observability → Security → Hardware/EDA → Desktop/media.
These are the projects to contribute to first, in roughly that priority order.

### 5. Contribution approach
- Start beginner-labeled projects in practical tier.
- Work up the stack layer order: start at layer 5 (Observability) or layer 6 (Security) — most beginner-friendly.
- Layer 1 (Silicon/EDA) and Layer 2 (Firmware) require deep background; schedule after building the stack above.
- Track every contribution in `MY_JOURNEY.md`.

### 6. GitHub
- Repo: `rajaghv-dev/open-star-map` (public)
- Commit specific files only — never `git add .`
- Push after every meaningful session

---

## Ontology node labels (full set)

| Label | Description |
|-------|-------------|
| `Project` | Any open-source project in scope |
| `Category` | A-K domain categories + open* sub-categories |
| `StackLayer` | 1=Silicon, 2=Firmware, 3=OS/Net, 4=Cloud, 5=Obs, 6=Security, 7=AI, 8=Data |
| `Foundation` | OpenInfra, CNCF, LF, Apache, Eclipse, lowRISC, etc. |
| `Language` | Implementation language |
| `License` | SPDX license ID |
| `Skill` | What contributing teaches |
| `Tier` | Strategic / Practical / Watchlist / NotOSS |
| `Spec` | A standard the project implements |
| `RawTag` | Free-form tag pre-normalization |
| `Concept` | Normalized ontology concept |
| `PersonalStrategy` | Best-70 themed group |

## Ontology edge types (full set)

`RUNS_ON` · `BELONGS_TO` · `GOVERNED_BY` · `WRITTEN_IN` · `LICENSED_AS` ·
`TEACHES` · `IN_TIER` · `IN_STRATEGY_GROUP` · `DEPENDS_ON` · `COMPLEMENTS` ·
`SUPERSEDES` · `MERGES_INTO` · `IMPLEMENTS_SPEC` · `PART_OF` · `NORMALIZES_TO`

---

## Demo chains

### Primary (end-to-end AI infra + security)
```
OpenTitan (RoT) → OpenBMC (firmware) → OpenStack/OCI (cloud/containers)
→ ONNX → OpenVINO/vLLM (inference) → LangGraph (agent)
→ OpenTelemetry (traces) → OpenSearch (logs)
→ OPA (policy gate) → OpenSCAP (compliance) → OpenSSF Scorecard
→ OpenLineage (data lineage)
```

### RAG evaluation chain
```
LlamaIndex/LangGraph → RAGAS → OpenCompass → MLflow (tracking)
```

### Hardware simulation chain
```
Yosys (synthesis) → Verilator (simulation) → cocotb (test)
→ OpenROAD (place-route) → OpenTitan (RoT integration)
```

---

## Ecosystem statistics

| Category | Count |
|----------|-------|
| Languages, runtimes, compilers (A) | 50 |
| AI/ML frameworks (B) | 50 |
| LLMs, agents, RAG, eval (C) | 50 |
| Cloud native, containers (D) | 50 |
| Observability (E) | 28 |
| Data engineering, databases (F) | 31 |
| Security, identity, compliance (G) | 37 |
| OS, embedded, firmware, EDA (H) | 46 |
| Web, backend, frontend (I) | 25 |
| Dev tools, CI/CD, editors (J) | 30 |
| Desktop, graphics, robotics (K) | 33 |
| **Total** | **430+** |
