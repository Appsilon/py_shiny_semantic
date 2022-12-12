from htmltools import HTMLDependency
from shiny.ui import TagList, tags


def button_dep():
    return HTMLDependency(
        name="semantic-button",
        version="2.5.0",
        source={"package": "shiny_semantic", "subdir": "www"},
        script=[{"src": "shiny-semantic-button.js"}],
    )


def input_action_button(input_id, label, type="default"):
    return TagList(
        button_dep(),
        tags.button({"id": input_id, "class_": f"ui {type} button"}, label),
    )
