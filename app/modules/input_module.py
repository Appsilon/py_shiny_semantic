from shiny import module, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import semantic_input

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Input",
        feature_subsection(
            "Shiny Bound Text Input",
            semantic_input("text", "Text input"),
            tags.span("Text:"),
            output_text("text_output", inline=True),
            tags.br(),
            tags.br(),
            semantic_input(
                "numeric",
                "Numeric input with Props",
                input_type="number",
                value=0,
                min=-10,
                max=10,
                step=10,
            ),
            tags.span("Numeric input with Props, Value:"),
            output_text("numeric_output", inline=True),
        ),
        feature_subsection(
            "States and Variations",
            semantic_input("disabled", "Disabled", class_name="disabled"),
            semantic_input("error", "Error", class_name="error"),
            semantic_input("date", "Date", input_type="date"),
            semantic_input("email", "Email", input_type="email"),
            semantic_input("password", "Password", input_type="password"),
            semantic_input("icon", "With Icon", icon_name="users"),
            semantic_input("label", "appsilon.com", label="https://"),
            semantic_input("value", "Pre-populated", value="Some text"),
            semantic_input("numeric", "Numeric", input_type="number"),
        ),
        feature_subsection(
            "Sizes",
            semantic_input("mini", "Mini", class_name="mini"),
            semantic_input("tiny", "Tiny", class_name="tiny"),
            semantic_input("small", "Small", class_name="small"),
            semantic_input("medium", "Medium", class_name="medium"),
            semantic_input("large", "Large", class_name="large"),
            semantic_input("big", "Big", class_name="big"),
            semantic_input("huge", "Huge", class_name="huge"),
            semantic_input("massive", "Massive", class_name="massive"),
            semantic_input("fluid", "Fluid", class_name="fluid"),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="text_output")
    @render.text
    def _():
        return input.text()

    @output(id="numeric_output")
    @render.text
    def _():
        return input.numeric()
