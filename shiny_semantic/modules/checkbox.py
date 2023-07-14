from typing import Optional, Union

from htmltools import TagList, tags
from shiny.module import resolve_id
from shiny.session import Session, require_active_session

from shiny_semantic._utils import drop_none, squash_whitespace


def checkbox(
    id: str,
    label: str,
    value: bool = False,
    *,
    type: Optional[str] = None,
    name: Optional[str] = None,
    class_: Optional[str] = None,
    **kwargs,
):
    """
    Generate an HTML checkbox or radio input element with an associated label.

    This function creates an HTML checkbox or radio input element along with a label.
    The checkbox/radio input is associated with its label through the 'for' attribute,
    and can be customized with additional attributes and CSS classes.

    Args:
        id (str): The unique identifier for the input element. Will also be used to generate
            the 'for' attribute in the associated label.
        label (str): The text label that will be displayed next to the checkbox/radio input.
        value (bool, optional): The initial state of the checkbox/radio input. Defaults to False.
        type (str, optional): The type of input element. Use 'radio' for radio buttons.
        name (str, optional): The name attribute for the input element. Defaults to the id value.
        class_ (str, optional): Additional CSS classes to apply to the input element.
        **kwargs: Additional keyword arguments that will be added as attributes to the generated
            <div> element containing the checkbox/radio input and label.

    Returns:
        str: A string representing the generated HTML structure.

    Example:
        checkbox_element = checkbox(
          "checkbox1",
          "Enable feature",
          value = True,
          class_ = "highlight"
        )
        print(checkbox_element)

    """
    class_ = f"{class_ or ''}"
    if value:
        class_ = f"{class_} checked"
    if type is not None:
        class_ = f"{class_} {type}"

    input_tag_type = "checkbox"
    if type == "radio":
        input_tag_type = "radio"

    # NOTE: if the value=False, let checked_ be None, i.e. not appear in HTML
    checked = "" if value else None

    id = resolve_id(id)
    name = name or id

    return tags.div(
        tags.input(id=id, type_=input_tag_type, name=name, checked=checked),
        tags.label(label, for_=id),
        id=id,
        class_=squash_whitespace(f"ui {class_} checkbox"),
        **kwargs,
    )


def checkbox_group(
    id: str,
    label: str,
    choices: Union[list[str], dict[str, str]],
    *,
    selected: Optional[Union[list[str], tuple[str], str]] = None,
    type: Optional[str] = None,
    position: Optional[str] = "grouped",
    class_: Optional[str] = None,
):
    """
    Generate a group of checkboxes with a common label and layout.

    This function generates a group of checkboxes, allowing users to select one or
    more options. It creates a styled UI form for the checkboxes with a common label.
    
    Args:
        id (str): Unique identifier for the checkbox group.
        label (str): The label text displayed above the checkbox group.
        choices (Union[list[str], dict[str, str]]): Choices available for selection. It can be a list of strings
            or a dictionary with keys as values and values as labels.
        selected (Optional[Union[list[str], tuple[str], str]]): Initially selected options. It can be a list of
            strings, a tuple of strings, or a single string. Defaults to an empty list.
        type (Optional[str]): Type of checkboxes. Possible values are "radio" or None (for regular checkboxes).
            Defaults to None.
        position (Optional[str]): Positioning style of the checkboxes within the group. Possible values are
            "grouped" or "inline". Defaults to "grouped".
        class_ (Optional[str]): Additional CSS class to be applied to the checkbox group container. Defaults to None.

    Returns:
        str: A string representing the HTML structure of the generated checkbox group.

    Raises:
        Exception: If type is "radio" and multiple options are selected, as radio buttons only allow one active value.

    Example:
        choices = {"option1": "Option 1", "option2": "Option 2", "option3": "Option 3"}
        selected_options = ["option1", "option3"]
        checkbox_group_html = checkbox_group(
          "group1",
          "Select Options",
          choices,
          selected = selected_options,
          type = "radio"
        )
        print(checkbox_group_html)

    """
    if isinstance(choices, list):
        choices = {choice: choice for choice in choices}

    if selected is None:
        selected = []
    if isinstance(selected, str):
        selected = [selected]

    if type == "radio" and len(selected) > 1:
        raise Exception("Radio buttons may have a maximum of 1 active value")

    checkbox_tags = TagList()
    for v, l in choices.items():
        checkbox_tag = tags.div(
            checkbox(
                # NOTE: for checkbox_group to work correctly, all individual checkboxes
                # inside it must share a common name attribute.
                id=f"{id}__{v}",
                label=l,
                value=v in selected,
                type=type,
                name=id,
                data_shiny_value=v,
            ),
            class_="field",
        )
        checkbox_tags.append(checkbox_tag)

    id = resolve_id(id)
    class_ = squash_whitespace(f"{position} {class_ or ''} fields ss-checkbox-group")

    return tags.div(
        tags.div(
            tags.label(label),
            checkbox_tags,
            id=id,
            class_=class_,
        ),
        class_="ui form",
    )


def update_checkbox(
    id: str,
    *,
    label: Optional[str] = None,
    value: Optional[bool] = None,
    session: Optional[Session] = None,
):
    """
    Update a checkbox input widget in a Shiny application session.

    This function updates the properties of a checkbox input widget in a Shiny application
    session. It allows modifying the label and value properties of the checkbox, facilitating
    dynamic updates to the widget's appearance and state during the Shiny app's execution.

    Args:
        id (str): The unique identifier of the checkbox input widget to be updated.
        label (str, optional): New label text for the checkbox. If not provided, the label remains unchanged.
        value (bool, optional): New value for the checkbox (True or False). If not provided, the value remains unchanged.
        session (Session, optional): The Shiny application session to which the checkbox belongs.
                                    If not provided, an active session is required and will be obtained.

    Returns:
        None

    Example:
        # Assuming 'checkbox_id' is the identifier of the checkbox in the Shiny app
        update_checkbox(
          checkbox_id,
          label = "Updated Label",
          value = True,
          session = my_session
        )

    """
    session = require_active_session(session)
    msg = {"label": label, "value": value}
    session.send_input_message(id, drop_none(msg))


def update_checkbox_group(
    id: str,
    *,
    labels: Optional[list[str]] = None,
    values: Optional[list[bool]] = None,
    group_label: Optional[str] = None,
    session: Optional[Session] = None,
):
    """
    Update a checkbox group input element in a Shiny app session.

    This function sends an input message to update the state of a checkbox group
    input element identified by its 'id' in a Shiny app session. The 'labels' argument
    provides the text labels for the checkboxes, the 'values' argument provides the
    corresponding boolean values indicating whether each checkbox is checked or not,
    and 'group_label' is an optional label for the entire group of checkboxes.

    Args:
        id (str): The identifier of the checkbox group input element.
        labels (List[str], optional): List of text labels for the checkboxes. Default is None.
        values (List[bool], optional): List of boolean values indicating checkbox states. Default is None.
        group_label (str, optional): Optional label for the entire group of checkboxes. Default is None.
        session (Session, optional): The Shiny app session to which the update message will be sent.
            If not provided, an active session is required. Default is None.

    Returns:
        None

    Example:
        # Assume 'my_session' is an active Shiny app session.
        checkbox_labels = ["Option 1", "Option 2", "Option 3"]
        checkbox_values = [True, False, True]
        update_checkbox_group(
            id = "my_checkbox_group",
            labels = checkbox_labels,
            values = checkbox_values,
            group_label = "Select Options",
            session = my_session,
        )

    """
    session = require_active_session(session)
    msg = {"labels": labels, "values": values, "group_label": group_label}
    session.send_input_message(id, drop_none(msg))
