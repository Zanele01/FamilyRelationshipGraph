import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt

import graphTrial

#read relationships and store in an adjacency list
def create_list(adj):
	data = open('data.txt', 'r').readlines()
	for line in data:
		u,v,w = map(float, line.strip().split(' '))
		adj[u].append((v,w))
		adj[v].append((u,w))	
	return adj
	
if __name__ == '__main__':

	adj = defaultdict(list)
	adj_list = create_list(adj)

	g = nx.Graph()
	
	graphTrial.draw_graph()
	graphTrial.plot_graph()
	
