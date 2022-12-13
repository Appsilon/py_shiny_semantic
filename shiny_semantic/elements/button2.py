from shiny.ui import tags

from ..typings import ButtonColor, ButtonFill, ButtonSize, ButtonType


def button(
    input_id: str,
    label: str = "",
    icon_name: str = "",
    type: ButtonType = ButtonType.default,
    fill: ButtonFill = ButtonFill.solid,
    color: ButtonColor = ButtonColor.default,
    size: ButtonSize = ButtonSize.default,
):

    icon = None
    button_icon_class = ""

    if icon_name != "":
        icon = tags.i(class_=f"{icon_name} icon")
        button_icon_class = "icon"

    classname = (
        f"{size.value} ui {color.value} "
        f"{fill.value} {button_icon_class} "
        f"{type.value} button "
    )

    return tags.button(
        {
            "id": input_id,
            "class": classname,
        },
        icon,
        label,
    )
