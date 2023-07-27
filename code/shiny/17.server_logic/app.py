from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_checkbox("enable", "Enable?"),
    ui.h3("Is it enabled?"),
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        if input.enable():
            return "Yes!"
        else:
            return "No!"

app = App(app_ui, server)


