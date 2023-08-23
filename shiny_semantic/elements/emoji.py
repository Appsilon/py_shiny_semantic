from typing import Optional

from htmltools import TagAttrArg, tags


def emoji(emoji_name: str, *, class_: Optional[str] = None, **kwargs: TagAttrArg):
    """
    Generate an <em> (emphasis) HTML tag representing an emoji.

    This function creates an HTML <em> tag that displays an emoji by using its name. The emoji name is enclosed in colons
    and should match a valid emoji name supported by the underlying system or library.

    Args:
        emoji_name (str): The name of the emoji, without colons. For example, "smile" for ":smile:".
        class_ (str, optional): CSS class to apply to the <em> tag for styling purposes. Defaults to None.
        **kwargs: Additional keyword arguments that will be added as attributes to the <em> tag.

    Returns:
        str: A string representing the generated <em> tag containing the specified emoji.

    Example:
        emoji_tag = emoji(
          "smile",
          class_ = "highlight",
          title = "Happy Face"
        )
        print(emoji_tag)

    """
    return tags.em(data_emoji=f":{emoji_name}:", class_=class_, **kwargs)
