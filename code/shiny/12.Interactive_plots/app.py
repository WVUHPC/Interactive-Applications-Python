from shiny import ui, App
from shinywidgets import output_widget, render_widget
import plotly.express as px
import plotly.graph_objs as go

df = px.data.iris()

app_ui = ui.page_fluid(
    ui.h2("Iris Dataset"),
    ui.div(
        ui.input_select(
            "x", label="Variable",
            choices=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        ),
        ui.input_select(
            "color", label="Color",
            choices=["species"]
        ),
        class_="d-flex gap-3"
    ),
    output_widget("my_widget")
)

def server(input, output, session):
    @output
    @render_widget
    def my_widget():
        fig = px.histogram(
            df, x=input.x(), color=input.color(),
            marginal="rug"
        )
        fig.layout.height = 275
        return fig

app = App(app_ui, server)

