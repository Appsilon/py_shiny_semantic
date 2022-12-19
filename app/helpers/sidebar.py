from shiny.ui import tags


def sidebar():
    return (
        tags.div(
            {"class": "ui left vertical menu sidebar"},
            tags.a("Item 1", class_="item"),
            tags.a("Item 2", class_="item"),
            tags.a("Item 3", class_="item"),
        ),
    )
