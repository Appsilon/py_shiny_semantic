from typing import Optional

from shiny.ui import tags


def divider(*args, class_name: Optional[str] = ""):
    return tags.div(*args, class_=f"ui {class_name} divider")
