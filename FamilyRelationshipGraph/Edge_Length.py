import networkx as nx
import matplotlib.pyplot as plt
 
class Edge_Length:
 	
	def __init__(self):
		self.edge_length = []

	def convert_edge_weights_to_length(self, graph):
		for u,v,w in graph.edges(data='weight'):
			self.edge_length.append(1 - w)
		
	def get_edge(self):
		return self.edge_length

	