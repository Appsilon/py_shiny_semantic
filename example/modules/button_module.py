from random import randint

from shiny import module, reactive, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import button, icon, update_button

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return (
        feature_section(
            "Button",
            feature_subsection(
                "Shiny Bound Inputs",
                button("button", "Click me"),
                tags.span(
                    "Clicks:",
                    output_text("n_clicks", True),
                    class_="item",
                ),
                button(
                    "update",
                    "Update other btn's label",
                    icon=icon("arrow left"),
                    class_="right floated",
                ),
            ),
            feature_subsection(
                "Button Types",
                button("btn1", "Default"),
                button("btn2", "Primary", class_="primary"),
                button("btn3", "Secondary", class_="secondary"),
                button("btn4", "Basic", class_="basic"),
                button("btn5", "Tertiary", class_="tertiary"),
                button("btn6", "Icon", icon=icon("pause")),
            ),
            feature_subsection(
                "Button Colors",
                button("btn7", "Positive", class_="positive"),
                button("btn8", "Negative", class_="negative"),
                button("btn9", "Purple", class_="purple"),
                button("btn10", "Olive", class_="olive"),
                button("btn11", "Orange", class_="basic orange"),
                button("btn12", "Teal", class_="tertiary teal"),
            ),
            feature_subsection(
                "Button Sizes",
                button("btn13", "Mini", class_="mini"),
                button("btn14", "Tiny", class_="tiny"),
                button("btn15", "Small", class_="small"),
                button("btn16", "Medium", class_="medium"),
                button("btn17", "Large", class_="large"),
                button("btn18", "Big", class_="big"),
            ),
            feature_subsection(
                "Button Social",
                button(
                    "btn19",
                    "Facebook",
                    icon=icon("facebook"),
                    class_="facebook",
                ),
                button(
                    "btn20",
                    "Linkedin",
                    icon=icon("linkedin"),
                    class_="linkedin",
                ),
                button(
                    "btn21",
                    "Instagram",
                    icon=icon("instagram"),
                    class_="instagram",
                ),
                button(
                    "btn22",
                    icon=icon("whatsapp"),
                    class_="circular whatsapp icon",
                ),
                button(
                    "btn23",
                    icon=icon("telegram"),
                    class_="circular telegram icon",
                ),
                button(
                    "btn24",
                    icon=icon("twitter"),
                    class_="circular twitter icon",
                ),
            ),
        ),
    )


@module.server
def server(input, output, session):
    @output(id="n_clicks")
    @render.text
    def _():
        return input.button()

    @reactive.Effect
    @reactive.event(input.update)
    def _():
        update_button("button", label=str(randint(0, 10)))
