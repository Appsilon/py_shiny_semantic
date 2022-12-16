from shiny_semantic import page_semantic

from .helpers import hero
from .modules import (
    button_module,
    emoji_module,
    flag_module,
    header_module,
    icon_module,
)

app_ui = page_semantic(
    hero(),
    button_module.ui("button_section"),
    emoji_module.ui("emoji_section"),
    flag_module.ui("flag_section"),
    header_module.ui("header_section"),
    icon_module.ui("icon_section"),
    title="Example: Buttons",
)


def app_server(input, output, session):
    button_module.server("button_section")
    emoji_module.server("emoji_section")
    flag_module.server("flag_section")
    header_module.server("header_section")
    icon_module.server("icon_section")