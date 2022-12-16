from shiny import module, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import text_input

from ..helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Input",
        feature_subsection(
            "Shiny Bound Text Input",
            text_input("text", "Placeholder"),
            tags.span("Text:"),
            output_text("text_output", inline=True),
        ),
        feature_subsection(
            "States and Variations",
            text_input("disabled", "Disabled", class_name="disabled"),
            text_input("error", "Error", class_name="error"),
            text_input("date", "Date", input_type="date"),
            text_input("email", "Email", input_type="email"),
            text_input("password", "Password", input_type="password"),
            text_input("icon", "With Icon", icon_name="users"),
            text_input("label", "appsilon.com", label="https://"),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="text_output")
    @render.text
    def _():
        return input.text()
