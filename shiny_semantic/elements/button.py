from typing import Optional

import shiny
from shiny.session import Session, require_active_session
from shiny.ui import tags

shiny.ui.update_action_button


def button(
    input_id: str,
    label: str,
    *args,
    icon_name: Optional[str] = None,
    class_name: Optional[str] = None,
):
    icon = icon_name and tags.i(class_=f"{icon_name} icon")
    class_ = f"ui {class_name or ''} button"

    return tags.div(
        icon,
        label,
        *args,
        id=input_id,
        class_=class_,
    )


def _drop_none(x) -> dict[str, object]:
    return {k: v for k, v in x.items() if v is not None}


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
    session.send_input_message(input_id, _drop_none(msg))
