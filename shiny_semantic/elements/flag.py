from typing import Optional

from htmltools import TagAttrArg, tags

from shiny_semantic._utils import squash_whitespace


def flag(country: str, *, class_: Optional[str] = None, **kwargs: TagAttrArg):
    """
    Generate an inline flag icon element for a specified country.

    This function generates an inline <i> element with a CSS class representing a flag icon
    for the specified country. Additional HTML attributes can be provided using keyword arguments.

    Args:
        country (str): The name of the country for which the flag icon should be displayed.
        class_ (str, optional): Additional CSS class to be applied to the flag icon. Defaults to None.
        **kwargs: Additional HTML attributes to be added to the <i> element.

    Returns:
        str: A string representing the generated <i> element with the flag icon and attributes.

    Example:
        flag_element = flag(
          "usa",
          class_ = "large-flag",
          title = "USA Flag"
        )
        print(flag_element)

    """
    return tags.i(
        class_=squash_whitespace(f"{class_ or ''} {country} flag"),
        **kwargs,
    )
