import matplotlib.pyplot as plt
import networkx as nx

class Filtering:
	def __init__(self):
		self.filterednodes = []
		
	def filter_nodes(self, graph):
		node_attribute = input("Age to be viewed on screen:")
		length = len(graph.nodes())
		for i in range(0,length):
			if graph.nodes[i]['feature'] < int(node_attribute): 
				self.filterednodes.append(i)

	def search_filterednodes(self,item):
		for node in range(0,len(self.filterednodes)):
			if node == item:
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
