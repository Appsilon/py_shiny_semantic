from typing import Optional

from shiny.ui import tags


def emoji(
    emoji_name: str,
    class_name: Optional[str] = "medium",
):
    return tags.em({"data-emoji": f":{emoji_name}:", "class": class_name})
