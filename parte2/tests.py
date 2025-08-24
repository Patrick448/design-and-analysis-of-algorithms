import unittest
import os
import pydot
from graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph1_file = "tests/graph1.txt"
        self.graph2_file = "tests/graph2.txt"

    def test_graph_creation_from_file_undirected(self):
        g = Graph(file_path=self.graph1_file)
        self.assertFalse(g.directed)
        self.assertEqual(len(g.nodes), 6)
        self.assertEqual(len(g.edges), 6)

    def test_graph_creation_from_file_directed(self):
        g = Graph(file_path=self.graph2_file)
        self.assertTrue(g.directed)
        self.assertEqual(len(g.nodes), 6)
        self.assertEqual(len(g.edges), 6)

    def test_adjacency_list_undirected(self):
        g = Graph(file_path=self.graph1_file)
        adjacency_list = g.get_adjacency_list()
        self.assertIn("x1", adjacency_list)
        self.assertCountEqual(adjacency_list["x1"], ["x2", "x3"])

    def test_adjacency_list_directed(self):
        g = Graph(file_path=self.graph2_file)
        adjacency_list = g.get_adjacency_list()
        # Directed graph adds both directions (due to implementation)
        self.assertIn("x2", adjacency_list)
        self.assertIn("x4", adjacency_list["x2"])

    def test_dfs_traversal(self):
        g = Graph(file_path=self.graph1_file)
        dfs_result = g.dfs_compute_tdc("x1")
        self.assertIn("x1", dfs_result)
        self.assertIn("x2", dfs_result)
        self.assertIn("x3", dfs_result)

    def test_connectivity_undirected(self):
        g = Graph(file_path=self.graph1_file)
        self.assertFalse(g.check_connected())  # Two separate components

    def test_connectivity_directed(self):
        g = Graph(file_path=self.graph2_file)
        self.assertTrue(g.check_connected())  # Strongly connected due to x2->x4 edge

    def test_pydot_export(self):
        g = Graph(file_path=self.graph1_file)
        dot_graph = g.to_pydot()
        self.assertIsInstance(dot_graph, pydot.Dot)
        self.assertEqual(len(dot_graph.get_nodes()), len(g.nodes))
        self.assertEqual(len(dot_graph.get_edges()), len(g.edges))


if __name__ == "__main__":
    unittest.main()
