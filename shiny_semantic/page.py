from htmltools import HTMLDependency
from shiny.ui import TagList, tags


def semantic_deps():
    dep = HTMLDependency(
        name="semantic-ui",
        version="2.5.0",
        source={"package": "shiny_semantic", "subdir": "www/shared/semantic"},
        script=[{"src": "semantic.min.js"}],
        stylesheet=[{"href": "semantic.min.css"}],
    )
    return [dep]


def page_semantic(*args, title=None, lang="en"):
    title = title or "Semantic App"
    head = TagList(tags.title(title), *semantic_deps())
    body = TagList(*args)
    return tags.html(
        tags.head(head),
        tags.body(body),
        lang=lang,
    )
