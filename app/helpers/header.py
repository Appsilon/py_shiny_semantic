from shiny.ui import tags

onclick_callback = """
    $('.ui.sidebar')
        .sidebar({
            transition: 'overlay',
            dimPage: true,
            blurring: true,
        })
        .sidebar('toggle');
"""


def header():
    return (
        tags.div(
            tags.div(
                "Semantic UI + Shiny for Python",
                class_="ui header item",
            ),
            tags.div(
                tags.i(class_="hamburger icon"),
                class_="ui basic icon button item",
                onclick=onclick_callback,
            ),
            tags.div(
                "Built by Appsilon",
                class_="right floating item",
            ),
            class_="ui top fixed menu",
            style="z-index: 103;",
        ),
    )
