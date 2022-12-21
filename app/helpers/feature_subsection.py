from shiny.ui import TagList, h3


def feature_subsection(title: str, *args):
    return TagList(
        h3(title, class_="ui header"),
        *args,
    )
