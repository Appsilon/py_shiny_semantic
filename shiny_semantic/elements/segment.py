from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace


def segment(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate a UI segment element in HTML.

    This function creates a UI segment element, often used in web interfaces to visually
    separate and group content. The segment can contain various child elements, such as text,
    images, buttons, etc. It supports custom CSS classes and additional attributes.

    Args:
        *children (TagChildArg): Variable number of child elements to be included within the segment.
        class_ (str, optional): Additional CSS class for the segment element.
        **kwargs (TagAttrArg): Additional attributes to be added to the segment element.

    Returns:
        str: A string representing the generated segment element in HTML.

    Example:
        content = tags.p("This is the content of the segment.")
        segment_element = segment(
          content,
          class_ = "custom-segment",
          id = "segment-1"
        )
        print(segment_element)

    """
    return tags.div(
        *children,
        class_=squash_whitespace(f"ui {class_ or ''} segment"),
        **kwargs,
    )
