from shiny import module, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import text_input

from ..helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Input",
        feature_subsection(
            "Text input",
            text_input("text", "Text..."),
            tags.span("Text:"),
            output_text("text_output", inline=True),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="text_output")
    @render.text
    def _():
        return input.text()
