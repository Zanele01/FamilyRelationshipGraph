import networkx as nx
import matplotlib.pyplot as plt
 
class Edge_Length:
 	
	def __init__(self,graph,weight,length):
		self.G = graph
		self.edge_weight = weight
		self.edge_length = length

	def convert_edge_weights_to_length(Graph, weight_value):
		edge_length = 1 - weight_value
		return edge_length
		
	def get_edge(self):
		return self.edge_length

