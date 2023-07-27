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
        iterations_till_divergence = max_iterations + np.zeros(z_array.shape)

        for h in range(h_range):
            for w in range(w_range):

                z = z_array[h][w]
                for i in range(max_iterations):
                    z = z ** 2 + a
                    if z * np.conj(z) > 4:
                        iterations_till_divergence[h][w] = i
                        break
        plt.imshow(iterations_till_divergence, cmap='twilight_shifted')


app = App(app_ui, server, debug=True)
