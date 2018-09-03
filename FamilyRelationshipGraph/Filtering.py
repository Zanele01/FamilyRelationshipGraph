import matplotlib.pyplot as plt
import networkx as nx

class Filtering:
	def __init__(self):
		self.filterednodes = []
		self.filteredweights = []
		
	def filter_nodes(self,graph,node_attribute):
		for node in graph.nodes(data='feature'):
			if node[1] < float(node_attribute): 
				self.filterednodes.append(node[0])
		self.remove_nodes(graph)
				
	def filter_weights(self,graph,weight_attribute):
		for edges in graph.edges(data='weight'):
			if edges[2] < float(weight_attribute): 
				self.filteredweights.append(edges[2])
		self.remove_weights(graph)
		
	def remove_nodes(self, graph):
		if len(self.filterednodes) != 0:
			for item in list(graph.edges()):
				if item[0] not in self.filterednodes and item[1] not in self.filterednodes:
					continue
				else:
					graph.remove_edge(item[0], item[1])
					graph.remove_nodes_from(list(nx.isolates(graph)))
				
	def remove_weights(self,graph):
		for edges in list(graph.edges(data='weight')):
			if edges[2] not in self.filteredweights: 
				continue
			else:
				graph.remove_edge(edges[0], edges[1])
				graph.remove_nodes_from(list(nx.isolates(graph)))
	
	def get_filtered_nodes(self):
		return self.filterednodes 
	
	def get_filtered_weights(self):
		return self.filteredweights
				
					
					
					

					
					
					
