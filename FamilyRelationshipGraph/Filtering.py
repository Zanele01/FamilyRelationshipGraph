import matplotlib.pyplot as plt
import networkx as nx

class Filtering:
    
    def __init__(self):
        self.attributes = []
		
	def select_node_data(self, node_attribute):
		node_attribute = input("Age to be viewed on screen:")
		self.attributes.append(node_attribute)
	
		try:
			selection = int(node_attribute)
		except ValueError:
			print("Invalid selection")
			
	def get_graph_data(self):
		return self.attributes
		
	def display_graph_data(self, graph):
		for attributes in graph.nodes(data = True):
				print (attributes)
	
	