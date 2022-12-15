from random import randint

from shiny import reactive, render, ui

from shiny_semantic import page_semantic
from shiny_semantic.elements import button, emoji, update_button

from .helpers import hero

app_ui = page_semantic(
    hero(),
    ui.tags.div(
        ui.tags.h2("Button", class_="ui centered header"),
        ui.tags.h3("Shiny Bound Inputs", class_="ui header"),
        button("button", "Click me"),
        ui.tags.span(
            "Clicks:",
            ui.output_text("n_clicks", True),
            class_="item",
        ),
        button(
            "update",
            "Update other btn's label",
            class_name="right floated",
            icon_name="arrow left",
        ),
        ui.tags.h3("Button Types", class_="ui header"),
        ui.tags.div(
            button("btn1", "Default"),
            button("btn2", "Primary", class_name="primary"),
            button("btn3", "Secondary", class_name="secondary"),
            button("btn4", "Basic", class_name="basic"),
            button("btn5", "Tertiary", class_name="tertiary"),
            button("btn6", "Icon", icon_name="pause"),
            class_="ui container",
        ),
        ui.tags.h3("Button Colors", class_="ui header"),
        ui.tags.div(
            button("btn7", "Positive", class_name="positive"),
            button("btn8", "Negative", class_name="negative"),
            button("btn9", "Purple", class_name="purple"),
            button("btn10", "Olive", class_name="olive"),
            button("btn11", "Orange", class_name="basic orange"),
            button("btn12", "Teal", class_name="tertiary teal"),
            class_="ui container",
        ),
        ui.tags.h3("Button Sizes", class_="ui header"),
        ui.tags.div(
            button("btn13", "Mini", class_name="mini"),
            button("btn14", "Tiny", class_name="tiny"),
            button("btn15", "Small", class_name="small"),
            button("btn16", "Medium", class_name="medium"),
            button("btn17", "Large", class_name="large"),
            button("btn18", "Big", class_name="big"),
            class_="ui container",
        ),
        ui.tags.h3("Button Social", class_="ui header"),
        ui.tags.div(
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
            class_="ui container",
        ),
        class_="ui raised padded container segment",
    ),
    ui.tags.div(
        ui.tags.h2("Emoji", class_="ui centered header"),
        ui.tags.h3("Different sets", class_="ui header"),
        emoji(emoji_name="smile"),
        emoji(emoji_name="angry"),
        emoji(emoji_name="bee"),
        emoji(emoji_name="blowfish"),
        emoji(emoji_name="apple"),
        emoji(emoji_name="avocado"),
        emoji(emoji_name="badminton"),
        emoji(emoji_name="dart"),
        emoji(emoji_name="airplane"),
        ui.tags.h3("Skin tones", class_="ui header"),
        emoji("adult"),
        emoji("adult_tone1"),
        emoji("adult_tone2"),
        emoji("adult_tone3"),
        emoji("adult_tone4"),
        emoji("adult_tone5"),
        ui.tags.h3("Sizes", class_="ui header"),
        emoji("flag_pl", class_name="tiny"),
        emoji("flag_pl", class_name="small"),
        emoji("flag_pl", class_name="medium"),
        emoji("flag_pl", class_name="large"),
        emoji("flag_pl", class_name="big"),
        class_="ui raised padded container segment",
    ),
    title="Example: Buttons",
)


def app_server(input, output, session):
    @output(id="n_clicks")
    @render.text
    def _():
        return input.button()

    @reactive.Effect
    @reactive.event(input.update)
    def _():
        update_button("button", label=str(randint(0, 10)))
