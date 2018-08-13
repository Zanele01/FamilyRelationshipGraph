import unittest
from Colormap import Colormap
from graphdraw import Graph_draw
from Edge_Length import Edge_Length

class TestGraphDraw(unittest.TestCase):
    def test_NotEmptyEdges(self):
        graph = Graph_draw()
        graph.create_edgelist('test_edges.txt')
        self.assertTrue(graph.get_edges())

    def test_NotEmptyWeights(self):
        graph = Graph_draw()
        graph.create_edgelist('test_edges.txt')
        self.assertTrue(graph.get_weights())

    def test_CorrectEdges(self):
        edges = [(0,1), (1,2), (2,3), (3,1), (4,0)]
        graph = Graph_draw()
        graph.create_edgelist('test_edges.txt')
        self.assertCountEqual(edges, graph.get_edges())

    def test_CorrectWeights(self):
        weights = [0.2, 0.96, 0.75, 0.24, 0.56]
        graph = Graph_draw()
        graph.create_edgelist('test_edges.txt')
        self.assertCountEqual(weights, graph.get_weights())

class TestColorMap(unittest.TestCase):

    def test_NotEmptyNodes(self):
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertTrue(color.get_nodes())

    def test_NotEmptyFeatures(self):
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertTrue(color.get_features())

    def test_correctnodes(self):
        nodes = [0,1,2,3,4]
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertCountEqual(nodes, color.get_nodes())

    def test_correctfeatures(self):
        features = [0,1,2,3,4]
        color = Colormap()
        color.create_nodes('test_nodes.txt')
        self.assertCountEqual(features,color.get_features())

if __name__ == '__main__':
    unittest.main()