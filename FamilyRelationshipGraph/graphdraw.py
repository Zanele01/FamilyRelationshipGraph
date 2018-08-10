#libraries
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from Colormap import Colormap
from Edge_Length import Edge_Length

class Graph_draw:
    #Initializer
    def __init__(self):
        self.edges = []
        self.weights = []

    def create_edgelist(self, filename):
        data = open('data.txt', 'r').readlines()
        for line in data:
            u,v,w = map(float, line.strip().split(' '))   
            self.edges.append((int(u),int(v)))    
            self.weights.append(w)

    def get_weights(self):
        return self.weights

    def add_edges(self, graph, length):
        edge_size = len(self.edges)
        for i in range(0,edge_size):
            graph.add_edge(self.edges[i][0], self.edges[i][1], weight= self.weights[i], length = length[i]) #add edges to graph
	
    def draw_graph(self, graph, map):
        nx.draw(graph,pos=None, node_size=150,with_labels=True,node_color = map['features'].cat.codes,cmap=plt.cm.get_cmap("Set1"), edge_color = 'gray')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':

    #create networkx graph
    graph = nx.Graph()
    G = Graph_draw() #create graph draw object
    G.create_edgelist('data.txt')

    #calculate edge length
    length = Edge_Length()
    length.convert_edge_weights_to_length(G.get_weights())
        
    #add colormap 
    Colormap = Colormap()
    Colormap.create_nodes('nodes.txt')
    df = pd.DataFrame()

    G.add_edges(graph, length.get_length()) #add all edges to graph
    df = Colormap.create_map(graph)

    G.draw_graph(graph,df)