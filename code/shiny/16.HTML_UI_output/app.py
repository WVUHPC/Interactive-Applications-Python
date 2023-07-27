from shiny import ui, render, App

app_ui = ui.page_fluid(
    ui.input_text("message", "Message", value="Hello, world!"),
    ui.input_checkbox_group("styles", "Styles", choices=["Bold", "Italic"]),
    ui.input_selectize("size", "HTML font size", choices=["H1", "H2", "H3", "H4"]),
    # The class_ argument is used to enlarge and center the text
    ui.output_ui("some_html", class_="display-3 text-center")
)

def server(input, output, session):
    @output
    @render.ui
    def some_html():
        x = input.message()
        if "Bold" in input.styles():
            x = ui.strong(x)
        if "Italic" in input.styles():
            x = ui.em(x)
        if "H1" in input.size():
            x = ui.h1(x)
        if "H2" in input.size():
            x = ui.h2(x)
        if "H3" in input.size():
            x = ui.h3(x)
        if "H4" in input.size():
            x = ui.h4(x)
        return x

app = App(app_ui, server)

