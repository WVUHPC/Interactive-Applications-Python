from shiny import App, render, ui

app_ui = ui.page_fluid(
	ui.h2("Sum Shiny!"),
	ui.input_slider("a", "A", 0, 100, 20),
	ui.input_slider("b", "B", 0, 100, 20),
	ui.output_text_verbatim("txt"),
)

def server(input, output, session):
	@output
	@render.text
	def txt():
		return f"a+b is {input.a() + input.b()}"

app = App(app_ui, server)

