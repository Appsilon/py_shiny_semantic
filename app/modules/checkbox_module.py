import random
import string

from shiny import module, reactive, render
from shiny.ui import output_text_verbatim

from shiny_semantic.elements import button, icon
from shiny_semantic.modules import checkbox, checkbox_group, update_checkbox

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Checkbox",
        feature_subsection(
            "Different types",
            checkbox("checkbox", "Checkbox", value=True),
            output_text_verbatim("checkbox_out"),
            checkbox("toggle", "Toggle", type="toggle"),
            output_text_verbatim("toggle_out"),
            checkbox("slider", "Slider", type="slider"),
            output_text_verbatim("slider_out"),
            checkbox("radio", "Radio", type="radio"),
            output_text_verbatim("radio_out"),
        ),
        feature_subsection(
            "Checkbox group",
            checkbox_group(
                id="group",
                labels=["One", "Two", "Three"],
                values=[True, False, False],
                group_label="Slider group",
                type="slider",
            ),
            output_text_verbatim("group_out"),
            checkbox_group(
                id="group_radio",
                labels=["One", "Two", "Three"],
                values=[False, False, False],
                group_label="Radio group",
                type="radio",
            ),
            output_text_verbatim("group_radio_out"),
        ),
        feature_subsection(
            "Server-side updates",
            checkbox("checkbox_to_update", "To be updated", type="toggle"),
            button(
                "update_checkbox",
                "Update label and value",
                icon=icon("arrow left"),
                class_="right floated",
            ),
            output_text_verbatim("update_single_out"),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="checkbox_out")
    @render.text
    def _():
        return input.checkbox()

    @output(id="toggle_out")
    @render.text
    def _():
        return input.toggle()

    @output(id="slider_out")
    @render.text
    def _():
        return input.slider()

    @output(id="radio_out")
    @render.text
    def _():
        return input.radio()

    @output(id="group_out")
    @render.text
    def _():
        return input.group()

    @output(id="group_radio_out")
    @render.text
    def _():
        return input.group_radio()

    @output(id="update_single_out")
    @render.text
    def _():
        return input.checkbox_to_update()

    @reactive.Effect
    @reactive.event(input.update_checkbox)
    def _():
        sample = random.choices(string.ascii_uppercase, k=6)
        label = "".join(sample)
        value = not input.checkbox_to_update()
        update_checkbox("checkbox_to_update", label=label, value=value)
