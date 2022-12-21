from shiny import module
from shiny.ui import tags

from shiny_semantic.elements import header, icon, subheader

from ..ui_helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Header",
        feature_subsection(
            "Header Sizes",
            header("Huge Header", class_name="huge"),
            header("Large Header", class_name="large"),
            header("Medium Header", class_name="medium"),
            header("Small Header", class_name="small"),
            header("Tiny Header", class_name="tiny"),
        ),
        feature_subsection(
            "Icon Header",
            header(
                icon("settings"),
                "Account settings",
                class_name="big icon",
            ),
            header(
                icon("users", "circular"),
                "Friends",
                class_name="medium icon",
            ),
            header(
                icon("plug"),
                "Uptime Guarantee",
                class_name="tiny",
            ),
        ),
        feature_subsection(
            "Subheader",
            header(
                "Account Settings",
                subheader("Manage your account settings"),
                class_name="medium",
            ),
            header(
                icon("settings"),
                tags.div(
                    "Account Settings",
                    subheader("Manage your preferences"),
                    class_="content",
                ),
                class_name="medium",
            ),
        ),
    )


@module.server
def server(input, output, session):
    pass
