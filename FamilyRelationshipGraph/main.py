#libraries
import networkx as nx
import pandas as pd
from graphdraw import Graph_draw
from Colormap import Colormap
from Filtering import Filtering
from Edge_Length import Edge_Length

if __name__ == '__main__':

    #create networkx graph
    graph = nx.Graph()

    #add colormap 
    Colormap = Colormap()
    Colormap.create_nodes('nodes.txt')
    Colormap.add_nodes(graph)

    G = Graph_draw() #create graph draw object
    G.create_edgelist('data.txt')

    #calculate edge length
    length = Edge_Length()
    length.convert_edge_weights_to_length(G.get_weights())

    G.add_edges(graph, length.get_length()) #add all edges to graph

    #Filtering nodes
    Filter = Filtering()
    Filter.filter_nodes(graph)
    Filter.remove_edges(graph)
    Filter.remove_nodes(graph)

    df = pd.DataFrame()
    df = Colormap.create_map(graph)

    G.draw_graph(graph,df)