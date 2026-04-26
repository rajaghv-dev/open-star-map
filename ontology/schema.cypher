-- Apache AGE schema for the open* knowledge graph
-- Graph name: open_star_graph
-- Load after: SELECT create_graph('open_star_graph');

-- ============================================================
-- NODE CONSTRAINTS (run once on fresh graph)
-- ============================================================

-- Project nodes — uniqueness on name
SELECT * FROM cypher('open_star_graph', $$
  CREATE CONSTRAINT ON (p:Project) ASSERT p.name IS UNIQUE
$$) AS (result agtype);

-- Concept nodes — uniqueness on name
SELECT * FROM cypher('open_star_graph', $$
  CREATE CONSTRAINT ON (c:Concept) ASSERT c.name IS UNIQUE
$$) AS (result agtype);

-- StackLayer nodes
SELECT * FROM cypher('open_star_graph', $$
  CREATE CONSTRAINT ON (l:StackLayer) ASSERT l.name IS UNIQUE
$$) AS (result agtype);


-- ============================================================
-- SEED STACK LAYERS (order = position in stack, 1=lowest)
-- ============================================================

SELECT * FROM cypher('open_star_graph', $$
  MERGE (:StackLayer {name: 'Silicon & EDA',     slug: 'silicon',      order: 1})
  MERGE (:StackLayer {name: 'Firmware',          slug: 'firmware',     order: 2})
  MERGE (:StackLayer {name: 'OS & Networking',   slug: 'os-net',       order: 3})
  MERGE (:StackLayer {name: 'Cloud & IaaS',      slug: 'cloud',        order: 4})
  MERGE (:StackLayer {name: 'Observability',     slug: 'observability',order: 5})
  MERGE (:StackLayer {name: 'Policy & Security', slug: 'security',     order: 6})
  MERGE (:StackLayer {name: 'AI & Inference',    slug: 'ai',           order: 7})
  MERGE (:StackLayer {name: 'Data Governance',   slug: 'data-gov',     order: 8})
$$) AS (result agtype);


-- ============================================================
-- SEED TIERS
-- ============================================================

SELECT * FROM cypher('open_star_graph', $$
  MERGE (:Tier {name: 'Strategic',  priority: 1})
  MERGE (:Tier {name: 'Practical',  priority: 2})
  MERGE (:Tier {name: 'Watchlist',  priority: 3})
  MERGE (:Tier {name: 'NotOSS',     priority: 99})
$$) AS (result agtype);


-- ============================================================
-- SAMPLE PROJECT NODES (extend via bootstrap.cypher from seed_concepts.json)
-- ============================================================

SELECT * FROM cypher('open_star_graph', $$
  MERGE (:Project {name: 'OpenTelemetry', url: 'https://github.com/open-telemetry', license: 'Apache-2.0', language: 'Go', difficulty: 'beginner',      status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenBMC',       url: 'https://github.com/openbmc/openbmc', license: 'Apache-2.0', language: 'C++', difficulty: 'advanced',    status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenTitan',     url: 'https://github.com/lowRISC/opentitan', license: 'Apache-2.0', language: 'SystemVerilog', difficulty: 'advanced', status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenROAD',      url: 'https://github.com/The-OpenROAD-Project/OpenROAD', license: 'BSD-3-Clause', language: 'C++', difficulty: 'advanced', status: 'active', is_oss: true})
  MERGE (:Project {name: 'ONNX',          url: 'https://github.com/onnx/onnx', license: 'Apache-2.0', language: 'Python', difficulty: 'intermediate',   status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenVINO',      url: 'https://github.com/openvinotoolkit/openvino', license: 'Apache-2.0', language: 'C++', difficulty: 'intermediate', status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenCV',        url: 'https://github.com/opencv/opencv', license: 'Apache-2.0', language: 'C++', difficulty: 'intermediate',   status: 'active', is_oss: true})
  MERGE (:Project {name: 'Open Policy Agent', url: 'https://github.com/open-policy-agent/opa', license: 'Apache-2.0', language: 'Go', difficulty: 'intermediate', status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenSearch',    url: 'https://github.com/opensearch-project/OpenSearch', license: 'Apache-2.0', language: 'Java', difficulty: 'intermediate', status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenTofu',      url: 'https://github.com/opentofu/opentofu', license: 'MPL-2.0', language: 'Go', difficulty: 'intermediate',   status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenStack',     url: 'https://opendev.org/openstack', license: 'Apache-2.0', language: 'Python', difficulty: 'intermediate',   status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenLineage',   url: 'https://github.com/OpenLineage/OpenLineage', license: 'Apache-2.0', language: 'Python', difficulty: 'intermediate', status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenSSF Scorecard', url: 'https://github.com/ossf/scorecard', license: 'Apache-2.0', language: 'Go', difficulty: 'beginner',  status: 'active', is_oss: true})
  MERGE (:Project {name: 'OpenAI',        url: 'https://openai.com', license: 'Proprietary', language: '', difficulty: '', status: 'active', is_oss: false})
$$) AS (result agtype);


-- ============================================================
-- STACK LAYER EDGES
-- ============================================================

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenTitan'}),     (l:StackLayer {slug: 'silicon'})      CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenBMC'}),       (l:StackLayer {slug: 'firmware'})     CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenROAD'}),      (l:StackLayer {slug: 'silicon'})      CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenStack'}),     (l:StackLayer {slug: 'cloud'})        CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenTelemetry'}), (l:StackLayer {slug: 'observability'})CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'Open Policy Agent'}),(l:StackLayer {slug: 'security'})  CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'ONNX'}),          (l:StackLayer {slug: 'ai'})           CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenVINO'}),      (l:StackLayer {slug: 'ai'})           CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenCV'}),        (l:StackLayer {slug: 'ai'})           CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenSearch'}),    (l:StackLayer {slug: 'observability'})CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenLineage'}),   (l:StackLayer {slug: 'data-gov'})     CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (p:Project {name: 'OpenSSF Scorecard'}),(l:StackLayer {slug: 'security'})  CREATE (p)-[:RUNS_ON]->(l)
$$) AS (result agtype);


-- ============================================================
-- INTER-PROJECT RELATIONSHIPS
-- ============================================================

-- OpenVINO DEPENDS_ON ONNX (accepts ONNX models)
SELECT * FROM cypher('open_star_graph', $$
  MATCH (a:Project {name: 'OpenVINO'}), (b:Project {name: 'ONNX'})
  CREATE (a)-[:DEPENDS_ON {note: 'accepts ONNX model format as input'}]->(b)
$$) AS (result agtype);

-- OpenTelemetry COMPLEMENTS OpenSearch (traces/logs ship to OpenSearch)
SELECT * FROM cypher('open_star_graph', $$
  MATCH (a:Project {name: 'OpenTelemetry'}), (b:Project {name: 'OpenSearch'})
  CREATE (a)-[:COMPLEMENTS {note: 'OTLP exporter ships traces+logs to OpenSearch'}]->(b)
$$) AS (result agtype);

-- OpenSearch COMPLEMENTS Open Policy Agent (search index used as policy data source)
SELECT * FROM cypher('open_star_graph', $$
  MATCH (a:Project {name: 'OpenSearch'}), (b:Project {name: 'Open Policy Agent'})
  CREATE (a)-[:COMPLEMENTS {note: 'search index used as external data in OPA bundle'}]->(b)
$$) AS (result agtype);

-- OpenLineage COMPLEMENTS OpenSearch (lineage events indexed for search)
SELECT * FROM cypher('open_star_graph', $$
  MATCH (a:Project {name: 'OpenLineage'}), (b:Project {name: 'OpenSearch'})
  CREATE (a)-[:COMPLEMENTS {note: 'lineage events indexed in OpenSearch for discovery'}]->(b)
$$) AS (result agtype);

-- OpenTitan PART_OF OpenBMC ecosystem (RoT integrates with BMC trust chain)
SELECT * FROM cypher('open_star_graph', $$
  MATCH (a:Project {name: 'OpenTitan'}), (b:Project {name: 'OpenBMC'})
  CREATE (a)-[:COMPLEMENTS {note: 'OpenTitan RoT integrated into OpenBMC secure boot chain'}]->(b)
$$) AS (result agtype);

-- OpenStack DEPENDS_ON OpenTelemetry (instrumented via OTLP)
SELECT * FROM cypher('open_star_graph', $$
  MATCH (a:Project {name: 'OpenStack'}), (b:Project {name: 'OpenTelemetry'})
  CREATE (a)-[:DEPENDS_ON {note: 'OpenStack emits OTLP traces from Nova, Neutron, etc.'}]->(b)
$$) AS (result agtype);

-- OpenTofu SUPERSEDES (Terraform fork — not an open* project but the relationship matters)
-- Note: archived / non-OSS projects have is_oss: false and are not loaded here

-- OpenTracing MERGES_INTO OpenTelemetry (historical)
SELECT * FROM cypher('open_star_graph', $$
  MERGE (a:Project {name: 'OpenTracing', status: 'archived', is_oss: true, url: 'https://opentracing.io'})
  WITH a
  MATCH (b:Project {name: 'OpenTelemetry'})
  CREATE (a)-[:MERGES_INTO {year: 2019, note: 'OpenTracing merged into OpenTelemetry project'}]->(b)
$$) AS (result agtype);

-- OpenCensus MERGES_INTO OpenTelemetry (historical)
SELECT * FROM cypher('open_star_graph', $$
  MERGE (a:Project {name: 'OpenCensus', status: 'archived', is_oss: true, url: 'https://opencensus.io'})
  WITH a
  MATCH (b:Project {name: 'OpenTelemetry'})
  CREATE (a)-[:MERGES_INTO {year: 2019, note: 'OpenCensus merged into OpenTelemetry project'}]->(b)
$$) AS (result agtype);


-- ============================================================
-- TIER EDGES
-- ============================================================

SELECT * FROM cypher('open_star_graph', $$
  MATCH (t:Tier {name: 'Strategic'})
  MATCH (p:Project) WHERE p.name IN [
    'OpenStack','OpenBMC','OpenTitan','OpenROAD','OpenTelemetry',
    'Open Policy Agent','OpenSearch','ONNX','OpenVINO','OpenCV','OpenSSF Scorecard'
  ]
  CREATE (p)-[:IN_TIER]->(t)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (t:Tier {name: 'Practical'})
  MATCH (p:Project) WHERE p.name IN [
    'OpenTelemetry','OpenSearch','Open Policy Agent','ONNX','OpenVINO','OpenCV','OpenSSF Scorecard'
  ]
  CREATE (p)-[:IN_TIER]->(t)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (t:Tier {name: 'Watchlist'})
  MATCH (p:Project) WHERE p.name IN [
    'OpenTitan','OpenROAD','OpenLineage','OpenTofu'
  ]
  CREATE (p)-[:IN_TIER]->(t)
$$) AS (result agtype);

SELECT * FROM cypher('open_star_graph', $$
  MATCH (t:Tier {name: 'NotOSS'})
  MATCH (p:Project {is_oss: false})
  CREATE (p)-[:IN_TIER]->(t)
$$) AS (result agtype);


-- ============================================================
-- USEFUL QUERY EXAMPLES
-- ============================================================

-- Full demo chain (ordered by stack layer):
-- SELECT * FROM cypher('open_star_graph', $$
--   MATCH (p:Project)-[:RUNS_ON]->(l:StackLayer)
--   MATCH (p)-[:IN_TIER]->(t:Tier {name: 'Practical'})
--   RETURN p.name, l.name, l.order
--   ORDER BY l.order
-- $$) AS (project agtype, layer agtype, order agtype);

-- Projects that complement each other:
-- SELECT * FROM cypher('open_star_graph', $$
--   MATCH (a:Project)-[r:COMPLEMENTS]-(b:Project)
--   RETURN a.name, b.name, r.note
-- $$) AS (a agtype, b agtype, note agtype);

-- Beginner-friendly projects by stack layer:
-- SELECT * FROM cypher('open_star_graph', $$
--   MATCH (p:Project {difficulty: 'beginner'})-[:RUNS_ON]->(l:StackLayer)
--   RETURN p.name, l.name
--   ORDER BY l.order
-- $$) AS (project agtype, layer agtype);
