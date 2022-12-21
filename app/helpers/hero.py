from shiny.ui import h1

from shiny_semantic.elements import container, segment


def hero():
    title = h1(
        "Shiny Semantic: Components Demo",
        class_="ui inverted header",
        style="margin-block: 5em;",
    )

    hero = segment(
        container(title, class_name="text"),
        class_name="inverted vertical masthead center aligned",
    )
    return hero
