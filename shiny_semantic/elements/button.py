from shiny.ui import tags

from ..typings import ButtonType


def button(
    input_id: str,
    label: str,
    type: ButtonType = ButtonType.default,
    is_basic: bool = False,
):
    basic = "basic" if is_basic else ""
    classname = f"ui {type.value} {basic} button "

    return tags.button(
        {
            "id": input_id,
            "class": classname,
        },
        label,
    )
