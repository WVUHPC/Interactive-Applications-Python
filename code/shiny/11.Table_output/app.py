from pathlib import Path
import pandas as pd
from shiny import ui, render, App

df = pd.read_csv(Path(__file__).parent / "iris.csv")

app_ui = ui.page_fluid(
    ui.h2("Iris Dataset"),
    ui.output_table("iris_dataset"),
)

def server(input, output, session):
    @output
    @render.table
    def iris_dataset():
        return df

app = App(app_ui, server)


