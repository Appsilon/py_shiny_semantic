from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace

# TODO: there are two header options implemented in Semantic UI:
# as a heading (h1, h2, etc) and as a div. The former scales in rems
# while the latter in ems. It is easier to implement the latter, since
# no overloads or conditionals will be required, but we should think
# whether it makes sense to leave only this option.


def header(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate a semantic header element with optional UI classes.

    This function creates an HTML <div> element with the specified content children and optional
    UI classes for styling. The generated <div> acts as a header element, often used to display
    headings or titles within a user interface.

    Args:
        *children (TagChildArg): Variable number of HTML content elements to be included within the header.
        class_ (str, optional): Additional CSS classes to be applied to the header element.
        **kwargs (TagAttrArg): Additional keyword arguments to be added as attributes to the header element.

    Returns:
        str: A string representing the generated HTML header element.

    Example:
        header_content = tags.h1("Welcome to My App!")
        header_element = header(header_content, class_="highlight", id="app-header")
        print(header_element)

    """
    return tags.div(
        *children,
        class_=squash_whitespace(f"ui {class_ or ''} header"),
        **kwargs,
    )


def subheader(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Create a subheader HTML element with optional classes and attributes.

    This function generates an HTML <div> element to represent a subheader. It allows
    specifying child elements to be included within the subheader, along with optional
    classes and additional HTML attributes.

    Args:
        *children (TagChildArg): Variable number of child elements to be included within the subheader.
        class_ (str, optional): CSS class(es) to be applied to the subheader. Multiple classes can be provided
            by separating them with a space. The "sub header" class is automatically added to the specified classes.
        **kwargs (TagAttrArg): Additional HTML attributes to be applied to the subheader.

    Returns:
        str: A string representing the generated subheader HTML element.

    Example:
        subheader_element = subheader(
          tags.h2("Important Information"),
          class_ = "highlight",
          id = "info-header"
        )
        print(subheader_element)

    """
    return tags.div(
        *children,
        class_=squash_whitespace(f"{class_ or ''} sub header"),
        **kwargs,
    )
