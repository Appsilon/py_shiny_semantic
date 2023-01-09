from shiny import module, reactive, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import button
from shiny_semantic.modules import modal, modal_show

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Modal",
        feature_subsection(
            "Default modal",
            button("default_modal", "Open Default Modal"),
            tags.div("Modal result:", output_text("default_out", inline=True)),
        ),
        feature_subsection(
            "Basic modal",
            button("basic_modal", "Open Basic Modal", class_="secondary"),
            tags.div("Modal result:", output_text("basic_out", inline=True)),
        ),
        feature_subsection(
            "With custom props",
            button("props_modal", "Open Modal", class_="teal"),
            tags.div("Clicks:", output_text("props_out", inline=True)),
        ),
    )


@module.server
def server(input, output, session):
    @reactive.Effect
    @reactive.event(input.default_modal)
    async def _():
        await modal_show(
            modal_ui=modal(
                id="default_modal_ui",
                header="Hello World",
                content="Lorem Ipsum",
            ),
            shiny_input="default_modal_result",
            session=session,
        )

    @reactive.Effect
    @reactive.event(input.basic_modal)
    async def _():
        await modal_show(
            modal_ui=modal(
                id="basic_modal_ui",
                header="Hello World",
                content="Lorem Ipsum",
                class_="basic",
            ),
            shiny_input="basic_modal_result",
            session=session,
        )

    @reactive.Effect
    @reactive.event(input.props_modal)
    async def _():
        await modal_show(
            modal_ui=modal(
                id="props_modal_ui",
                header=tags.h3("Placeholder content"),
                content=tags.div(
                    tags.div(class_="square image"),
                    tags.div(class_="line"),
                    tags.div(class_="line"),
                    tags.div(class_="line"),
                    class_="ui placeholder",
                ),
                actions=tags.div(
                    button(
                        session.ns("modal_test"),
                        "Click",
                        class_="left floated",
                    ),
                    button(
                        session.ns("modal_dismiss"),
                        "Dismiss",
                        class_="approve secondary",
                    ),
                ),
                class_="mini",
            ),
            shiny_input="props_modal_result",
            modal_props={
                "closable": False,
                "inverted": True,
                "blurring": True,
                "transition": {
                    "showMethod": "fade down",
                    "showDuration": 600,
                    "hideMethod": "fade up",
                    "hideDuration": 600,
                },
            },
            session=session,
        )

    @output(id="default_out")
    @render.text
    def _():
        return input.default_modal_result()

    @output(id="basic_out")
    @render.text
    def _():
        return input.basic_modal_result()

    @output(id="props_out")
    @render.text
    def _():
        return input.modal_test()
