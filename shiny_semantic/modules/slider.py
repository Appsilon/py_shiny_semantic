import json
from typing import Optional

from htmltools import TagAttrArg, tags
from shiny._namespaces import resolve_id
from shiny.ui import input_slider

from shiny_semantic._utils import squash_whitespace


def slider(
    id: str,
    label: str,
    min_value: float,
    max_value: float,
    start_value: float,
    *,
    end_value: Optional[float] = None,
    step: Optional[float] = None,
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
