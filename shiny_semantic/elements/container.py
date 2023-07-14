from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace


def container(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Create a container HTML element with optional classes and attributes.

    This function generates an HTML <div> element with the specified content elements as children.
    It can be used to encapsulate content within a container, often used in web design frameworks.
    
    Args:
        *children (TagChildArg): Variable number of content elements to be included inside the container.
        class_ (str, optional): Additional classes to be added to the container's class attribute.
            Default is None.
        **kwargs (TagAttrArg): Additional attributes to be added to the container element.

    Returns:
        str: A string representing the generated HTML container element.

    Example:
        container_content = tags.p("This is content inside the container.")
        container_element = container(
          container_content,
          class_ = "my-custom-class",
          id = "container1"
        )
        print(container_element)

    """
    return tags.div(
        *children,
        class_=squash_whitespace(f"ui {class_ or ''} container"),
        **kwargs,
    )
