from shiny import ui, App

app_ui = ui.page_fluid(
	ui.p(ui.input_action_button("x1", "Action button")),
	ui.p(ui.input_action_button("x2", "Action button (Primary)", class_="btn-primary")),
	ui.p(ui.input_action_button("x3", "Action button (Danger)", class_="btn-danger")),
	ui.p(ui.input_action_link("x4", "Action link")),
)

app = App(app_ui, None)

