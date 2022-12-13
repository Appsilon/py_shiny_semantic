from random import randint

from shiny import App, reactive, render, ui

from shiny_semantic import page_semantic
from shiny_semantic.elements import button2, update_button2

app_ui = page_semantic(
    ui.tags.div(
        ui.tags.div(
            ui.tags.h1(
                "Shiny Semantic: Components Demo",
                class_="ui inverted header",
                style="margin-block: 3em;",
            ),
            class_="ui text container",
        ),
        class_="ui inverted vertical masthead center aligned segment",
    ),
    ui.tags.div(
        ui.tags.h2("Button", class_="ui header"),
        ui.tags.h3("Shiny Bound Inputs", class_="ui header"),
        button2("button", "Click me"),
        ui.tags.span(
            "Clicks:",
            ui.output_text("n_clicks", True),
            class_="item",
        ),
        button2(
            "update",
            "Update other btn's label",
            class_name="right floated",
            icon_name="arrow left",
        ),
        class_="ui raised padded container segment",
    ),
    title="Example: Buttons",
)


def server(input, output, session):
    @output(id="n_clicks")
    @render.text
    def _():
        return input.button()

    @reactive.Effect
    @reactive.event(input.update)
    def _():
        update_button2("button", label=str(randint(0, 10)))


app = App(app_ui, server)
