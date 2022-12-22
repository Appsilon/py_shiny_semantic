from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace


def container(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    return tags.div(
        *children,
        class_=squash_whitespace(f"ui {class_ or ''} container"),
        **kwargs,
    )
