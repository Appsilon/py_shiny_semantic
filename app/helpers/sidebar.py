from shiny.ui import tags


def sidebar():
    return (
        tags.div(
            {"class": "ui left vertical menu sidebar"},
            _link("Button"),
            _link("Emoji"),
            _link("Flag"),
            _link("Icon"),
            _link("Header"),
            _link("Input"),
            _link("Modal"),
        ),
    )


def _link(item):
    return tags.a(
        item,
        href=f"#{item}",
        class_="item",
        onclick="$('.ui.sidebar').sidebar('toggle');",
    )
