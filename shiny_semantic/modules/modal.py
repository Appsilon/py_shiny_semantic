from typing import Dict, Optional

from shiny._namespaces import resolve_id
from shiny.session import Session, require_active_session
from shiny.ui import TagChildArg, tags

from shiny_semantic.elements import button


def modal(
    id: str,
    header: TagChildArg,
    content: TagChildArg,
    actions: Optional[TagChildArg] = None,
    class_name: Optional[str] = None,
):
    modal_header = tags.div(header, class_="header")
    modal_content = tags.div(content, class_="content")
    modal_actions = (
        tags.div(actions, class_="actions")
        if actions
        else tags.div(
            button("cancel", "Cancel", class_name="negative"),
            button("ok", "OK", class_name="positive"),
            class_="actions",
        )
    )

    modal = tags.div(
        modal_header,
        modal_content,
        modal_actions,
        id=resolve_id(id),
        class_=f"ui {class_name} modal" if class_name else "ui modal",
    )

    return modal


async def modal_show(
    modal_ui,
    modal_props: Optional[Dict] = None,
    shiny_input: str = "modal",
    session: Optional[Session] = None,
):
    session = require_active_session(session)

    await session.send_custom_message(
        "showSemanticModal",
        {
            "ui": str(modal_ui),
            "props": modal_props,
            "shiny_input": session.ns(shiny_input),
        },
    )
