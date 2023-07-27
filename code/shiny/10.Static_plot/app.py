import numpy as np
from shiny import ui, render, App
from matplotlib import pyplot as plt

app_ui = ui.page_fluid(
	ui.h2("Random points on scatter plot"),
	ui.input_slider("n", "Number of Points", value=50, min=10, max=100, step=10),
	ui.output_plot("a_scatter_plot"),
)

def server(input, output, session):
	@output
	@render.plot
	def a_scatter_plot():
		x = np.random.rand(input.n())
		y = np.random.rand(input.n())
		return plt.scatter(x,y)

app = App(app_ui, server)

