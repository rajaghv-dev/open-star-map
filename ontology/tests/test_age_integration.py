"""
AGE integration test — creates a temporary graph, inserts dummy nodes and
edges, asserts queries return the expected results, then drops the graph.

Skipped automatically unless:
  - psycopg (v3) is installed
  - OPEN_STAR_AGE_DSN env var is set, e.g.
      postgresql://postgres:postgres@localhost:5455/postgres

Cleanup is in tearDown, so the test graph is removed even on failure.

Run:  python3 -m unittest ontology.tests.test_age_integration -v
"""
import os
import unittest
import uuid

try:
    import psycopg
    HAS_PSYCOPG = True
except ImportError:
    HAS_PSYCOPG = False

DSN = os.environ.get("OPEN_STAR_AGE_DSN")


@unittest.skipUnless(
    HAS_PSYCOPG and DSN,
    "AGE integration test requires psycopg and OPEN_STAR_AGE_DSN",
)
class TestAGEIntegration(unittest.TestCase):
    """Each test runs against an ephemeral graph for full isolation."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = f"open_star_test_{uuid.uuid4().hex[:12]}"
        cls.conn = psycopg.connect(DSN, autocommit=True)
        cls.conn.execute("LOAD 'age';")
        cls.conn.execute('SET search_path = ag_catalog, "$user", public;')
        cls.conn.execute(f"SELECT create_graph('{cls.graph}');")
        cls._seed()

    @classmethod
    def tearDownClass(cls) -> None:
        try:
            cls.conn.execute(f"SELECT drop_graph('{cls.graph}', true);")
        finally:
            cls.conn.close()

    @classmethod
    def cypher(cls, query: str, columns: str = "r agtype") -> list:
        sql = (
            f"SELECT * FROM cypher('{cls.graph}', $$ {query} $$) "
            f"AS ({columns});"
        )
        return cls.conn.execute(sql).fetchall()

    @classmethod
    def _seed(cls) -> None:
        # Stack layers
        cls.cypher("""
            MERGE (:StackLayer {name: 'Silicon & EDA',  slug: 'silicon',       order: 1})
            MERGE (:StackLayer {name: 'Firmware',       slug: 'firmware',      order: 2})
            MERGE (:StackLayer {name: 'Observability',  slug: 'observability', order: 5})
            MERGE (:StackLayer {name: 'AI & Inference', slug: 'ai',            order: 7})
        """)
        # Tiers
        cls.cypher("""
            MERGE (:Tier {name: 'Strategic', priority: 1})
            MERGE (:Tier {name: 'Practical', priority: 2})
        """)
        # Dummy projects (recognisable test- prefix so a stray leak is obvious)
        cls.cypher("""
            MERGE (:Project {name: 'test-OpenTitan',     license: 'Apache-2.0', is_oss: true})
            MERGE (:Project {name: 'test-OpenBMC',       license: 'Apache-2.0', is_oss: true})
            MERGE (:Project {name: 'test-OpenTelemetry', license: 'Apache-2.0', is_oss: true})
            MERGE (:Project {name: 'test-ONNX',          license: 'Apache-2.0', is_oss: true})
            MERGE (:Project {name: 'test-OpenVINO',      license: 'Apache-2.0', is_oss: true})
        """)
        # RUNS_ON edges
        cls.cypher("""
            MATCH (p:Project {name:'test-OpenTitan'}),     (l:StackLayer {slug:'silicon'})
            CREATE (p)-[:RUNS_ON]->(l)
        """)
        cls.cypher("""
            MATCH (p:Project {name:'test-OpenBMC'}),       (l:StackLayer {slug:'firmware'})
            CREATE (p)-[:RUNS_ON]->(l)
        """)
        cls.cypher("""
            MATCH (p:Project {name:'test-OpenTelemetry'}), (l:StackLayer {slug:'observability'})
            CREATE (p)-[:RUNS_ON]->(l)
        """)
        cls.cypher("""
            MATCH (p:Project {name:'test-ONNX'}),          (l:StackLayer {slug:'ai'})
            CREATE (p)-[:RUNS_ON]->(l)
        """)
        cls.cypher("""
            MATCH (p:Project {name:'test-OpenVINO'}),      (l:StackLayer {slug:'ai'})
            CREATE (p)-[:RUNS_ON]->(l)
        """)
        # Inter-project relationships
        cls.cypher("""
            MATCH (a:Project {name:'test-OpenVINO'}), (b:Project {name:'test-ONNX'})
            CREATE (a)-[:DEPENDS_ON]->(b)
        """)
        cls.cypher("""
            MATCH (a:Project {name:'test-OpenTitan'}), (b:Project {name:'test-OpenBMC'})
            CREATE (a)-[:COMPLEMENTS]->(b)
        """)
        # Tier membership
        cls.cypher("""
            MATCH (t:Tier {name:'Strategic'}), (p:Project)
            WHERE p.name IN ['test-OpenTitan','test-OpenBMC','test-OpenTelemetry','test-ONNX','test-OpenVINO']
            CREATE (p)-[:IN_TIER]->(t)
        """)

    # ---------- assertions ----------

    def test_project_count(self) -> None:
        rows = self.cypher("MATCH (p:Project) RETURN count(p)", "c agtype")
        self.assertEqual(int(str(rows[0][0])), 5)

    def test_stack_layer_count(self) -> None:
        rows = self.cypher("MATCH (l:StackLayer) RETURN count(l)", "c agtype")
        self.assertEqual(int(str(rows[0][0])), 4)

    def test_runs_on_for_otel(self) -> None:
        rows = self.cypher("""
            MATCH (p:Project {name:'test-OpenTelemetry'})-[:RUNS_ON]->(l:StackLayer)
            RETURN l.slug
        """, "slug agtype")
        self.assertEqual(len(rows), 1)
        self.assertIn("observability", str(rows[0][0]))

    def test_depends_on_traversal(self) -> None:
        rows = self.cypher("""
            MATCH (a:Project)-[:DEPENDS_ON]->(b:Project)
            RETURN a.name, b.name
        """, "a agtype, b agtype")
        self.assertEqual(len(rows), 1)
        self.assertIn("test-OpenVINO", str(rows[0][0]))
        self.assertIn("test-ONNX", str(rows[0][1]))

    def test_strategic_tier_membership(self) -> None:
        rows = self.cypher("""
            MATCH (p:Project)-[:IN_TIER]->(t:Tier {name:'Strategic'})
            RETURN count(p)
        """, "c agtype")
        self.assertEqual(int(str(rows[0][0])), 5)

    def test_demo_chain_ordering(self) -> None:
        rows = self.cypher("""
            MATCH (p:Project)-[:RUNS_ON]->(l:StackLayer)
            RETURN l.order
            ORDER BY l.order
        """, "ord agtype")
        orders = [int(str(r[0])) for r in rows]
        self.assertEqual(orders, sorted(orders))
        self.assertEqual(orders[0], 1)   # silicon first
        self.assertEqual(orders[-1], 7)  # AI last

    def test_no_leakage_outside_test_graph(self) -> None:
        """Sanity: the test-prefixed projects must not appear in the real graph."""
        with psycopg.connect(DSN, autocommit=True) as conn:
            conn.execute("LOAD 'age';")
            conn.execute('SET search_path = ag_catalog, "$user", public;')
            row = conn.execute(
                "SELECT 1 FROM ag_catalog.ag_graph WHERE name = 'open_star_graph';"
            ).fetchone()
            if row is None:
                self.skipTest("real graph 'open_star_graph' does not exist on this DB")
            leaked = conn.execute(
                "SELECT * FROM cypher('open_star_graph', $$ "
                "MATCH (p:Project) WHERE p.name STARTS WITH 'test-' RETURN p.name "
                "$$) AS (n agtype);"
            ).fetchall()
            self.assertEqual(leaked, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
