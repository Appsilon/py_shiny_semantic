import json
from typing import Optional

from htmltools import TagChildArg, TagList, tags
from shiny._namespaces import resolve_id

from shiny_semantic._utils import squash_whitespace


def selection(
    id: str,
    label: TagChildArg,
    options: list[str],
    *,
    class_: Optional[str] = None,
    settings: Optional[dict] = None,
):
    option_tags = TagList()
    for option in options:
        option_tags.append(tags.option(option))

    class_name = squash_whitespace(
        f"ui {class_ or ''} selection dropdown semantic-select-input"
    )

    return tags.select(
        option_tags,
        id=resolve_id(id),
        class_=class_name,
        data_settings=json.dumps(settings),
    )
