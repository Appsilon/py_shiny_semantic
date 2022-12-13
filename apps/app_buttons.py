from shiny import App, render, ui

from shiny_semantic import page_semantic
from shiny_semantic.elements import button
from shiny_semantic.typings import (
    ButtonColor,
    ButtonFill,
    ButtonSize,
    ButtonType,
)


def click_reporter(btn_class, output_id):
    return (
        ui.tags.div(
            f"{btn_class} button was clicked:",
            ui.output_text(output_id, True),
            " times",
        ),
    )


app_ui = page_semantic(
    ui.tags.div(
        button("btn_default", "Default"),
        button("btn_primary", "Primary", type=ButtonType.primary),
        button("btn_secondary", "Secondary", type=ButtonType.secondary),
        button("btn_positive", "Positive", type=ButtonType.positive),
        button("btn_negative", "Negative", type=ButtonType.negative),
        button(
            "btn_outline_negative",
            "Outline Negative",
            type=ButtonType.negative,
            fill=ButtonFill.outline,
        ),
        button(
            "btn_underline_orange",
            "Underline Orange",
            type=ButtonType.default,
            fill=ButtonFill.underline,
            color=ButtonColor.orange,
        ),
        button(
            "btn_default_teal",
            "Default Teal",
            type=ButtonType.default,
            fill=ButtonFill.solid,
            color=ButtonColor.teal,
        ),
        button("btn_massive", "Massive", size=ButtonSize.massive),
        button("btn_icon", "With Icon", icon_name="pause"),
        button("btn_icon_only", icon_name="plane"),
    ),
    ui.tags.div(
        click_reporter("Default", "btn_default_output"),
        click_reporter("Primary", "btn_primary_output"),
        click_reporter("Secondary", "btn_secondary_output"),
        click_reporter("Positive", "btn_positive_output"),
        click_reporter("Negative", "btn_negative_output"),
        click_reporter("Outline Negative", "btn_outline_negative_output"),
        click_reporter("Underline Orange", "btn_underline_orange_output"),
        click_reporter("Defatul Teal", "btn_default_teal_output"),
        click_reporter("Massive", "btn_massive_output"),
        click_reporter("With Icon", "btn_icon_output"),
        click_reporter("Icon Only", "btn_icon_only_output"),
    ),
    title="Example: Buttons",
)


def server(input, output, session):
    @output(id="btn_default_output")
    @render.text
    def _():
        return input.btn_default()

    @output(id="btn_primary_output")
    @render.text
    def _():
        return input.btn_primary()

    @output(id="btn_secondary_output")
    @render.text
    def _():
        return input.btn_secondary()

    @output(id="btn_positive_output")
    @render.text
    def _():
        return input.btn_positive()

    @output(id="btn_negative_output")
    @render.text
    def _():
        return input.btn_negative()

    @output(id="btn_outline_negative_output")
    @render.text
    def _():
        return input.btn_outline_negative()

    @output(id="btn_underline_orange_output")
    @render.text
    def _():
        return input.btn_underline_orange()

    @output(id="btn_default_teal_output")
    @render.text
    def _():
        return input.btn_default_teal()

    @output(id="btn_massive_output")
    @render.text
    def _():
        return input.btn_massive()

    @output(id="btn_icon_output")
    @render.text
    def _():
        return input.btn_icon()

    @output(id="btn_icon_only_output")
    @render.text
    def _():
        return input.btn_icon_only()


app = App(app_ui, server)
