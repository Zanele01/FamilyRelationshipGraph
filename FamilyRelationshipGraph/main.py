import networkx as nx
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from GraphDraw import GraphDraw
from ColourMap import ColourMap
from Filtering import Filtering
from EdgeLength import EdgeLength
from Display import Display


if __name__ == '__main__':

	root = tk.Tk()
	root.configure(background='white')
	root.title('Family Graph Viewer')
	root.geometry('1200x800')

	dispaly = Display(root)
	root.mainloop()
