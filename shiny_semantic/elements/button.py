from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags
from shiny.module import resolve_id
from shiny.session import Session, require_active_session

from shiny_semantic._utils import drop_none, squash_whitespace


def button(
    id: str,
    label: Optional[str] = None,
    *,
    icon: TagChildArg = None,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    class_name = f"ui {class_ or ''} button"

    return tags.button(
        icon,
        label,
        id=resolve_id(id),
        class_=squash_whitespace(class_name),
        **kwargs,
    )


def update_button(
    input_id: str,
    *,
    label: Optional[str] = None,
    icon_name: Optional[str] = None,
    session: Optional[Session] = None,
):
    session = require_active_session(session)
    msg = {
        "label": label,
        "icon": icon_name,
    }
    session.send_input_message(input_id, drop_none(msg))
