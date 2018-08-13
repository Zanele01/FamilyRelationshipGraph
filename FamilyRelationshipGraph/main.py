#libraries
import networkx as nx
import pandas as pd
from Graph_Draw import Graph_Draw
from Colour_Map import Colour_Map
from Edge_Length import Edge_Length

if __name__ == '__main__':

    #create networkx graph
	graph = nx.Graph()
	#create graph draw object
	G = Graph_Draw() 
	G.create_edgelist('data.txt')

    #calculate edge length
	length = Edge_Length()
	length.convert_edge_weights_to_length(G.get_weights())
        
    #add colormap 
	Colour_Map = Colour_Map()
	Colour_Map.create_nodes('nodes.txt')
	df = pd.DataFrame()

    #add all edges to graph
	G.add_edges(graph, length.get_length())
	df = Colour_Map.create_map(graph)
	
	G.draw_graph(graph,df)
	
	