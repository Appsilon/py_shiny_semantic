from typing import Optional

from htmltools import TagAttrArg, TagChildArg, tags

from shiny_semantic._utils import squash_whitespace

# TODO: there are two header options implemented in Semantic UI:
# as a heading (h1, h2, etc) and as a div. The former scales in rems
# while the latter in ems. It is easier to implement the latter, since
# no overloads or conditionals will be required, but we should think
# whether it makes sense to leave only this option.


def header(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    return tags.div(
        *children,
        class_=squash_whitespace(f"ui {class_ or ''} header"),
        **kwargs,
    )


def subheader(
    *children: TagChildArg,
    class_: Optional[str] = None,
    **kwargs: TagAttrArg,
):
    return tags.div(
        *children,
        class_=squash_whitespace(f"{class_ or ''} sub header"),
        **kwargs,
    )
