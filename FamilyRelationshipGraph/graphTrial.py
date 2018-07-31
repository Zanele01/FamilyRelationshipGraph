import networkx as nx
import matplotlib.pyplot as plt

graph = nx.path_graph(5) #graph corresponding to lines in adjacency list format
graph = nx.read_adjlist("data.txt",comments='#',delimiter=None,create_using=nx.Graph(),nodetype=float,encoding='utf-8')

pos = nx.random_layout(graph)
nx.draw_networkx_nodes(graph, pos, node_size = 200)

plt.axis('off')
plt.show()