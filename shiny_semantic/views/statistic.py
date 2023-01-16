from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace


def statistic(
    value: TagChildArg,
    label: str,
    *,
    value_first=True,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    value_element = tags.div(value, class_="value")
    label_element = tags.div(label, class_="label")

    content = [label_element, value_element]

    if value_first:
        content.reverse()

    return tags.div(
        *content,
        class_=squash_whitespace(f"ui {class_ or ''} statistic"),
        **kwargs,
    )
