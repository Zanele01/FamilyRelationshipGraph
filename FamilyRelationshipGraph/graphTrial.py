import networkx as nx
import matplotlib.pyplot as plt

<<<<<<< Updated upstream
def draw_graph():
	graph = nx.path_graph(5) #graph corresponding to lines in adjacency list format
	graph = nx.read_adjlist("data.txt",comments='#',delimiter=None,create_using=nx.Graph(),nodetype=float,encoding='utf-8')
	pos = nx.random_layout(graph)
	nx.draw(graph)
=======
#graph = nx.path_graph(5) #graph corresponding to lines in adjacency list format
#nx.write_adjlist(graph,"data.txt")
graph = nx.read_adjlist("data.txt",comments='#',delimiter=None,create_using=nx.Graph(),nodetype=float,encoding='utf-8')
>>>>>>> Stashed changes

def plot_graph():
	plt.axis('off')
	plt.show()
		