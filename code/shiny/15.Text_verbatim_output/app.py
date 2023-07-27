from shiny import ui, render, App
import scipy.special

app_ui = ui.page_fluid(
    ui.output_text_verbatim("a_code_block"),
    # The p-3 CSS class is used to add padding on all sides of the page
    class_="p-3"
)

def server(input, output, session):
    @output
    @render.text
    def a_code_block():
        # This function should return a string
        return scipy.special.__doc__

app = App(app_ui, server)

