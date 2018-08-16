import matplotlib.pyplot as plt
import networkx as nx

from Edge_Length import Edge_Length

class Filtering:
	def __init__(self):
		self.filterednodes = []
		self.filteredweights = []
		
	def filter_nodes(self, graph,node_attribute):
		length = len(graph.nodes())
		for i in range(0,length):
			if graph.nodes[i]['feature'] < int(node_attribute): 
				self.filterednodes.append(i)
				
	def filter_weights(self,graph,weight_attribute):
		for edges in graph.edges(data='weight'):
			if edges[2] < float(weight_attribute): 
				self.filteredweights.append(edges[2])
				
	def search_filterednodes(self,item):
		for node in range(0,len(self.filterednodes)):
			if node == item:
				return True
		return False
	
	def search_filteredweights(self,item):
		for weight in range(0,len(self.filteredweights)):
			if self.filteredweights[weight] == item:
				return True
		return False
		
	def remove_edges(self, graph):
		if len(self.filterednodes) != 0:
			for item in list(graph.edges()):
				if self.search_filterednodes(item[0]) == True or self.search_filterednodes(item[1]) == True:
					graph.remove_edge(item[0], item[1])
	
	def remove_nodes(self,graph):
		for item in list(graph.nodes()):
			if self.search_filterednodes(item) == True:
				graph.remove_node(item)
				
	def remove_filteredweights(self,graph):
		for edges in list(graph.edges(data='weight')):
			if self.search_filteredweights(edges[2]) == True: 
				graph.remove_edge(edges[0], edges[1])
	
	def get_filtered_nodes(self):
		return self.filterednodes 
	
	def get_filtered_weights(self):
		return self.filteredweights
				
					
					
					
