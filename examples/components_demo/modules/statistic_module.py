from htmltools import TagList
from shiny import module

from shiny_semantic.elements import icon
from shiny_semantic.views import statistic

from ._feature_layout import feature_section, feature_subsection


@module.ui
def ui():
    return feature_section(
        "Statistic",
        feature_subsection(
            "Value first",
            statistic(123, "subscribers"),
        ),
        feature_subsection(
            "Label first",
            statistic(123, "subscribers", value_first=False),
        ),
        feature_subsection(
            "Arbitrary content",
            statistic(
                TagList(
                    icon("globe americas"),
                    "SEVEN",
                    icon("globe asia"),
                ),
                "Continents on Earth",
                class_="brown",
            ),
        ),
    )


@module.server
def server(input, output, session):
    pass
