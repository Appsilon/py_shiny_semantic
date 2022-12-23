from typing import Optional

from htmltools import TagAttrArg, tags

from shiny_semantic._utils import squash_whitespace


def flag(country: str, *, class_: Optional[str] = None, **kwargs: TagAttrArg):
    return tags.i(
        class_=squash_whitespace(f"{class_ or ''} {country} flag"),
        **kwargs,
    )
