import matplotlib.pyplot as plt
import networkx as nx

from Filtering import Filtering

class Graph_draw:

	def __init__(self):
		self.edges = []
		self.weights = []
		self.filter = []
		
	def create_edgelist(self, filename):
		data = open('data.txt', 'r').readlines()
		for line in data:
			u,v,w = map(float, line.strip().split(' '))   
			self.edges.append((int(u),int(v)))    
			self.weights.append(w)
			
	def get_weights(self):
		return self.weights
		
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
		for j in self.filter:
			print(j)
					
	def draw_graph(self, graph, map):
		self.search_node_attributes(graph)
		nx.draw(graph, pos = None, node_size = 150, with_labels = True, node_color = map['features'].cat.codes, cmap = plt.cm.get_cmap("Set1"), edge_color = 'gray')
		plt.axis('off')
		plt.show()
		
	
		
		
	
		