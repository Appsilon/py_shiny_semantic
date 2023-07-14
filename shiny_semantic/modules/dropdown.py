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
    """
    Generate a dropdown input component with customizable options.

    This function creates a dropdown input component based on Fomantic UI framework.
    The dropdown can be configured with various attributes like ID, available choices,
    selected value, placeholder, settings, and additional classes.

    Args:
        id (str): Identifier for the dropdown component. Should be unique within the page.
        choices (list[str]): List of string choices that populate the dropdown menu.
        value (Optional[Union[str, list[str]]], optional): Initially selected value(s).
            If a list of values is provided, they will be joined using commas.
        placeholder (Optional[str], optional): Placeholder text displayed when no item is selected.
        settings (Optional[dict], optional): Additional settings to configure the dropdown behavior.
        class_ (Optional[str], optional): Additional CSS class names to apply to the dropdown.

    Returns:
        str: A string representing the generated HTML for the dropdown component.

    Example:
        choices = ["Option 1", "Option 2", "Option 3"]
        settings = {"onChange": "handle_dropdown_change"}
        dropdown_html = dropdown(
          "myDropdown",
          choices,
          value = "Option 2",
          placeholder = "Select an option",
          settings = settings,
          class_ = "custom-dropdown"
        )
        print(dropdown_html)

    """
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
    """
    Generate an input select field with optional label and dropdown choices.

    This function generates an HTML input select field, commonly used for creating dropdown menus,
    with an optional label and specified choices. It returns the corresponding HTML representation
    of the input field.

    Args:
        id (str): Identifier for the input select field. Used to uniquely identify the field and its label.
        label (str, optional): Label for the input select field. If provided, it will be associated with the input field.
        choices (list[str]): List of strings representing the available options for the dropdown menu.
        selected (Union[str, list[str]], optional): Default selected option(s) in the dropdown. Can be a single option or a list of options.
        placeholder (str, optional): Placeholder text to display in the dropdown before a selection is made.
        settings (dict, optional): Additional settings to customize the behavior and appearance of the dropdown.
        class_ (str, optional): CSS class to apply to the input select field.

    Returns:
        str: A string representing the HTML representation of the input select field.

    Example:
        select_field = input_select(
            id = "color-select",
            label = "Select a Color",
            choices = ["Red", "Green", "Blue"],
            selected = "Green",
            placeholder = "Choose a color...",
            settings = {"searchable": True},
            class_ = "custom-select-field",
        )
        print(select_field)

    """
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
    """
    Update a select input in a session with new properties.

    This function is used to update the properties of a select input in a specified session. It allows modifying
    the label, available choices, and the selected option of the select input. The updated properties are sent to
    the session using the provided `Session` instance.

    Args:
        id (str): The unique identifier of the select input to be updated.
        label (str, optional): The label text to be displayed alongside the select input. Defaults to None.
        choices (list[str], optional): List of available choices for the select input. Defaults to None.
        selected (Union[str, list[str]], optional): The option(s) that should be selected in the select input.
            It can be a single value or a list of values. Defaults to None.
        session (Session, optional): The active session where the select input should be updated.
            If not provided, the function will attempt to use the currently active session.
            Defaults to None.

    Returns:
        None

    Example:
        session = create_session()
        update_select(
            id = "color_select",
            label = "Choose a color:",
            choices = ["Red", "Green", "Blue"],
            selected = "Green",
            session = session,
        )

    """
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
