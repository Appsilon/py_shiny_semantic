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
    """
    Generate an HTML button element with optional icon and attributes.

    This function generates an HTML button element with various customization options,
    including providing an icon, setting CSS classes, and adding additional attributes.

    Args:
        id (str): The unique identifier for the button.
        label (str, optional): The text label to display on the button. If not provided, the button will be icon-only.
        icon (TagChildArg, optional): An HTML element representing an icon to be displayed on the button.
        class_ (str, optional): Additional CSS classes to be applied to the button element.
        **kwargs (TagAttrArg): Additional attributes to be added to the button element.

    Returns:
        str: A string representing the generated HTML button element.

    Example:
        # Creating a button with text label
        button_with_label = button("my_button", label="Click Me", class_="primary", onclick="handle_click()")

        # Creating an icon-only button
        icon_element = tags.i(class_="fas fa-search")
        icon_button = button("search_button", icon=icon_element, class_="icon-button")

    """
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
    """
    Update a button in an active session.

    This function updates the properties of a button element in a given active session.
    The input_id is used to identify the specific button element to be updated. The label
    and icon_name arguments can be provided to change the label text and icon of the button,
    respectively.

    Args:
        input_id (str): The ID of the button element to be updated.
        label (str, optional): The new label text for the button. If not provided, the label remains unchanged.
        icon_name (str, optional): The name of the icon to be displayed on the button. If not provided,
            the icon remains unchanged.
        session (Session, optional): An active session instance in which the button is located.
            If not provided, the function attempts to use the default active session.

    Returns:
        None

    Example:
        update_button(
          "my_button",
          label = "Click Me",
          icon_name = "icon-check",
          session = session
        )

    """
    session = require_active_session(session)
    msg = {
        "label": label,
        "icon": icon_name,
    }
    session.send_input_message(input_id, drop_none(msg))
