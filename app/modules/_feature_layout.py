from shiny.ui import TagList, h2, h3, tags

from shiny_semantic.elements import segment


def feature_section(title: str, *args):
    return TagList(
        tags.div(id=title, style="opacity: 0; margin-bottom: 5rem;"),
        segment(
            h2(title, class_="ui centered header"),
            *args,
            class_="raised padded container",
        ),
    )


def feature_subsection(title: str, *args):
    return TagList(
        h3(title, class_="ui header"),
        *args,
    )
