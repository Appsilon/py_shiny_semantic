from typing import Optional, Union

from htmltools import TagAttrArg, TagChildArg, tags
from shiny.module import resolve_id

from shiny_semantic._utils import squash_whitespace


def semantic_input(
    id: str,
    value: Union[str, float] = "",
    *,
    placeholder: Optional[str] = "",
    icon: TagChildArg = None,
    type: str = "text",
    semantic_class: Optional[str] = None,
    semantic_label: Optional[str] = None,
    semantic_label_class: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate a semantic-styled input element with optional label and icon.

    This function generates a customizable HTML input element with a semantic styling,
    allowing for the addition of icons, labels, and various attributes. The input
    element is enclosed in a <div> element with appropriate classes for styling.

    Args:
        id (str): Identifier for the input element.
        value (Union[str, float], optional): Initial value of the input element. Defaults to an empty string.
        placeholder (str, optional): Placeholder text to display in the input element.
        icon (TagChildArg, optional): Icon to display with the input. Can be an HTML element or Tag object.
        type (str, optional): Type of the input element (e.g., "text", "number", "password"). Defaults to "text".
        semantic_class (str, optional): Additional classes to apply to the enclosing <div> element for styling.
        semantic_label (str, optional): Label text to display above the input element.
        semantic_label_class (str, optional): Additional classes to apply to the label element for styling.
        **kwargs (TagAttrArg): includes all html attributes relevant to the input tag, including,
        for example, `min`, `max` and `step` in case of input type = "number",
        as well as `class_` that is passed directly to the input tag,
        as opposed to the `semantic_class` that is passed to the enclosing div element.

    Returns:
        str: A string representing the generated HTML code.

    Example:
        input_with_icon = semantic_input(
            id = "username",
            placeholder = "Enter your username",
            icon = tags.i(class_ = "user icon"),
            semantic_label = "Username",
            semantic_label_class = "blue",
            required = True,
        )
        print(input_with_icon)

    """
    # Enclosing div's class
    if semantic_class is None:
        semantic_class = ""

    # Modify the enclosing div's class if icon is passed
    if icon is not None:
        semantic_class += " icon"

    # Define the label
    label_tag = None
    if semantic_label is not None:
        label_tag = tags.div(
            semantic_label,
            class_=squash_whitespace(f"ui {semantic_label_class or ''} label"),
        )
        semantic_class += " labeled"

    # Finalize & clean the div's class
    semantic_class = squash_whitespace(f"ui {semantic_class} input")

    return tags.div(
        label_tag,
        tags.input(
            id=resolve_id(id),
            type=type,
            value=value,
            placeholder=placeholder,
            **kwargs,
        ),
        icon,
        class_=semantic_class,
    )
