from htmltools import HTMLDependency, TagList, tags


def page_semantic(*args, title=None, lang="en"):
    """
    Generate a HTML page with semantic structure.

    This function takes a variable number of content elements and generates an HTML page
    with a predefined semantic structure. The page includes a title, necessary dependencies,
    and the provided content elements within the <body> tag.

    Args:
        *args: Variable number of content elements to be included in the <body> of the page.
        title (str, optional): Title of the HTML page. If not provided, default title "Semantic App" is used.
        lang (str, optional): Language attribute for the HTML tag. Defaults to "en" (English).

    Returns:
        str: A string representing the generated HTML page.

    Example:
        content = TagList(tags.p("Welcome to the Shiny Semantic!"), tags.div(tags.p("Content goes here.")))
        html_page = page_semantic(content, title="My Shiny Semantic Page", lang="en")
        print(html_page)

    """
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
    """
    Generate a HTMLDependency for Semantic UI.

    This function creates an HTMLDependency object representing the necessary
    dependencies for using Semantic UI in a web application.

    Returns:
        HTMLDependency: An object containing the necessary scripts and stylesheets for Semantic UI.

    Example:
        semantic_dep = _semantic_dependency()
        # Use the dependency object appropriately in your application's context.

    """
    return HTMLDependency(
        name="semantic-ui",
        version="2.9.0",
        source={"package": "shiny_semantic", "subdir": "www/semantic"},
        script=[{"src": "fomantic.min.js"}],
        stylesheet=[{"href": "fomantic.min.css"}],
    )


def _shiny_semantic_bindings():
    """
    Generate HTML dependency for Shiny Semantic Bindings.

    This function generates an HTMLDependency object that represents the necessary
    bindings for integrating Shiny with Semantic UI components. The dependency includes
    the JavaScript source file for the bindings.

    Returns:
        HTMLDependency: An HTMLDependency object containing the Shiny Semantic Bindings.

    Example:
        semantic_bindings = _shiny_semantic_bindings()
        # Use the 'semantic_bindings' object as needed within your code.

    """
    return HTMLDependency(
        name="shiny-semantic-bindings",
        version="0.0.1",
        source={"package": "shiny_semantic", "subdir": "www"},
        script=[{"src": "shiny-semantic-bindings.js", "type": "module"}],
    )
