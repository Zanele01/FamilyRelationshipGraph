import matplotlib.pyplot as plt
import pandas as pd

class Colormap:
    def __init__(self):
        self.nodes = []
        self.features = []

    def create_nodes(self, filename):
        nodes = open(filename, 'r').readlines()
        for line in nodes:
            u,v = map(int, line.strip().split(' '))   
            self.nodes.append(u)   
            self.features.append(v)

    def get_nodes(self):
        return self.nodes

    def get_features(self):
        return self.features

    def create_map(self, graph):
        df = pd.DataFrame({'nodes': self.nodes})
        df['features'] = self.features
        
        df = df.set_index('nodes')
        df = df.reindex(graph.nodes())
        
        df['features']=pd.Categorical(df['features'])
        df['features'].cat.codes
        
        return df