from shiny.ui import tags

from ..typings import ButtonColor, ButtonFill, ButtonSize, ButtonType


def button(
    input_id: str,
    label: str,
    type: ButtonType = ButtonType.default,
    fill: ButtonFill = ButtonFill.solid,
    color: ButtonColor = ButtonColor.default,
    size: ButtonSize = ButtonSize.default,
):
    classname = (
        f"{size.value} ui {color.value} {fill.value} {type.value} button "
    )

    return tags.button(
        {
            "id": input_id,
            "class": classname,
        },
        label,
    )
