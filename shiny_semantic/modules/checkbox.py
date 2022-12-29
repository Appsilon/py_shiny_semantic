from typing import Optional

from htmltools import tags
from shiny._namespaces import resolve_id
from shiny.ui import input_checkbox

from shiny_semantic._utils import squash_whitespace


def checkbox(
    id: str,
    label: str,
    value: bool = False,
    *,
    type: Optional[str] = None,
    class_: Optional[str] = None,
    **kwargs,
):

    class_ = f"{class_ or ''}"
    if value:
        class_ = f"{class_} checked"
    if type is not None:
        class_ = f"{class_} {type}"

    type_ = "checkbox"
    if type == "radio":
        type_ = "radio"

    id = resolve_id(id)

    return tags.div(
        tags.input(id=id, type_=type_, name=id, tabindex="0"),
        tags.label(label, for_=id),
        class_=squash_whitespace(f"ui {class_} checkbox"),
        **kwargs,
    )
