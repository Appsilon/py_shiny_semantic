from typing import Optional

from shiny.ui import tags


def flag(
    country: str,
    class_name: Optional[str] = "",
):
    return tags.i(class_=f"{class_name} {country} flag")
