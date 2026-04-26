# Ontology — open* Knowledge Graph

## Design principle

> The graph IS the live ontology. OWL export is inspection-only.

The same principle used in the CFP conference pipeline applies here:
- **Apache AGE (Cypher)** = primary store, always queryable, always current
- **owlready2 + rdflib** = export layer → `.owl` for Protégé inspection only
- **`seed_concepts.json`** = hand-authored taxonomy, committed before any automation runs
- **`relationships.json`** = hand-authored known edges between specific projects

This means you can ask real questions in Cypher:

```cypher
-- What projects sit at both the AI and Firmware stack layers?
MATCH (p:Project)-[:RUNS_ON]->(l:StackLayer)
WHERE l.name IN ['AI', 'Firmware']
WITH p, collect(l.name) AS layers
WHERE size(layers) = 2
RETURN p.name, layers

-- What does OpenTelemetry connect to in the practical demo chain?
MATCH (p:Project {name: 'OpenTelemetry'})-[r]-(q:Project)
RETURN p.name, type(r), q.name

-- Which projects supersede or merge others?
MATCH (a:Project)-[:SUPERSEDES|MERGES_INTO]->(b:Project)
RETURN a.name, b.name
```

---

## Files in this directory

| File | Purpose |
|------|---------|
| `schema.cypher` | Apache AGE DDL — node labels, edge types, constraints |
| `seed_concepts.json` | Hand-authored taxonomy: StackLayers, Categories, Skills, Foundations |
| `relationships.json` | Known edges between specific open* projects |
| `bootstrap.cypher` | Cypher to load seed_concepts.json into a live AGE graph |
| `export.py` | owlready2 → `.owl` export (inspection only, not the primary store) |

---

## Node labels

| Label | Description | Key Properties |
|-------|-------------|----------------|
| `Project` | An open* project | `name`, `url`, `license`, `language`, `difficulty`, `status`, `is_oss` |
| `Category` | Grouping (e.g. "Silicon & EDA") | `name`, `slug` |
| `StackLayer` | Position in the open systems stack | `name`, `order` (1=lowest) |
| `Foundation` | Governing body | `name`, `url` |
| `Language` | Primary implementation language | `name` |
| `License` | SPDX license identifier | `spdx_id`, `is_osi` |
| `Skill` | What contributing teaches | `name`, `domain` |
| `Tier` | Strategic/Practical/Watchlist | `name`, `priority` |
| `Spec` | A standard this project implements | `name`, `body` |
| `RawTag` | Free-form tag before normalization | `value` |
| `Concept` | Normalized ontology concept (from RawTag) | `name`, `parent` |

---

## Edge types

| Edge | From → To | Meaning |
|------|-----------|---------|
| `BELONGS_TO` | Project → Category | project lives in this category |
| `RUNS_ON` | Project → StackLayer | project operates at this layer |
| `GOVERNED_BY` | Project → Foundation | foundation owns/stewards the project |
| `WRITTEN_IN` | Project → Language | primary implementation language |
| `LICENSED_AS` | Project → License | project's OSS license |
| `TEACHES` | Project → Skill | contributing builds this skill |
| `IN_TIER` | Project → Tier | strategic placement |
| `DEPENDS_ON` | Project → Project | runtime or build dependency |
| `COMPLEMENTS` | Project ↔ Project | bidirectional — work well together |
| `SUPERSEDES` | Project → Project | replaces or forks from |
| `MERGES_INTO` | Project → Project | project folded into another |
| `IMPLEMENTS_SPEC` | Project → Spec | project implements this standard |
| `PART_OF` | Project → Project | sub-project or component of a larger one |
| `NORMALIZES_TO` | RawTag → Concept | free-form tag resolved to ontology concept |

---

## Stack layer order

```
8  Data Governance    (OpenLineage, OpenMetadata)
7  AI / ML           (ONNX, OpenVINO, OpenCV, OpenXLA)
6  Policy & Security  (OPA, OpenSSF, OpenSCAP, OpenSSL)
5  Observability      (OpenTelemetry, OpenMetrics, OpenSearch)
4  Containers & Cloud (OCI, Kata, OpenStack, OpenShift)
3  OS & Networking    (OpenWrt, OpenBSD, Open vSwitch)
2  Firmware           (OpenBMC, OpenSBI, OpenTitan)
1  Silicon / EDA      (OpenROAD, OpenLane, OpenFPGA, OpenRAM)
```

The demo chain runs bottom-up through layers 1–8:
```
[1] OpenTitan (RoT) → [2] OpenBMC (BMC fw) → [4] OpenStack (cloud)
→ [4] OCI/Kata (containers) → [5] OpenTelemetry (traces)
→ [5] OpenSearch (logs) → [6] OPA (policy) → [6] OpenSCAP (compliance)
→ [7] ONNX → OpenVINO (AI inference) → [8] OpenLineage (data lineage)
```

---

## Ontology lifecycle

```
Hand-author seed_concepts.json
        ↓
bootstrap.cypher → load into AGE graph
        ↓
Scrape / classify open* projects → add Project nodes
        ↓
discover.py → GitHub API → normalize RawTags → NORMALIZES_TO Concept edges
        ↓
export.py → owlready2 → open_star.owl (Protégé inspection)
```

This mirrors the CFP pipeline:
`seed_concepts.json → AGE → LLM classification → RawTag → Concept → OWL export`

---

## OWL export design (inspection only)

Classes map to node labels. Object properties map to edge types.

| OWL Class | AGE Label |
|-----------|-----------|
| `OpenProject` | `Project` |
| `StackLayer` | `StackLayer` |
| `TechnicalSkill` | `Skill` |
| `OpenFoundation` | `Foundation` |
| `OntologyConcept` | `Concept` |

Object properties: `runsOn`, `governedBy`, `dependsOn`, `complements`, `supersedes`,
`mergesInto`, `implementsSpec`, `teaches`, `belongsTo`.

The OWL file is never edited directly. It is regenerated by `export.py` from the AGE graph on demand.
