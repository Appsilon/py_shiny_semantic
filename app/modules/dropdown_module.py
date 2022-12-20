from shiny import module, render
from shiny.ui import output_text_verbatim

from shiny_semantic.modules import selection

from ..helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Dropdown",
        feature_subsection(
            "Selection",
            selection(
                input_id="selection",
                options=["One", "Two", "Three"],
                class_name="search",
                settings={
                    "clearable": True,
                },
            ),
            output_text_verbatim("selection_out"),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="selection_out")
    @render.text
    def _():
        return input.selection()
