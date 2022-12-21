from shiny_semantic import page_semantic

from .helpers import hero
from .modules import button_module, emoji_module

app_ui = page_semantic(
    hero(),
    button_module.ui("button_section"),
    emoji_module.ui("emoji_section"),
    title="Example: Buttons",
)


def app_server(input, output, session):
    emoji_module.server("emoji_section")
    button_module.server("button_section")
