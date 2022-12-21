from shiny.ui import h2

from shiny_semantic.elements import segment


def feature_section(title: str, *args):
    return segment(
        h2(title, class_="ui centered header"),
        *args,
        class_name="raised padded container",
    )
