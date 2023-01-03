import json
from typing import Optional, Union

from htmltools import tags
from shiny.module import resolve_id
from shiny.session import Session, require_active_session

from shiny_semantic._utils import drop_none, squash_whitespace
from shiny_semantic.elements import icon


def dropdown(
    id: str,
    choices: list[str],
    *,
    value: Optional[Union[str, list[str]]] = None,
    placeholder: Optional[str] = None,
    settings: Optional[dict] = None,
    class_: Optional[str] = None,
):
    choice_tags = [
        tags.div(
            choice,
            class_="item",
            data_value=choice,
        )
        for choice in choices
    ]

    class_name = squash_whitespace(f"ui {class_ or ''} selection dropdown semantic-select-input")

    id = resolve_id(id)

    if isinstance(value, list):
        value = ",".join(value)

    # NOTE: This HTML structure represents the Fomantic-recomended way of creating this component
    # See: https://fomantic-ui.com/modules/dropdown.html#/usage
    return tags.div(
        tags.input(type_="hidden", name=id, value=value),
        icon("dropdown"),
        tags.div(placeholder, class_="default text"),
        tags.div(*choice_tags, class_="menu"),
        id=id,
        class_=class_name,
        data_settings=json.dumps(settings),
    )


def input_select(
    id: str,
    label: Optional[str],
    choices: list[str],
    *,
    selected: Optional[Union[str, list[str]]] = None,
    placeholder: Optional[str] = None,
    settings: Optional[dict] = None,
    class_: Optional[str] = None,
):
    id = resolve_id(id)
    return tags.div(
        tags.div(
            # NOTE: label tag is inspired by the way it is implemented in Shiny.
            # See: `from shiny.ui._utils import shiny_input_label`
            tags.label(label, id=f"{id}-label", for_=id),
            dropdown(
                id,
                choices,
                value=selected,
                placeholder=placeholder,
                settings=settings,
                class_=class_,
            ),
            class_="field",
        ),
        class_="ui form",
    )


def update_select(
    id: str,
    *,
    label: Optional[str] = None,
    choices: Optional[list[str]] = None,
    selected: Optional[Union[str, list[str]]] = None,
    session: Optional[Session] = None,
):
    session = require_active_session(session)

    msg_choices = None
    if choices is not None:
        msg_choices = {
            "values": [{"value": choice, "text": choice, "name": choice} for choice in choices]
        }

    msg = {
        "label": label,
        "choices": msg_choices,
        "value": selected,
    }

    session.send_input_message(id, drop_none(msg))
