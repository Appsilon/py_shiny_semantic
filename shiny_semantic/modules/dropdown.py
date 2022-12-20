import json
from typing import Optional

from shiny._namespaces import resolve_id
from shiny.ui import TagList, tags


def selection(
    input_id: str,
    options: list[str],
    class_name: Optional[str] = None,
    settings: Optional[dict] = None,
):
    option_tags = TagList()
    for option in options:
        option_tags.append(tags.option(option))

    class_ = (
        "ui selection dropdown semantic-select-input"
        if class_name is None
        else f"ui {class_name} selection dropdown semantic-select-input"
    )

    return tags.select(
        option_tags,
        id=resolve_id(input_id),
        class_=class_,
        data_settings=json.dumps(settings),
    )
