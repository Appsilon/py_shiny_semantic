from shiny.ui import tags


def sidebar():
    return (
        tags.div(
            _link("Button"),
            _link("Emoji"),
            _link("Flag"),
            _link("Icon"),
            _link("Header"),
            _link("Input"),
            _link("Modal"),
            _link("Dropdown"),
            class_="ui left vertical menu inverted sidebar",
            style="padding-top: 4rem;",
        ),
    )


def _link(item):
    return tags.a(
        item,
        href=f"#{item}",
        class_="item",
        onclick="$('.ui.sidebar').sidebar('toggle');",
    )
