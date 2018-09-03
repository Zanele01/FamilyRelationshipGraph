import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation
from networkx.drawing.nx_agraph import graphviz_layout
from Filtering import Filtering

class Graph_draw:

	def __init__(self):
		self.edges = []
		self.fig = plt.figure(figsize=(8,8))
		self.ax = self.fig.add_subplot(1,1,1)
		self.weights = []
		
	def create_edgelist(self, filename):
		data = open(filename, 'r')
		lines = data.readlines()
		for line in lines:
				u,v,w = line.strip('	').split()  
				self.edges.append((u,v))    
				self.weights.append(float(w))	
		data.close()
		
	def get_weights(self):
		return self.weights
		
	def get_edges(self):
		return self.edges
		
	def add_edges(self, graph, length):
		edge_size = len(self.edges)
		for i in range(0, edge_size):
			graph.add_edge(self.edges[i][0], self.edges[i][1], weight = self.weights[i], length = length[i]) #add edges to graph
		
	def animate(self):
		self.ax.clear()
		return self.ax

	def draw_graph(self, graph, map):
		anim = animation.FuncAnimation(self.fig, self.draw_graph)
		positions = graphviz_layout(graph)#, k=0.99*1/np.sqrt(len(graph.nodes())))#*1/np.sqrt(len(graph.nodes())))
		nx.draw(graph,ax= self.ax, pos = positions, node_size = 30, node_color = map['features'].cat.codes, cmap = plt.cm.get_cmap("tab20"), edge_color = 'gray')
		labels = nx.get_edge_attributes(graph,'weight')
		nx.draw_networkx_edge_labels(graph,positions,edge_labels=labels, font_size = 3)
		plt.savefig("graph.pdf")
		return plt.gcf()	
