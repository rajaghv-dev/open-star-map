-- bootstrap.cypher
-- One-time setup: loads seed_concepts.json and relationships.json into a live Apache AGE graph.
--
-- Prerequisites:
--   psql -U postgres -d your_db -c "LOAD 'age';"
--   psql -U postgres -d your_db -c "SET search_path = ag_catalog, '\$user', public;"
--   psql -U postgres -d your_db -c "SELECT create_graph('open_star_graph');"
--
-- Then run this file:
--   psql -U postgres -d your_db -f ontology/bootstrap.cypher
--
-- After bootstrap, use schema.cypher for further population and query examples.

LOAD 'age';
SET search_path = ag_catalog, "$user", public;

-- Idempotent: MERGE never duplicates nodes

-- Stack layers
SELECT * FROM cypher('open_star_graph', $$
  MERGE (:StackLayer {name: 'Silicon & EDA',     slug: 'silicon',       order: 1})
  MERGE (:StackLayer {name: 'Firmware',          slug: 'firmware',      order: 2})
  MERGE (:StackLayer {name: 'OS & Networking',   slug: 'os-net',        order: 3})
  MERGE (:StackLayer {name: 'Cloud & IaaS',      slug: 'cloud',         order: 4})
  MERGE (:StackLayer {name: 'Observability',     slug: 'observability', order: 5})
  MERGE (:StackLayer {name: 'Policy & Security', slug: 'security',      order: 6})
  MERGE (:StackLayer {name: 'AI & Inference',    slug: 'ai',            order: 7})
  MERGE (:StackLayer {name: 'Data Governance',   slug: 'data-gov',      order: 8})
$$) AS (r agtype);

-- Tiers
SELECT * FROM cypher('open_star_graph', $$
  MERGE (:Tier {name: 'Strategic', priority: 1})
  MERGE (:Tier {name: 'Practical', priority: 2})
  MERGE (:Tier {name: 'Watchlist', priority: 3})
  MERGE (:Tier {name: 'NotOSS',   priority: 99})
$$) AS (r agtype);

-- Seed concepts (hierarchy loaded from seed_concepts.json via Python bootstrap script)
-- Direct SQL insert for root concepts:
SELECT * FROM cypher('open_star_graph', $$
  MERGE (:Concept {name: 'root-of-trust',         parent: null})
  MERGE (:Concept {name: 'secure-boot',           parent: 'root-of-trust'})
  MERGE (:Concept {name: 'attestation',           parent: 'root-of-trust'})
  MERGE (:Concept {name: 'bmc',                   parent: null})
  MERGE (:Concept {name: 'redfish',               parent: 'bmc'})
  MERGE (:Concept {name: 'ipmi',                  parent: 'bmc'})
  MERGE (:Concept {name: 'eda-flow',              parent: null})
  MERGE (:Concept {name: 'place-and-route',       parent: 'eda-flow'})
  MERGE (:Concept {name: 'synthesis',             parent: 'eda-flow'})
  MERGE (:Concept {name: 'observability',         parent: null})
  MERGE (:Concept {name: 'traces',                parent: 'observability'})
  MERGE (:Concept {name: 'metrics',               parent: 'observability'})
  MERGE (:Concept {name: 'logs',                  parent: 'observability'})
  MERGE (:Concept {name: 'policy-as-code',        parent: null})
  MERGE (:Concept {name: 'rego',                  parent: 'policy-as-code'})
  MERGE (:Concept {name: 'fine-grained-authz',    parent: 'policy-as-code'})
  MERGE (:Concept {name: 'supply-chain-security', parent: null})
  MERGE (:Concept {name: 'sbom',                  parent: 'supply-chain-security'})
  MERGE (:Concept {name: 'slsa',                  parent: 'supply-chain-security'})
  MERGE (:Concept {name: 'compliance-scanning',   parent: 'supply-chain-security'})
  MERGE (:Concept {name: 'inference',             parent: null})
  MERGE (:Concept {name: 'model-format',          parent: 'inference'})
  MERGE (:Concept {name: 'graph-optimization',    parent: 'inference'})
  MERGE (:Concept {name: 'data-lineage',          parent: null})
  MERGE (:Concept {name: 'data-catalog',          parent: null})
  MERGE (:Concept {name: 'iac',                   parent: null})
  MERGE (:Concept {name: 'container-runtime',     parent: null})
  MERGE (:Concept {name: 'service-mesh',          parent: null})
  MERGE (:Concept {name: 'edge-cloud',            parent: null})
  MERGE (:Concept {name: 'open-isa',              parent: null})
$$) AS (r agtype);

-- Parent→child Concept edges
SELECT * FROM cypher('open_star_graph', $$
  MATCH (parent:Concept), (child:Concept)
  WHERE child.parent IS NOT NULL AND child.parent = parent.name
  CREATE (child)-[:CHILD_OF]->(parent)
$$) AS (r agtype);
