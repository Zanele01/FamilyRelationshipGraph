#libraries
import networkx as nx
import pandas as pd
import tkinter as tk
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from graphdraw import Graph_draw
from Colormap import Colormap
from Filtering import Filtering
from Edge_Length import Edge_Length

class Display:
	def __init__(self, window):
		self.window = window

		labelText = tk.StringVar()
		labelText.set("Enter relationship cut off")
		Dir = tk.Label(self.window,font='14', textvariable=labelText)
		Dir.grid(row=0, column=0)

		self.val = tk.StringVar()
		self.mEntry = tk.Entry(self.window, textvariable = self.val, text = 'Filter')
		self.mEntry.grid(row=0, column=1)

		self.Button = tk.Button(self.window,font='14', text = 'OK', command = self.Enter)
		self.Button.grid(row=1, column=0)
		self.showButton = tk.Button(self.window,font='14', text = 'Show graph', command=self.draw_graph)
		self.showButton.grid(row=2, column=0)
		self.quitButton = tk.Button(self.window,font='14', text='Quit', bg = "black", fg = "red", command=self.window.quit)
		self.quitButton.grid(row=3, column=0)

	def Enter(self):
		mtext = self.mEntry.get()
		try:
			mtext = float(mtext)
			self.draw_graph(weight=mtext)
		except:
			tk.Label(self.window,font='14', text = 'Invalid Input').grid(row=5,column=0)

	def draw_graph(self, **kwargs):
		#create networkx graph
		graph = nx.Graph()

		G = Graph_draw() #create graph draw object
		length = Edge_Length()
		Filter = Filtering()

		G.create_edgelist('dataset.txt')
		length.convert_edge_weights_to_length(G.get_weights())
		G.add_edges(graph, length.get_length()) #add all edges to graph
		
		for key in kwargs:
			if key =='weight':
				Filter.filter_weights(graph,kwargs[key])
				Filter.remove_weights(graph)
			#elif key == 'feature':


		fig = G.draw_graph(graph)
		
		canvas = FigureCanvasTkAgg(fig, master=self.window)
		canvas.get_tk_widget().grid(row=10, column=3)
		canvas.draw()

if __name__ == '__main__':

	root = tk.Tk()
	root.configure(background='white')
	root.title('Family Graph Viewer')
	root.geometry('1200x1000')

	dispaly = Display(root)
	root.mainloop()