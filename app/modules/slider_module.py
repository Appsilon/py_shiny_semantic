from shiny import module, render
from shiny.ui import output_text_verbatim

from shiny_semantic.modules import slider

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Slider",
        feature_subsection(
            "Simple",
            slider(
                id="slider",
                label="Slider",
                min_value=0,
                max_value=10,
                start_value=5,
            ),
            output_text_verbatim("slider_out"),
        ),
        feature_subsection(
            "Range",
            slider(
                id="slider_range",
                label="Range Slider",
                min_value=-10,
                max_value=10,
                start_value=1,
                end_value=4,
            ),
            output_text_verbatim("slider_range_out"),
        ),
        feature_subsection(
            "Custom",
            slider(
                id="slider_custom",
                label="Custom Slider",
                min_value=1,
                max_value=5,
                start_value=3,
                step=1,
                ticks=False,
                labels=True,
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
