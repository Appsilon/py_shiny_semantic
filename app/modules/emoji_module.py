from shiny import module

from shiny_semantic.elements import emoji

from ..helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Emoji",
        feature_subsection(
            "Different sets",
            emoji(emoji_name="smile"),
            emoji(emoji_name="angry"),
            emoji(emoji_name="bee"),
            emoji(emoji_name="blowfish"),
            emoji(emoji_name="apple"),
            emoji(emoji_name="avocado"),
            emoji(emoji_name="badminton"),
            emoji(emoji_name="dart"),
            emoji(emoji_name="airplane"),
        ),
        feature_subsection(
            "Skin tones",
            emoji("adult"),
            emoji("adult_tone1"),
            emoji("adult_tone2"),
            emoji("adult_tone3"),
            emoji("adult_tone4"),
            emoji("adult_tone5"),
        ),
        feature_subsection(
            "Sizes",
            emoji("leo", class_name="tiny"),
            emoji("leo", class_name="small"),
            emoji("leo", class_name="medium"),
            emoji("leo", class_name="large"),
            emoji("leo", class_name="big"),
        ),
    )


@module.server
def server(input, output, session):
    pass
