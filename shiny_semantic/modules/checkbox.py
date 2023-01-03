from typing import Optional, Union

from htmltools import TagList, tags
from shiny.module import resolve_id
from shiny.session import Session, require_active_session

from shiny_semantic._utils import drop_none, squash_whitespace


def checkbox(
    id: str,
    label: str,
    value: bool = False,
    *,
    type: Optional[str] = None,
    name: Optional[str] = None,
    class_: Optional[str] = None,
    **kwargs,
):

    class_ = f"{class_ or ''}"
    if value:
        class_ = f"{class_} checked"
    if type is not None:
        class_ = f"{class_} {type}"

    input_tag_type = "checkbox"
    if type == "radio":
        input_tag_type = "radio"

    # NOTE: if the value=False, let checked_ be None, i.e. not appear in HTML
    checked = "" if value else None

    id = resolve_id(id)
    name = name or id

    return tags.div(
        tags.input(id=id, type_=input_tag_type, name=name, checked=checked),
        tags.label(label, for_=id),
        id=id,
        class_=squash_whitespace(f"ui {class_} checkbox"),
        **kwargs,
    )


def checkbox_group(
    id: str,
    label: str,
    choices: Union[list[str], dict[str, str]],
    *,
    selected: Optional[Union[list[str], tuple[str], str]] = None,
    type: Optional[str] = None,
    position: Optional[str] = "grouped",
    class_: Optional[str] = None,
):
    if isinstance(choices, list):
        choices = {choice: choice for choice in choices}

    if selected is None:
        selected = []
    if isinstance(selected, str):
        selected = [selected]

    if type == "radio" and len(selected) > 1:
        raise Exception("Radio buttons may have a maximum of 1 active value")

    checkbox_tags = TagList()
    for v, l in choices.items():
        checkbox_tag = tags.div(
            checkbox(
                # NOTE: for checkbox_group to work correctly, all individual checkboxes
                # inside it must share a common name attribute.
                id=f"{id}__{v}",
                label=l,
                value=v in selected,
                type=type,
                name=id,
                data_shiny_value=v,
            ),
            class_="field",
        )
        checkbox_tags.append(checkbox_tag)

    id = resolve_id(id)
    class_ = squash_whitespace(f"{position} {class_ or ''} fields ss-checkbox-group")

    return tags.div(
        tags.div(
            tags.label(label),
            checkbox_tags,
            id=id,
            class_=class_,
        ),
        class_="ui form",
    )


def update_checkbox(
    id: str,
    *,
    label: Optional[str] = None,
    value: Optional[bool] = None,
    session: Optional[Session] = None,
):
    session = require_active_session(session)
    msg = {"label": label, "value": value}
    session.send_input_message(id, drop_none(msg))


def update_checkbox_group(
    id: str,
    *,
    labels: Optional[list[str]] = None,
    values: Optional[list[bool]] = None,
    group_label: Optional[str] = None,
    session: Optional[Session] = None,
):
    session = require_active_session(session)
    msg = {"labels": labels, "values": values, "group_label": group_label}
    session.send_input_message(id, drop_none(msg))
