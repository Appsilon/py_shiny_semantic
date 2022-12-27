import json
from typing import Optional

from htmltools import TagChildArg, TagList, tags
from shiny._namespaces import resolve_id
from shiny._utils import drop_none
from shiny.session import Session, require_active_session

from shiny_semantic._utils import squash_whitespace
from shiny_semantic.elements import icon

# NOTE: attempt to follow Shiny API conventions


def input_select(
    id: str,
    label: Optional[str],
    choices: list[str],
    *,
    placeholder: Optional[str] = None,
    settings: Optional[dict] = None,
    class_: Optional[str] = None,
):
    choice_tags = TagList()
    for choice in choices:
        choice_tags.append(tags.div(choice, class_="item", data_value=choice))

    class_name = squash_whitespace(
        f"ui {class_ or ''} selection dropdown semantic-select-input"
    )

    id = resolve_id(id)

    return tags.div(
        tags.div(
            tags.label(label, id=f"{id}-label", for_=id),
            tags.div(
                tags.input(type_="hidden", name=id),
                icon("dropdown"),
                tags.div(placeholder, class_="default text"),
                tags.div(choice_tags, class_="menu"),
                id=id,
                class_=class_name,
                data_settings=json.dumps(settings),
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
    value: Optional[str] = None,
    session: Optional[Session] = None,
):
    session = require_active_session(session)

    msg_choices = None
    if choices is not None:
        msg_choices = {
            "values": [
                {"value": choice, "text": choice, "name": choice} for choice in choices
            ]
        }

    msg = {
        "label": label,
        "choices": msg_choices,
        "value": value,
    }

    session.send_input_message(id, drop_none(msg))
