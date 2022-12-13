from shiny import App, render, ui

from shiny_semantic import page_semantic
from shiny_semantic.elements import button
from shiny_semantic.typings import ButtonType


def click_reporter(btn_class, output_id):
    return (
        ui.tags.div(
            f"{btn_class} button was clicked:",
            ui.output_text(output_id, True),
            " times",
        ),
    )


app_ui = page_semantic(
    ui.tags.div(
        button("btn_default", "Default"),
        button("btn_primary", "Primary", ButtonType.primary),
    ),
    ui.tags.div(
        click_reporter("Default", "btn_default_output"),
        click_reporter("Primary", "btn_primary_output"),
    ),
    title="Example: Buttons",
)


def server(input, output, session):
    @output(id="btn_default_output")
    @render.text
    def _():
        return input.btn_default()

    @output(id="btn_primary_output")
    @render.text
    def _():
        return input.btn_primary()


app = App(app_ui, server)
