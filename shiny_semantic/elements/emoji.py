from typing import Optional

from shiny.ui import tags


def emoji(
    emoji_name: str,
    size: Optional[str] = "medium",
):
    return tags.em({"data-emoji": f":{emoji_name}:", "class": size})
