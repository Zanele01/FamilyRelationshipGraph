import networkx as nx
import matplotlib.pyplot as plt
 
class Edge_Length:	
	def __init__(self):
		self.edge_length = []

	def convert_edge_weights_to_length(self, weights):
		for data in weights:
			self.edge_length.append(1 - data)
		
	def get_length(self):
		return self.edge_length

	