import re
from typing import Dict, Optional

from htmltools import Tag, TagAttrArg, TagChildArg, tags
from shiny.module import resolve_id
from shiny.session import Session, require_active_session

from shiny_semantic._utils import squash_whitespace
from shiny_semantic.elements import button


def modal(
    id: str,
    *,
    header: TagChildArg,
    content: TagChildArg,
    actions: Optional[TagChildArg] = None,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate a modal dialog HTML element.

    This function creates a modal dialog element typically used in web applications to display
    additional content, alerts, or prompts on top of the main content. The modal consists of a
    header, content, and optional actions.

    Args:
        id (str): Identifier for the modal element.
        header (TagChildArg): HTML content for the modal header.
        content (TagChildArg): HTML content for the modal body.
        actions (Optional[TagChildArg], optional): HTML content for the modal actions section.
            Defaults to None. If not provided, default "Cancel" and "OK" buttons will be included.
        class_ (Optional[str], optional): Additional CSS classes to be applied to the modal element.
        **kwargs (TagAttrArg): Additional HTML attributes to be applied to the modal element.

    Returns:
        str: A string representing the generated modal dialog HTML element.

    Example:
        modal_element = modal(
            id = "my-modal",
            header = tags.h2("Modal Header"),
            content = tags.p("Modal content goes here."),
            actions = tags.button("confirm", "Confirm", class_ = "positive"),
            class_ = "custom-modal",
            style = "width: 400px;",
        )
        print(modal_element)
    """
    modal_header = tags.div(header, class_="header")
    modal_content = tags.div(content, class_="content")
    modal_actions = (
        tags.div(actions, class_="actions")
        if actions
        else tags.div(
            button("cancel", "Cancel", class_="negative"),
            button("ok", "OK", class_="positive"),
            class_="actions",
        )
    )

    _assert_modal_actions(modal_actions)

    modal = tags.div(
        modal_header,
        modal_content,
        modal_actions,
        id=resolve_id(id),
        class_=squash_whitespace(f"ui {class_ or ''} modal"),
        **kwargs,
    )

    return modal


async def modal_show(
    modal_ui: Tag,
    modal_props: Optional[Dict] = None,
    shiny_input: str = "modal",
    session: Optional[Session] = None,
):
    """
    Display a semantic modal dialog in a Shiny app.

    This asynchronous function sends a custom message to the active Shiny session to
    display a modal dialog with the provided UI content and optional properties.

    Args:
        modal_ui (Tag): The HTML content representing the UI of the modal dialog.
        modal_props (dict, optional): Optional properties to customize the modal behavior.
            Default is None.
        shiny_input (str, optional): The Shiny input identifier for the modal dialog.
            Default is "modal".
        session (Session, optional): The Shiny session object. If not provided,
            the function will attempt to obtain the active session.

    Returns:
        None

    Example:
        modal_content = tags.div(tags.h2("Modal Title"), tags.p("Modal content goes here."))
        modal_show(modal_content, modal_props = {"size": "large"})

    """
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
    """
    Assert the presence of specific button classes in a modal's action UI.

    This function checks if a provided Tag containing modal action UI has at least one button
    with the required classes: 'approve', 'positive', 'deny', or 'negative'. If none of these
    classes are found, an Exception is raised.

    Args:
        actions_ui (Tag): Tag containing the HTML representation of modal action UI.

    Raises:
        Exception: If none of the required button classes are found in the provided Tag.

    Example:
        actions = tags.div(
            tags.button("Approve", class_ = "approve"),
            tags.button("Cancel", class_ = "negative")
        )
        _assert_modal_actions(actions)

    """
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
