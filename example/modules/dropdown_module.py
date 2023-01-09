import random
import string

from shiny import module, reactive, render
from shiny.ui import output_text_verbatim

from shiny_semantic.elements import button, icon
from shiny_semantic.modules import dropdown, input_select, update_select

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Dropdown",
        feature_subsection(
            "Selection",
            input_select(
                id="selection",
                label="Dropdown Label",
                placeholder="Select",
                choices=["One", "Two", "Three"],
            ),
            button(
                "update",
                "Update label & choices",
                icon=icon("up arrow"),
                class_="right floated",
            ),
            output_text_verbatim("selection_out"),
        ),
        feature_subsection(
            "Customizable Selection",
            dropdown(
                id="selection_custom",
                placeholder="Fluid + Clearable + Searchable + Multiple",
                choices=["hello", "world"],
                value=["hello", "world"],
                settings={
                    "clearable": True,
                },
                class_="multiple search",
            ),
            output_text_verbatim("selection_custom_out"),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="selection_out")
    @render.text
    def _():
        return input.selection()

    @output(id="selection_custom_out")
    @render.text
    def _():
        return input.selection_custom()

    @reactive.Effect
    @reactive.event(input.update)
    def _():
        choices = random.choices(population=string.ascii_uppercase, k=5)
        label = "".join(choices)
        update_select(
            "selection",
            choices=choices,
            label=label,
        )
