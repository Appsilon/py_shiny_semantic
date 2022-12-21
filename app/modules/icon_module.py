from shiny import module

from shiny_semantic.elements import icon

from ..helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Icon",
        feature_subsection(
            "Various icon sets",
            icon("users"),
            icon("wheelchair"),
            icon("file"),
            icon("map"),
        ),
        feature_subsection(
            "Loading state",
            icon("spinner", "loading"),
            icon("notched circle", "loading"),
            icon("asterisk", "loading"),
        ),
        feature_subsection(
            "Size",
            icon("home", "mini"),
            icon("home", "tiny"),
            icon("home", "small"),
            icon("home"),
            icon("home", "large"),
            icon("home", "big"),
            icon("home", "huge"),
            icon("home", "massive"),
        ),
        feature_subsection(
            "Shape and color",
            icon("home", "circular"),
            icon("home", "circular teal"),
            icon("home", "circular inverted teal"),
            icon("home", "circular colored teal"),
            icon("home", "bordered"),
            icon("home", "bordered teal"),
            icon("home", "bordered inverted teal"),
            icon("home", "bordered colored teal"),
        ),
    )


@module.server
def server(input, output, session):
    pass
