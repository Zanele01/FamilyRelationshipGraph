import unittest
import networkx as nx
from ColourMap import ColourMap
from GraphDraw import GraphDraw
from EdgeLength import EdgeLength
from Filtering import Filtering

class TestEdgeLength(unittest.TestCase):
	def test_CalculateEdgeLength(self):
		edge = EdgeLength()
		edge_list = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
		weight = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
		edge.convert_edge_weights_to_length(weight)
		self.assertListEqual(edge_list, edge.get_length())
		
class TestGraphDraw(unittest.TestCase):
	def test_NotEmptyEdges(self):
		graph = GraphDraw()
		graph.create_edgelist('test_edges.txt')
		self.assertTrue(graph.get_edges())
		
	def test_NotEmptyWeights(self):
		graph = GraphDraw()
		graph.create_edgelist('test_edges.txt')
		self.assertTrue(graph.get_weights())
		
	def test_CorrectEdges(self):
		edges = [(0,1), (1,2), (2,3), (3,1), (4,0)]
		graph = GraphDraw()
		graph.create_edgelist('test_edges.txt')
		self.assertCountEqual(edges, graph.get_edges())
		
	def test_CorrectWeights(self):
		weights = [0.2, 0.96, 0.75, 0.24, 0.56]
		graph = GraphDraw()
		graph.create_edgelist('test_edges.txt')
		self.assertCountEqual(weights, graph.get_weights())
		
class TestColuorMap(unittest.TestCase):
	def test_NotEmptyNodes(self):
		colour = ColourMap()
		colour.create_nodes('test_nodes.txt')
		self.assertTrue(colour.get_nodes())
		
	def test_NotEmptyFeatures(self):
		colour = ColourMap()
		colour.create_nodes('test_nodes.txt')
		self.assertTrue(colour.get_features())
		
	def test_correctnodes(self):
		nodes = [0,1,2,3,4]
		colour = ColourMap()
		colour.create_nodes('test_nodes.txt')
		self.assertCountEqual(nodes, colour.get_nodes())
		
	def test_correctfeatures(self):
		features = [0,1,2,3,4]
		colour = ColourMap()
		colour.create_nodes('test_nodes.txt')
		self.assertCountEqual(features,colour.get_features())

class TestFiltering(unittest.TestCase):			
	def test_FiltersNoNodes(self):
		nodes = []
		graph = nx.Graph()
		
		colour = ColourMap()
		colour.create_nodes('test_nodes.txt')
		colour.add_nodes(graph)
		
		filter = Filtering()
		filter.filter_nodes(graph,-1) #filter age < -1
		self.assertCountEqual(nodes, filter.get_filtered_nodes())
		
	def test_FiltersAllWeights(self):
		weights = [0.2, 0.96, 0.75, 0.24, 0.56]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		graph = nx.Graph()
		
		G = GraphDraw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,1) #filter weight < 1
		self.assertCountEqual(weights, filter.get_filtered_weights())
		
	def test_FiltersSelectedWeights(self):
		weights = [0.2, 0.24]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		graph = nx.Graph()
		
		G = GraphDraw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,0.5) #filter weight < 0.5
		self.assertCountEqual(weights, filter.get_filtered_weights())
		
	def test_FiltersNoWeights(self):
		weights = []
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		graph = nx.Graph()
		
		G = GraphDraw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,-1) #filter weight < -1
		self.assertCountEqual(weights, filter.get_filtered_weights())
		
	def test_WeightsNotRemovedFromFilteredList(self):
		weights = [0.2, 0.96, 0.75, 0.24, 0.56]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		
		graph = nx.Graph()
		
		G = GraphDraw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,0.1) #filter weight < 0.1
		
		filter.remove_weights(graph)
		
		self.assertCountEqual(weights,G.get_weights())
		


if __name__ == '__main__':
    unittest.main()