from typing import Optional

from shiny._namespaces import resolve_id
from shiny.ui import tags


def text_input(input_id: str, placeholder: Optional[str] = ""):
    return tags.div(
        tags.input(
            type="text",
            placeholder=placeholder,
            id=resolve_id(input_id),
        ),
        class_="ui input",
    )
