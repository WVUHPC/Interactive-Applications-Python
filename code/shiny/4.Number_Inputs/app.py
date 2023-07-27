from shiny import ui, App

app_ui = ui.page_fluid(
    ui.input_numeric("x1", "Number", value=10),
    ui.input_slider("x2", "Slider", value=10, min=0, max=20),
    ui.input_slider("x3", "Range slider", value=(6, 14), min=0, max=20)
)

app = App(app_ui, None)

