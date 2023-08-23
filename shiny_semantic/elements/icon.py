from typing import Optional

from htmltools import TagAttrArg, tags

from shiny_semantic._utils import squash_whitespace


def icon(
    icon_name: str,
    *,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate an HTML <i> element with an icon.

    This function creates an HTML <i> element that is commonly used for displaying icons using icon classes.
    The icon_name parameter specifies the icon class to be applied to the <i> element.
    Additional attributes can be passed using the kwargs parameter.

    Args:
        icon_name (str): The icon class name to be applied to the <i> element.
        class_ (str, optional): Additional CSS class(es) to be added to the <i> element.
            If not provided, only the icon class specified by icon_name will be used.
        **kwargs: Additional keyword arguments representing attributes to be added to the <i> element.

    Returns:
        dominate.tags.i: An HTML <i> element with the specified icon class and optional attributes.

    Example:
        # Creating a simple icon element
        simple_icon = icon("fa fa-star")

        # Creating an icon element with additional classes and attributes
        custom_icon = icon(
          "my-icon",
          class_ = "custom-icon",
          title = "Custom Icon",
          aria_label = "Custom"
        )

    """
    return tags.i(
        class_=squash_whitespace(f"{class_ or ''} {icon_name} icon"),
        **kwargs,
    )
