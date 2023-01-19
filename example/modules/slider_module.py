import random

from shiny import module, reactive, render
from shiny.ui import output_text_verbatim

from shiny_semantic.elements import button, icon
from shiny_semantic.modules import slider, update_slider

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Slider",
        feature_subsection(
            "Simple",
            slider(
                id="slider",
                min_value=0,
                max_value=10,
                start_value=5,
            ),
            output_text_verbatim("slider_out"),
            button("update_value", "Update value", icon=icon("arrow up")),
        ),
        feature_subsection(
            "Range",
            slider(
                id="slider_range",
                min_value=-10,
                max_value=10,
                start_value=1,
                end_value=4,
            ),
            output_text_verbatim("slider_range_out"),
            button("update_range", "Update Range", icon=icon("arrow up")),
        ),
        feature_subsection(
            "Custom",
            slider(
                id="slider_custom",
                min_value=1,
                max_value=5,
                start_value=3,
                step=1,
                show_ticks=False,
                show_labels=True,
                custom_labels=["A", "B", "C", "D", "E", "F"],
                class_="big red",
            ),
            output_text_verbatim("slider_custom_out"),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="slider_out")
    @render.text
    def _():
        return input.slider()

    @output(id="slider_range_out")
    @render.text
    def _():
        return input.slider_range()

    @output(id="slider_custom_out")
    @render.text
    def _():
        return input.slider_custom()

    @reactive.Effect
    @reactive.event(input.update_value)
    def _():
        update_slider("slider", value=random.randint(0, 10))

    @reactive.Effect
    @reactive.event(input.update_range)
    def _():
        value = [random.randint(-10, 0), random.randint(0, 10)]
        update_slider("slider_range", value=value)
