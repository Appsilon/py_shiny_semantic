from shiny.ui import tags

from shiny_semantic.elements import container, segment


def header():
    onclick_callback = """
        $('.ui.sidebar')
            .sidebar({
                transition: 'overlay',
                dimPage: true,
                blurring: true,
            })
            .sidebar('toggle');
    """

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


def hero():
    title = tags.h1(
        "Shiny Semantic: Components Demo",
        class_="ui inverted header",
        style="margin-block: 5em;",
    )

    hero = segment(
        container(title, class_="text"),
        class_="inverted vertical masthead center aligned",
    )
    return hero


def sidebar():
    def _link(item):
        return tags.a(
            item,
            href=f"#{item}",
            class_="item",
            onclick="$('.ui.sidebar').sidebar('toggle');",
        )

    return (
        tags.div(
            _link("Button"),
            _link("Emoji"),
            _link("Flag"),
            _link("Icon"),
            _link("Header"),
            _link("Input"),
            _link("Modal"),
            _link("Slider"),
            _link("Dropdown"),
            _link("Checkbox"),
            _link("Statistic"),
            class_="ui left vertical menu inverted sidebar",
            style="padding-top: 4rem;",
        ),
    )
