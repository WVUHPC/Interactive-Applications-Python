from shiny import ui, render, App

app_ui = ui.page_fluid(
    ui.output_text("my_cool_text")
)

def server(input, output, session):
    @output
    @render.text
    def my_cool_text():
        return "hello, world!"

app = App(app_ui, server)

