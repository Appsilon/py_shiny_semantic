from htmltools import HTMLDependency
from shiny.ui import TagList, tags


def semantic_dependency():
    return HTMLDependency(
        name="fomantic-ui",
        version="2.9.0",
        source={"package": "shiny_semantic", "subdir": "www/shared/fomantic"},
        script=[{"src": "fomantic.min.js"}],
        stylesheet=[{"href": "fomantic.min.css"}],
    )


def shiny_semantic_bindings():
    return HTMLDependency(
        name="shiny-semantic-bindings",
        version="0.0.1",
        source={"package": "shiny_semantic", "subdir": "www"},
        script=[{"src": "shiny-semantic-bindings.js"}],
    )


def page_semantic(*args, title=None, lang="en"):
    title = title or "Semantic App"
    head = TagList(
        tags.title(title),
        semantic_dependency(),
        shiny_semantic_bindings(),
    )
    body = TagList(*args)
    return tags.html(
        tags.head(head),
        tags.body(body),
        lang=lang,
    )
