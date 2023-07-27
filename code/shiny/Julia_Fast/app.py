import matplotlib.pyplot as plt
import numpy as np
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("ar", "Real(a)", min=-1.0, max=1.0, value=-0.744, step=0.01),
            ui.input_slider("ai", "Imag(a)", min=-1.0, max=1.0, value=0.148, step=0.01),
            ui.input_slider("n", "Number of Iterations", min=1, max=100, value=20, step=1),
        ),
        ui.panel_main(
            ui.output_plot("julia_plot"),
        ),
    ),
)


def server(input, output, session):
    @output
    @render.plot(alt="Julia")
    def julia_plot():
        h_range = 500
        w_range = 1000
        max_iterations = input.n()
        y, x = np.ogrid[1.4: -1.4: h_range * 1j, -2.8: 2.8: w_range * 1j]
        z_array = x + y * 1j
        a = input.ar() + input.ai() * 1j
        iterations_until_divergence = max_iterations + np.zeros(z_array.shape)

        # create array of all True
        not_already_diverged = iterations_until_divergence < 10000

        # create array of all False
        diverged_in_past = iterations_until_divergence > 10000

        for i in range(max_iterations):
            z_array = z_array ** 2 + a

            z_size_array = z_array * np.conj(z_array)
            diverging = z_size_array > 4

            diverging_now = diverging & not_already_diverged
            iterations_until_divergence[diverging_now] = i

            not_already_diverged = np.invert(diverging_now) & not_already_diverged

            # prevent overflow (values headed towards infinity) for diverging locations
            diverged_in_past = diverged_in_past | diverging_now
            z_array[diverged_in_past] = 0

        plt.imshow(iterations_until_divergence, cmap='twilight_shifted')


app = App(app_ui, server, debug=True)
