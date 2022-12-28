import json
from typing import Optional, Union

from htmltools import TagAttrArg, tags
from shiny._namespaces import resolve_id
from shiny._utils import drop_none
from shiny.session import Session, require_active_session

from shiny_semantic._utils import squash_whitespace


def slider(
    id: str,
    label: str,
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
    if isinstance(value, (int, float)):
        value = [value]

    session = require_active_session(session)
    msg = {"value": value}
    print(msg)
    session.send_input_message(id, drop_none(msg))
