from typing import Optional

from htmltools import TagAttrArg
from shiny._namespaces import resolve_id
from shiny.ui import tags

from shiny_semantic.elements import icon

from .._utils import strip_whitespace


def text_input(
    input_id: str,
    placeholder: Optional[str] = "",
    value: str = "",
    label: Optional[str] = None,
    icon_name: Optional[str] = None,
    input_type: str = "text",
    class_name: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    # Enclosing div's class
    if class_name is None:
        class_name = ""

    # Define icon inside the input
    icon_tag = None
    if icon_name is not None:
        icon_tag = icon(icon_name)
        class_name += " icon"

    # Define the label
    label_tag = None
    if label is not None:
        label_tag = tags.div(label, class_="ui label")
        class_name += " labeled"

    # Finalize & clean the div's class
    class_ = strip_whitespace(f"ui {class_name} input")

    return tags.div(
        label_tag,
        tags.input(
            id=resolve_id(input_id),
            type=input_type,
            value=value,
            placeholder=placeholder,
            **kwargs,
        ),
        icon_tag,
        class_=class_,
    )
