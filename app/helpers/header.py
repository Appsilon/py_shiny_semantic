from shiny.ui import tags


def header():
    return (
        tags.div(
            {"class": "ui top fixed menu"},
            tags.div(
                tags.i(class_="hamburger icon"),
                class_="ui basic icon button item",
                onclick="""
            $('.ui.sidebar')
                .sidebar({
                    dimPage: true,
                    blurring: true,
                    scrollLock: true,
                })
                .sidebar('toggle');
            """,
            ),
            tags.div(
                "Semantic UI + Shiny for Python",
                class_="ui header item",
                # style="margin: 0; display: flex; align-items: center;",
            ),
            tags.div(
                "Built by Appsilon",
                class_="right floating item",
            ),
        ),
    )
