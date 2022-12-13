from typing import Optional

from shiny.session import Session, require_active_session
from shiny.ui import tags


def button(
    input_id: str,
    label: Optional[str] = None,
    *args,
    icon_name: Optional[str] = None,
    class_name: Optional[str] = None,
):
    icon = icon_name and tags.i(class_=f"{icon_name} icon")
    class_ = f"ui {class_name or ''} button"

    return tags.button(
        icon,
        label,
        *args,
        id=input_id,
        class_=class_,
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
    session.send_input_message(input_id, _drop_none(msg))


def _drop_none(x) -> dict[str, object]:
    return {k: v for k, v in x.items() if v is not None}
