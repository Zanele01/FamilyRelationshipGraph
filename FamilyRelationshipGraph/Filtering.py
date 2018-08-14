import matplotlib.pyplot as plt
import networkx as nx

class Filtering:
    
	def __init__(self):
		self.attributes = 0
		
	def select_node_data(self):
		node_attribute = input("Feauture to be viewed on screen:")
		self.attributes = int(node_attribute)
	
		try:
			selection = int(node_attribute)
		except ValueError:
			print("Invalid selection")
		
	def get_node_data(self):
		return self.attributes
		
	
	
		

	
	
	
	