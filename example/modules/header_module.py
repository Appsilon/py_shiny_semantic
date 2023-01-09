from shiny import module
from shiny.ui import tags

from shiny_semantic.elements import header, icon, subheader

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Header",
        feature_subsection(
            "Header Sizes",
            header("Huge Header", class_="huge"),
            header("Large Header", class_="large"),
            header("Medium Header", class_="medium"),
            header("Small Header", class_="small"),
            header("Tiny Header", class_="tiny"),
        ),
        feature_subsection(
            "Icon Header",
            header(
                icon("settings"),
                "Account settings",
                class_="big icon",
            ),
            header(
                icon("users", class_="circular"),
                "Friends",
                class_="medium icon",
            ),
            header(
                icon("plug"),
                "Uptime Guarantee",
                class_="tiny",
            ),
        ),
        feature_subsection(
            "Subheader",
            header(
                "Account Settings",
                subheader("Manage your account settings"),
                class_="medium",
            ),
            header(
                icon("settings"),
                tags.div(
                    "Account Settings",
                    subheader("Manage your preferences"),
                    class_="content",
                ),
                class_="medium",
            ),
        ),
    )


@module.server
def server(input, output, session):
    pass
