import networkx as nx
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from GraphDraw import GraphDraw
from ColourMap import ColourMap
from Filtering import Filtering
from EdgeLength import EdgeLength

class Display:
	def __init__(self, window):
		self.window = window

		labelText = tk.StringVar()
		labelText.set("Enter relationship cut off")
		Dir = tk.Label(self.window,font='14', textvariable=labelText)
		Dir.grid(row=0, column=0)
		self.val = tk.StringVar()
		self.mEntry = tk.Entry(self.window, textvariable = self.val, text = 'Filter weight')
		self.mEntry.grid(row=0, column=1)

		label1 = tk.StringVar()
		label1.set("Enter Age cut off")
		Direc = tk.Label(self.window,font='14', textvariable=label1)
		Direc.grid(row=1, column=0)
		self.value = tk.StringVar()
		self.entry = tk.Entry(self.window, textvariable = self.value, text = 'Filter age')
		self.entry.grid(row=1, column=1)

		self.Button = tk.Button(self.window,font='14', text = 'OK', command = self.enter_weight)
		self.Button.grid(row=0, column=2)
		self.Button1 = tk.Button(self.window,font='14', text = 'Okay', command = self.enter_feature)
		self.Button1.grid(row=1, column=2)
		self.graphButton = tk.Button(self.window,font='14', text = 'Show original graph', command=self.draw_graph)
		self.graphButton.grid(row=3, column=0)
		self.quitButton = tk.Button(self.window,font='14', text='Quit', bg = "black", fg = "red", command=self.window.quit)
		self.quitButton.grid(row=4, column=0)

	def enter_feature(self):
		text = self.entry.get()
		try:
			text = float(text)
			self.draw_graph(feature=text)
		except ValueError:
			tk.Label(self.window,font='16', bg='red', text = 'Invalid Input').grid(row=5,column=0)

	def enter_weight(self):
		mtext = self.mEntry.get()
		try:
			mtext = float(mtext)
			self.draw_graph(weight=mtext)
		except ValueError:
			tk.Label(self.window,font='16', bg='red', text = 'Invalid Input').grid(row=5,column=0)

	def draw_graph(self, **kwargs):
		#create networkx graph
		graph = nx.Graph()

		#create graph draw object
		G = GraphDraw() 
		length = EdgeLength()
		Filter = Filtering()

		#add colormap
		Colour = ColourMap()
		Colour.create_nodes('input2.txt')
		Colour.add_nodes(graph)

		G.create_edgelist('dataset.txt')
		length.convert_edge_weights_to_length(G.get_weights())
		
		#add all edges to graph
		G.add_edges(graph, length.get_length()) 

		for key in kwargs:
			if key =='weight':
				Filter.filter_weights(graph,kwargs[key])
			elif key == 'feature':
				Filter.filter_nodes(graph,kwargs[key])

		df = pd.DataFrame()
		df = Colour.create_map(graph)
		fig = G.draw_graph(graph,df)
		
		canvas = FigureCanvasTkAgg(fig, master=self.window)
		canvas.get_tk_widget().grid(row=6, column=4)
		canvas.draw()