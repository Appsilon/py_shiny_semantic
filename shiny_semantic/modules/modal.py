import re
from typing import Dict, Optional

from htmltools import Tag
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

    _assert_modal_actions(modal_actions)

    modal = tags.div(
        modal_header,
        modal_content,
        modal_actions,
        id=resolve_id(id),
        class_=f"ui {class_name} modal" if class_name else "ui modal",
    )

    return modal


async def modal_show(
    modal_ui: Tag,
    modal_props: Optional[Dict] = None,
    shiny_input: str = "modal",
    session: Optional[Session] = None,
):
    session = require_active_session(session)

    await session.send_custom_message(
        type="showSemanticModal",
        message={
            "ui": str(modal_ui),
            "props": modal_props,
            "shiny_input": session.ns(shiny_input),
        },
    )


def _assert_modal_actions(actions_ui: Tag):
    match_approve = re.search("<button.*class=.*(approve).*>", str(actions_ui))
    match_positive = re.search("<button.*class=.*(positive).*>", str(actions_ui))
    match_deny = re.search("<button.*class=.*(deny).*>", str(actions_ui))
    match_negative = re.search("<button.*class=.*(negative).*>", str(actions_ui))

    if any([match_approve, match_positive, match_deny, match_negative]):
        return

    raise Exception(
        """Modal actions has to have at least one button with one
        of the following classes: positive, negative, approve, deny."""
    )
