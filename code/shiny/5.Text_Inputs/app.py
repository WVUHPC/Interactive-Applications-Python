from shiny import ui, App

app_ui = ui.page_fluid(
    ui.input_text("x1", "Text", placeholder="Enter text"),
    ui.input_text_area("x2", "Text area", placeholder="Enter text"),
    ui.input_password ("x3", "Password", placeholder="Enter password"),
)

app = App(app_ui, None)

