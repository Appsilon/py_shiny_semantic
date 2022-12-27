import json
from typing import Optional

from htmltools import TagChildArg, TagList, tags
from shiny._namespaces import resolve_id
from shiny._utils import drop_none
from shiny.session import Session, require_active_session

from shiny_semantic._utils import squash_whitespace
from shiny_semantic.elements import icon


def selection(
    id: str,
    label: TagChildArg,
    choices: list[str],
    *,
    class_: Optional[str] = None,
    settings: Optional[dict] = None,
):
    choice_tags = TagList()
    for choice in choices:
        choice_tags.append(tags.div(choice, class_="item", data_value=choice))

    class_name = squash_whitespace(
        f"ui {class_ or ''} selection dropdown semantic-select-input"
    )

    return tags.div(
        tags.input(type_="hidden", name=resolve_id(id)),
        icon("dropdown"),
        tags.div("Placeholder", class_="default text"),  # TODO: replace placeholder
        tags.div(choice_tags, class_="menu"),
        id=resolve_id(id),
        class_=class_name,
        data_settings=json.dumps(settings),
    )


def update_selection(
    id: str,
    *,
    label: Optional[str] = None,
    choices: Optional[list[str]] = None,
    value: Optional[str] = None,
    session: Optional[Session] = None,
):
    session = require_active_session(session)

    msg_values = None
    if choices is not None:
        msg_values = [
            {"value": choice, "text": choice, "name": choice} for choice in choices
        ]

    msg = {
        "label": label,
        "choices": {"values": msg_values},
        "value": value,
    }

    print(msg)

    session.send_input_message(id, drop_none(msg))
