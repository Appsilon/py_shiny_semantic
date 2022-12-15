from shiny import module
from shiny.ui import tags

from shiny_semantic.elements import header, subheader

from ..helpers import feature_section, feature_subsection


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
                tags.i(class_="settings icon"),
                "Account settings",
                class_name="big icon",
            ),
            header(
                tags.i(class_="circular users icon"),
                "Friends",
                class_name="medium icon",
            ),
            header(
                tags.i(class_="plug icon"),
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
                tags.i(class_="settings icon"),
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
