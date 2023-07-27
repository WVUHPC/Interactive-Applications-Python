from shiny import ui, App

app_ui = ui.page_fluid(
    ui.input_checkbox("x1", "Checkbox"),
    ui.input_switch("x2", "Switch")
)

app = App(app_ui, None)

