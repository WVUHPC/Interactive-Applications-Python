from shiny import ui, App

app_ui = ui.page_fluid(
    ui.input_date("x1", "Date input"),
    ui.input_date_range("x2", "Date range input"),
)

app = App(app_ui, None)

