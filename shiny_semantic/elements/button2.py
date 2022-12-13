from typing import Optional

from shiny.ui import tags


def button2(
    input_id: str,
    label: str,
    *args,
    icon_name: Optional[str] = None,
    class_name: Optional[str] = None,
):
    icon = icon_name and tags.i(class_=f"{icon_name} icon")
    class_ = f"ui {class_name or ''} button"

    return tags.div(
        icon,
        label,
        *args,
        id=input_id,
        class_=class_,
    )
