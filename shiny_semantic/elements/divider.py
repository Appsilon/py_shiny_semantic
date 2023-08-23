from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace


def divider(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate a UI divider element with optional content and attributes.

    This function creates a <div> element styled as a UI divider, commonly used in user interfaces
    to visually separate content. You can provide optional children elements to include content
    within the divider, and you can also customize the styling and attributes of the divider.

    Args:
        *children (TagChildArg): Variable number of HTML content elements to be placed inside the divider.
        class_ (str, optional): Additional CSS class to apply to the divider for custom styling.
        **kwargs (TagAttrArg): Additional HTML attributes to apply to the <div> element.

    Returns:
        str: A string representing the generated HTML <div> element.

    Example:
        div_content = tags.p("This is some content within the divider.")
        div_attributes = {"id": "my-divider", "data-role": "separator"}
        divider_element = divider(
          div_content,
          class_ = "custom-divider",
          **div_attributes
        )
        print(divider_element)

    """
    return tags.div(
        *children,
        class_=squash_whitespace(f"ui {class_ or ''} divider"),
        **kwargs,
    )
