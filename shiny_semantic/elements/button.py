from shiny.ui import tags

from ..typings import ButtonType


def button(
    input_id: str,
    label: str,
    type: ButtonType = ButtonType.default,
):
    classname = f"ui {type.value} button "

    return tags.button(
        {
            "id": input_id,
            "class": classname,
        },
        label,
    )
