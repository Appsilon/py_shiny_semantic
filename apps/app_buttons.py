from shiny import App, render, ui

from shiny_semantic import input_action_button, page_semantic


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
        input_action_button("btn_default", "Default"),
        input_action_button("btn_primary", "Primary", "primary"),
        input_action_button("btn_secondary", "Secondary", "secondary"),
        input_action_button("btn_basic", "Basic", "basic"),
    ),
    ui.tags.div(
        click_reporter("Default", "btn_default_output"),
        click_reporter("Primary", "btn_primary_output"),
        click_reporter("Secondary", "btn_secondary_output"),
        click_reporter("Basic", "btn_basic_output"),
    ),
    title="Example: Buttons",
)


def server(input, output, session):
    @output
    @render.text
    def btn_default_output():
        return input.btn_default()

    @output
    @render.text
    def btn_primary_output():
        return input.btn_primary()

    @output
    @render.text
    def btn_secondary_output():
        return input.btn_secondary()

    @output
    @render.text
    def btn_basic_output():
        return input.btn_basic()


app = App(app_ui, server)
