from typing import Optional

from shiny.ui import tags


def icon(icon_name: str, class_name: Optional[str] = ""):
    return tags.i(class_=f"{class_name} {icon_name} icon")
