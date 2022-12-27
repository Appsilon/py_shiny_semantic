from shiny import module, reactive, render
from shiny.ui import output_text_verbatim

from shiny_semantic.elements import button, icon
from shiny_semantic.modules import selection, update_selection

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Dropdown",
        feature_subsection(
            "Selection",
            selection(
                id="selection",
                label="Choose your option",
                choices=["One", "Two", "Three"],
            ),
            button(
                "update",
                "Update dropdown",
                icon=icon("left arrow"),
                class_="right floated",
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

    @reactive.Effect
    @reactive.event(input.update)
    def _():
        update_selection("selection", choices=["hello", "world"])
