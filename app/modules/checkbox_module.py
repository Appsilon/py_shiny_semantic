import random
import string

from shiny import module, reactive, render
from shiny.ui import output_text_verbatim

from shiny_semantic.elements import button, header, icon
from shiny_semantic.modules import (
    checkbox,
    checkbox_group,
    update_checkbox,
    update_checkbox_group,
)

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
        ),
        feature_subsection(
            "Checkbox group",
            checkbox_group(
                id="group",
                label="Slider group with custom values",
                choices={"a": "One", "b": "Two", "c": "Three"},
                selected="a",
                type="slider",
            ),
            output_text_verbatim("group_out"),
            checkbox_group(
                id="group_radio",
                label="Inline radio group",
                choices=["One", "Two", "Three"],
                type="radio",
                position="inline",
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
            checkbox_group(
                id="group_to_update",
                label="Group to be Updated",
                choices=["hello", "world"],
                selected=["hello"],
            ),
            header("Click each button many times!", class_="small"),
            button("update_group_labels", "Random labels"),
            button("update_group_values", "Random values"),
            button("update_group_group_label", "Random group label"),
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

    @reactive.Effect
    @reactive.event(input.update_group_labels)
    def _():
        labels = random.choices(string.ascii_letters, k=2)
        update_checkbox_group("group_to_update", labels=labels)

    @reactive.Effect
    @reactive.event(input.update_group_values)
    def _():
        values = random.choices([True, False], k=2)
        update_checkbox_group("group_to_update", values=values)

    @reactive.Effect
    @reactive.event(input.update_group_group_label)
    def _():
        sample = random.choices(string.ascii_letters, k=12)
        group_label = "".join(sample)
        update_checkbox_group("group_to_update", group_label=group_label)
