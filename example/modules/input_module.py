from shiny import module, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import icon, semantic_input

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Input",
        feature_subsection(
            "Shiny Bound Text Input",
            semantic_input("text", placeholder="Text input"),
            tags.span("Text:"),
            output_text("text_output", inline=True),
            tags.br(),
            tags.br(),
            semantic_input(
                "numeric",
                placeholder="Numeric input with Props",
                type="number",
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
            semantic_input("disabled", placeholder="Disabled", semantic_class="disabled"),
            semantic_input("error", placeholder="Error", semantic_class="error"),
            semantic_input("date", placeholder="Date", type="date"),
            semantic_input("email", placeholder="Email", type="email"),
            semantic_input("password", placeholder="Password", type="password"),
            semantic_input("icon", placeholder="With Icon", icon=icon("users")),
            semantic_input(
                "label",
                placeholder="appsilon.com",
                semantic_label="https://",
            ),
            semantic_input("value", placeholder="Pre-populated", value="Some text"),
            semantic_input("numeric", placeholder="Numeric", type="number"),
        ),
        feature_subsection(
            "Sizes",
            semantic_input("mini", placeholder="Mini", semantic_class="mini"),
            semantic_input("tiny", placeholder="Tiny", semantic_class="tiny"),
            semantic_input("small", placeholder="Small", semantic_class="small"),
            semantic_input("medium", placeholder="Medium", semantic_class="medium"),
            semantic_input("large", placeholder="Large", semantic_class="large"),
            semantic_input("big", placeholder="Big", semantic_class="big"),
            semantic_input("huge", placeholder="Huge", semantic_class="huge"),
            semantic_input("massive", placeholder="Massive", semantic_class="massive"),
            semantic_input("fluid", placeholder="Fluid", semantic_class="fluid"),
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
