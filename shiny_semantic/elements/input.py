from typing import Optional

from shiny._namespaces import resolve_id
from shiny.ui import tags

from shiny_semantic.elements import icon


def text_input(
    input_id: str,
    placeholder: Optional[str] = "",
    input_type: Optional[str] = "text",
    class_name: str = "",
    icon_name: Optional[str] = None,
    label: Optional[str] = None,
):
    icon_tag = None
    if icon_name is not None:
        icon_tag = icon(icon_name)
        class_name += " icon"

    label_tag = None
    if label is not None:
        label_tag = tags.div(label, class_="ui label")
        class_name += " labeled"

    return tags.div(
        label_tag,
        tags.input(
            type=input_type,
            placeholder=placeholder,
            id=resolve_id(input_id),
        ),
        icon_tag,
        class_=f"ui {class_name} input",
    )
