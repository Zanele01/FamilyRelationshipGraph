import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys
import operator as op
import copy


from Filtering import Filtering

class Graph_draw:

	def __init__(self):
		self.edges = []
		self.weights = []
		self.filter = []
		
	def create_edgelist(self, filename):
		data = open(filename, 'r')
		lines = data.readlines()
		for line in lines:
			u,v,w = map(float, line.strip().split(' '))   
			self.edges.append((int(u),int(v)))    
			self.weights.append(w)	
		data.close()
		
	def get_weights(self):
		return self.weights
		
	def get_edges(self):
		return self.edges
		
	def add_edges(self, graph, length):
		edge_size = len(self.edges)
		for i in range(0, edge_size):
			graph.add_edge(self.edges[i][0], self.edges[i][1], weight = self.weights[i], length = length[i]) #add edges to graph
			
	def search_node_attributes(self,graph):
		Filter = Filtering()
		Filter.select_node_data()
		length = len(graph.nodes())
		for i in range(0,length):
			if graph.nodes[i]['feature'] > Filter.get_node_data():
				self.filter.append(graph.nodes[i]['feature'])
				filter_graph = graph.subgraph(self.filter)
					
	def draw_graph(self, graph, map):
		
		nx.draw(graph, pos = None, node_size = 150, with_labels = True, node_color = map['features'].cat.codes, cmap = plt.cm.get_cmap("Set1"), edge_color = 'gray')
		plt.axis('off')
		plt.savefig("graph.pdf")
		plt.show()
		
	
		
		
	
		
		
	
		
		
	
		