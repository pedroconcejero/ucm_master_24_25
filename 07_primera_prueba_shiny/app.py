from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Esto es una prueba para el máster UCM!"),
    ui.input_slider("n", "Número", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)