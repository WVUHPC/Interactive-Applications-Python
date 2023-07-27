from shiny import *
from shinywidgets import output_widget, render_widget
import ipyleaflet as L

basemaps = {
  "OpenStreetMap": L.basemaps.OpenStreetMap.Mapnik,
  "Stamen.Toner": L.basemaps.Stamen.Toner,
  "Stamen.Terrain": L.basemaps.Stamen.Terrain,
  "Stamen.Watercolor": L.basemaps.Stamen.Watercolor,
  "Esri.WorldImagery": L.basemaps.Esri.WorldImagery,
  "Esri.NatGeoWorldMap": L.basemaps.Esri.NatGeoWorldMap,
}

app_ui = ui.page_fluid(
    ui.h2("West Virginia - Mountaineer Country"),
    ui.input_select(
        "basemap", "Choose a basemap",
        choices=list(basemaps.keys())
    ),
    output_widget("map")
)

def server(input, output, session):
    @output
    @render_widget
    def map():
        basemap = basemaps[input.basemap()]
        return L.Map(basemap=basemap, center=[39.6, -79.9], zoom=10)

app = App(app_ui, server)

