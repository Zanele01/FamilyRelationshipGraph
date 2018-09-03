import networkx as nx
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

class ColourMap:
    def __init__(self):
        self.nodes = []
        self.features = []

    def create_nodes(self, filename):
        data = open(filename, 'r')
        lines = data.readlines()
        for line in lines:
            u,v = line.strip('	').split()   
            self.nodes.append(u)   
            self.features.append(float(v))
        data.close()

    def add_nodes(self,graph):
        length = len(self.nodes)
        for i in range (0,length):
            graph.add_node(self.nodes[i], feature = self.features[i])

    def create_map(self, graph):
        df = pd.DataFrame({'nodes': graph.nodes()})

        feature = []
        for item in graph.nodes(data='feature'):
            feature.append(item[1])

        df['features'] = feature
        
        df = df.set_index('nodes')
        
        df['features']=pd.Categorical(df['features'])
        df['features'].cat.codes

        return df

    def get_nodes(self):
        return self.nodes

    def get_features(self):
        return self.features