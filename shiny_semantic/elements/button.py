from shiny.ui import tags

from ..typings import ButtonColor, ButtonFill, ButtonType


def button(
    input_id: str,
    label: str,
    type: ButtonType = ButtonType.default,
    fill: ButtonFill = ButtonFill.solid,
    color: ButtonColor = ButtonColor.default,
):
    classname = f"ui {color.value} {fill.value} {type.value} button "

    return tags.button(
        {
            "id": input_id,
            "class": classname,
        },
        label,
    )
