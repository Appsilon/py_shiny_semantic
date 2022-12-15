from typing import Optional

from shiny.ui import tags


def container(*args, class_name: Optional[str] = ""):
    return tags.div(*args, class_=f"ui {class_name} container")
