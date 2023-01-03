from typing import Optional, Union

from htmltools import TagAttrArg, TagChildArg, tags
from shiny.module import resolve_id

from shiny_semantic._utils import squash_whitespace


def semantic_input(
    id: str,
    # FIXME: adding label param to match Shiny API.
    # Should be revised -- is probably resolved, when
    # a shiny-like `shiny_semantic.elements.input_text()`
    # is created.
    label=None,
    value: Union[str, float] = "",
    *,
    placeholder: Optional[str] = "",
    icon: TagChildArg = None,
    type: str = "text",
    semantic_class: Optional[str] = None,
    semantic_label: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    """Keword arguments (**kwargs) include all html attributes
    relevant to the input tag, including, for example, `min`, `max` and `step`
    in case of input type="number", as well as `class_` that is passed directly
    to the input tag, as opposed to the `semantic_class` that is passed to the
    enclosing div element.
    """
    # Enclosing div's class
    if semantic_class is None:
        semantic_class = ""

    # Modify the enclosing div's class if icon is passed
    if icon is not None:
        semantic_class += " icon"

    # Define the label
    label_tag = None
    if semantic_label is not None:
        label_tag = tags.div(semantic_label, class_="ui label")
        semantic_class += " labeled"

    # Finalize & clean the div's class
    semantic_class = squash_whitespace(f"ui {semantic_class} input")

    return tags.div(
        label_tag,
        tags.input(
            id=resolve_id(id),
            type=type,
            value=value,
            placeholder=placeholder,
            **kwargs,
        ),
        icon,
        class_=semantic_class,
    )
