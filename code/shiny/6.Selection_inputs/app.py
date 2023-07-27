from shiny import ui, App

choices = ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]

app_ui = ui.page_fluid(
	ui.h2("Platonic Solids"),
	ui.input_selectize("x1", "Selectize (single)", choices),
	ui.input_selectize("x2", "Selectize (multiple)", choices, multiple = True),
	ui.input_select("x3", "Select (single)", choices),
	ui.input_select("x4", "Select (multiple)", choices, multiple = True),
	ui.input_radio_buttons("x5", "Radio buttons", choices),
    	ui.input_checkbox_group("x6", "Checkbox group", choices),
)

app = App(app_ui, None)

