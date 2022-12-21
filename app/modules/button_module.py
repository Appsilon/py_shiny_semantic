from random import randint

from shiny import module, reactive, render
from shiny.ui import output_text, tags

from shiny_semantic.elements import button, update_button

from ..helpers import feature_section, feature_subsection


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
                    class_name="right floated",
                    icon_name="arrow left",
                ),
            ),
            feature_subsection(
                "Button Types",
                button("btn1", "Default"),
                button("btn2", "Primary", class_name="primary"),
                button("btn3", "Secondary", class_name="secondary"),
                button("btn4", "Basic", class_name="basic"),
                button("btn5", "Tertiary", class_name="tertiary"),
                button("btn6", "Icon", icon_name="pause"),
            ),
            feature_subsection(
                "Button Colors",
                button("btn7", "Positive", class_name="positive"),
                button("btn8", "Negative", class_name="negative"),
                button("btn9", "Purple", class_name="purple"),
                button("btn10", "Olive", class_name="olive"),
                button("btn11", "Orange", class_name="basic orange"),
                button("btn12", "Teal", class_name="tertiary teal"),
            ),
            feature_subsection(
                "Button Sizes",
                button("btn13", "Mini", class_name="mini"),
                button("btn14", "Tiny", class_name="tiny"),
                button("btn15", "Small", class_name="small"),
                button("btn16", "Medium", class_name="medium"),
                button("btn17", "Large", class_name="large"),
                button("btn18", "Big", class_name="big"),
            ),
            feature_subsection(
                "Button Social",
                button(
                    "btn19",
                    "Facebook",
                    class_name="facebook",
                    icon_name="facebook",
                ),
                button(
                    "btn20",
                    "Linkedin",
                    class_name="linkedin",
                    icon_name="linkedin",
                ),
                button(
                    "btn21",
                    "Instagram",
                    class_name="instagram",
                    icon_name="instagram",
                ),
                button(
                    "btn22",
                    class_name="circular whatsapp icon",
                    icon_name="whatsapp",
                ),
                button(
                    "btn23",
                    class_name="circular telegram icon",
                    icon_name="telegram",
                ),
                button(
                    "btn24",
                    class_name="circular twitter icon",
                    icon_name="twitter",
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
