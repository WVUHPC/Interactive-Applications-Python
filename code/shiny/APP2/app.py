from shiny import App, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "Choose a number n:", 0, 100, 40),
    ui.output_text_verbatim("txt")
)

def server(input, output, session):
    ...

app = App(app_ui, server)

