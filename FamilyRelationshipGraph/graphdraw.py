import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation
from networkx.algorithms import bipartite
from Filtering import Filtering

class Graph_draw:

	def __init__(self):
		self.edges = []
		self.fig = plt.figure(figsize=(7,7))
		self.ax = self.fig.add_subplot(1,1,1)
		self.weights = []
		self.filter = []
		
	def create_edgelist(self, filename):
		data = open(filename, 'r')
		lines = data.readlines()
		count = 0
		for line in lines:
			count = count+1

			if count == 1:
				self.filter = [4]
			else:
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

	def draw_graph(self, graph): # map):
		anim = animation.FuncAnimation(self.fig, self.draw_graph)
		positions = nx.spring_layout(graph, random_state=10)
		nx.draw(graph,ax= self.ax, pos = positions, node_size = 20)#, with_labels = True, node_color = map['features'].cat.codes, cmap = plt.cm.get_cmap("Set1"), edge_color = 'gray')
		plt.savefig("graph.pdf")
		return plt.gcf()	