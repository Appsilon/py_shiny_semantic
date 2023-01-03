from typing import Optional, Union

from shiny._namespaces import resolve_id
from shiny._utils import drop_none
from shiny.session import Session, require_active_session
from shiny.ui import TagList, tags

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

    # NOTE: if the value=False, let checked_ be None, i.e. not appear in HTML
    checked_ = value and ""

    id = resolve_id(id)

    return tags.div(
        tags.input(id=id, type_=type_, name=id, checked=checked_),
        tags.label(label, for_=id),
        id=id,
        class_=squash_whitespace(f"ui {class_} checkbox"),
        **kwargs,
    )


def checkbox_group(
    id: str,
    label: str,
    choices: list[str],
    *,
    selected: Optional[Union[list[str], tuple[str], str]] = None,
    type: Optional[str] = None,
    position: Optional[str] = "grouped",
    class_: Optional[str] = None,
):
    if selected is None:
        selected = []
    if isinstance(selected, str):
        selected = [selected]

    if type == "radio" and len(selected) > 1:
        raise Exception("Radio buttons may have a maximum of 1 active value")

    checkbox_tags = TagList()
    for choice in choices:
        checkbox_tag = tags.div(
            checkbox(
                # NOTE: id of a particular checkbox inside a group doesn't play any role
                # in terms of Shiny reactivity.
                # However, since a chackbox input's "name" field is inferred from the id,
                # it is essential that they are the same throughout the group.
                id=f"{id}__group",
                label=choice,
                value=choice in selected,
                type=type,
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
