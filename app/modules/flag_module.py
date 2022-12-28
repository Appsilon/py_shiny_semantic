from shiny import module

from shiny_semantic.elements import flag

from ._feature_layout import feature_section, feature_subsection


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
            flag("un", class_="small"),
            flag("un", class_="medium"),
            flag("un", class_="large"),
            flag("un", class_="big"),
            flag("un", class_="huge"),
            flag("un", class_="massive"),
        ),
    )


@module.server
def server(input, output, session):
    pass
