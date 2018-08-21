import unittest
import networkx as nx
from Colormap import Colormap
from graphdraw import Graph_draw
from Edge_Length import Edge_Length
from Filtering import Filtering

class TestEdgeLength(unittest.TestCase):
	def test_CalculateEdgeLength(self):
		edge = Edge_Length()
		edge_list = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
		weight = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
		edge.convert_edge_weights_to_length(weight)
		self.assertListEqual(edge_list, edge.get_length())
		
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

class TestFiltering(unittest.TestCase):
	def test_FiltersAllNodes(self):
		nodes = [0,1,2,3,4]
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		filter = Filtering()
		filter.filter_nodes(graph,5) #filter age < 5
		self.assertCountEqual(nodes, filter.get_filtered_nodes())
		
	def test_FiltersSelectedNodes(self):
		nodes = [0,1]
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		filter = Filtering()
		filter.filter_nodes(graph,2) #filter age < 2
		self.assertCountEqual(nodes, filter.get_filtered_nodes())
		
	def test_FiltersNoNodes(self):
		nodes = []
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		filter = Filtering()
		filter.filter_nodes(graph,-1) #filter age < -1
		self.assertCountEqual(nodes, filter.get_filtered_nodes())
		
	def test_FiltersAllWeights(self):
		weights = [0.2, 0.96, 0.75, 0.24, 0.56]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		graph = nx.Graph()
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,1) #filter weight < 1
		self.assertCountEqual(weights, filter.get_filtered_weights())
		
	def test_FiltersSelectedWeights(self):
		weights = [0.2, 0.24]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		graph = nx.Graph()
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,0.5) #filter weight < 0.5
		self.assertCountEqual(weights, filter.get_filtered_weights())
		
	def test_FiltersNoWeights(self):
		weights = []
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		graph = nx.Graph()
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,-1) #filter weight < -1
		self.assertCountEqual(weights, filter.get_filtered_weights())
		
	def test_ItemFoundInFilteredNodes(self):
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		
		filter = Filtering()
		filter.filter_nodes(graph,5) #filter age < 5
		
		item = 4
		self.assertTrue(filter.search_filterednodes(item))
		
	def test_ItemNotFoundInFilteredNodes(self):
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		
		filter = Filtering()
		filter.filter_nodes(graph,23) #filter age < 23
		
		item = 59
		self.assertFalse(filter.search_filterednodes(item))
		
	def  test_ItemNotFoundInEmptyFilteredNodes(self):
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		
		filter = Filtering()
		filter.filter_nodes(graph,-1) #filter age < -1
		
		item = 1
		self.assertFalse(filter.search_filterednodes(item))
		
	def test_ItemFoundInFilteredWeights(self):
		graph = nx.Graph()
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,0.5) #filter weight < 0.5
		
		item = 0.2
		self.assertTrue(filter.search_filteredweights(item))
		
	def test_ItemNotFoundInFilteredWeights(self):
		graph = nx.Graph()
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,0.5) #filter weight < 0.5
		
		item = 0.56
		self.assertFalse(filter.search_filteredweights(item))
		
	def test_ItemNotFoundInEmptyFilteredWeights(self):
		graph = nx.Graph()
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,-1) #filter weight < -1
		
		item = 0.24
		self.assertFalse(filter.search_filteredweights(item))
			
	def test_EdgesNotRemovedFromFilteredList(self):
		nodes = [0,1,2,3,4]
		edges = [(0,1), (1,2), (2,3), (3,1), (4,0)]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_nodes(graph,5) #filter age < 5
		
		filter.remove_edges(graph)

		self.assertCountEqual(edges,G.get_edges())
		
	def test_NodesNotRemovedFromFilteredList(self):
		nodes = [0,1,2,3,4]
		
		graph = nx.Graph()
		
		color = Colormap()
		color.create_nodes('test_nodes.txt')
		color.add_nodes(graph)

		filter = Filtering()
		filter.filter_nodes(graph,5) #filter age < 5
		
		filter.remove_nodes(graph)

		self.assertCountEqual(nodes,color.get_nodes())
		
	def test_WeightsNotRemovedFromFilteredList(self):
		weights = [0.2, 0.96, 0.75, 0.24, 0.56]
		length = [0.3, 0.36, 0.55, 0.84, 0.46]
		
		graph = nx.Graph()
		
		G = Graph_draw()
		G.create_edgelist('test_edges.txt')
		G.add_edges(graph,length)
		
		filter = Filtering()
		filter.filter_weights(graph,0.1) #filter weight < 0.1
		
		filter.remove_weights(graph)
		
		self.assertCountEqual(weights,G.get_weights())
		


if __name__ == '__main__':
    unittest.main()