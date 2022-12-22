from typing import Optional

from htmltools import TagAttrArg, tags

from shiny_semantic._utils import squash_whitespace


def icon(
    icon_name: str,
    *,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    return tags.i(
        class_=squash_whitespace(f"{class_ or ''} {icon_name} icon"),
        **kwargs,
    )
