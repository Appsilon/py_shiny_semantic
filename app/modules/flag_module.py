from shiny import module

from shiny_semantic.elements import flag

from ..helpers import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Flag",
        feature_subsection(
            "Countries specified with full name",
            flag("france"),
            flag("germany"),
        ),
        feature_subsection(
            "Countries specified with ISO code",
            flag("fr"),
            flag("de"),
        ),
        feature_subsection(
            "Flag sizes",
            flag("un", "small"),
            flag("un", "medium"),
            flag("un", "large"),
            flag("un", "big"),
            flag("un", "huge"),
            flag("un", "massive"),
        ),
    )


@module.server
def server(input, output, session):
    pass
