import json
from typing import Optional, Union

from htmltools import TagAttrArg, tags
from shiny.module import resolve_id
from shiny.session import Session, require_active_session

from shiny_semantic._utils import drop_none, squash_whitespace


def slider(
    id: str,
    # TODO: add `label: str` argument
    min_value: Union[float, int],
    max_value: Union[float, int],
    start_value: Union[float, int],
    *,
    end_value: Optional[Union[float, int]] = None,
    step: Optional[Union[float, int]] = None,
    show_labels: bool = True,
    show_ticks: bool = False,
    custom_labels: Optional[list[str]] = None,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """
    Generate an interactive slider element in HTML.

    This function generates an HTML div element representing an interactive slider. The slider
    can be used to select a single value or a range of values, depending on the parameters provided.
    The appearance of the slider, including labels and ticks, can be customized through the function
    arguments.

    Args:
        id (str): Unique identifier for the slider element.
        label (str): Label text to describe the purpose of the slider.
        min_value (Union[float, int]): The minimum value of the slider.
        max_value (Union[float, int]): The maximum value of the slider.
        start_value (Union[float, int]): The initial value of the slider.
        end_value (Optional[Union[float, int]], optional): The end value for a range slider.
        step (Optional[Union[float, int]], optional): The step value for the slider.
        show_labels (bool, optional): Whether to show labels for slider values (default is True).
        show_ticks (bool, optional): Whether to show ticks for slider values (default is False).
        custom_labels (Optional[list[str]], optional): Custom labels for specific values.
        class_ (Optional[str], optional): Additional CSS classes for styling the slider div.
        **kwargs (TagAttrArg): Additional keyword arguments for HTML attributes.

    Returns:
        str: A string representing the generated HTML div element for the slider.

    Example:
        slider_element = slider(
            id = "my-slider",
            label = "Select a value:",
            min_value = 0,
            max_value = 100,
            start_value = 50,
            step = 5,
            show_labels = True,
            show_ticks = True,
            custom_labels = ["Low", "Medium", "High"],
            class_ = "custom-slider",
        )
        print(slider_element)

    """

    class_ = class_ or ""

    if show_labels:
        class_ = f"{class_} labeled"

    if show_ticks:
        class_ = f"{class_} ticked"

    if end_value is not None:
        class_ = f"{class_} range"

    return tags.div(
        id=resolve_id(id),
        class_=squash_whitespace(f"ui {class_} slider ss-slider"),
        data_min_=min_value,
        data_max=max_value,
        data_start=start_value,
        data_end=end_value,
        data_step=step,
        data_labels=json.dumps(custom_labels),
        **kwargs,
    )


def update_slider(
    id: str,
    *,
    value: Union[int, float, list[float], list[int]],
    session: Optional[Session] = None,
):
    """
    Update the value of a slider widget in a session.

    This function is used to update the value of a slider widget identified by its ID
    in a session. The new value can be a single integer or float, or a list of integers
    or floats, depending on the slider configuration.

    Args:
        id (str): The ID of the slider widget to be updated.
        value (Union[int, float, list[float], list[int]]): The new value(s) for the slider.
            If a single value is provided, it will be converted to a list.
        session (Optional[Session], optional): The session object in which the slider exists.
            If not provided, an active session is required.

    Returns:
        None

    Example:
        # Assuming 'my_session' is a valid session object and 'slider_id' is the ID of the slider to update
        new_value = 25
        update_slider(slider_id, value = new_value, session = my_session)

    """
    if isinstance(value, (int, float)):
        value = [value]

    session = require_active_session(session)
    msg = {"value": value}
    session.send_input_message(id, drop_none(msg))
