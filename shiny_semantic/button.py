from shiny.ui import tags


def input_action_button(input_id, label, type="default"):
    return tags.button({"id": input_id, "class_": f"ui {type} button"}, label)
