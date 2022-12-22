from shiny import module

from shiny_semantic.elements import icon

from ._feature_layout import feature_section, feature_subsection


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
            icon("spinner", class_="loading"),
            icon("notched circle", class_="loading"),
            icon("asterisk", class_="loading"),
        ),
        feature_subsection(
            "Size",
            icon("home", class_="mini"),
            icon("home", class_="tiny"),
            icon("home", class_="small"),
            icon("home"),
            icon("home", class_="large"),
            icon("home", class_="big"),
            icon("home", class_="huge"),
            icon("home", class_="massive"),
        ),
        feature_subsection(
            "Shape and color",
            icon("home", class_="circular"),
            icon("home", class_="circular teal"),
            icon("home", class_="circular inverted teal"),
            icon("home", class_="circular colored teal"),
            icon("home", class_="bordered"),
            icon("home", class_="bordered teal"),
            icon("home", class_="bordered inverted teal"),
            icon("home", class_="bordered colored teal"),
        ),
    )


@module.server
def server(input, output, session):
    pass
