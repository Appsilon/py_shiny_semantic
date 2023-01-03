from htmltools import HTMLDependency, TagList, tags


def page_semantic(*args, title=None, lang="en"):
    title = title or "Semantic App"
    head = TagList(
        tags.title(title),
        _semantic_dependency(),
        _shiny_semantic_bindings(),
    )
    body = TagList(*args)
    return tags.html(
        tags.head(head),
        tags.body(body),
        lang=lang,
        style="scroll-behavior: smooth;",
    )


def _semantic_dependency():
    return HTMLDependency(
        name="semantic-ui",
        version="2.9.0",
        source={"package": "shiny_semantic", "subdir": "www/semantic"},
        script=[{"src": "fomantic.min.js"}],
        stylesheet=[{"href": "fomantic.min.css"}],
    )


def _shiny_semantic_bindings():
    return HTMLDependency(
        name="shiny-semantic-bindings",
        version="0.0.1",
        source={"package": "shiny_semantic", "subdir": "www"},
        script=[{"src": "shiny-semantic-bindings.js", "type": "module"}],
    )
