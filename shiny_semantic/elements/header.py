from typing import Optional

from shiny.ui import tags

# TODO: there are two header options implemented in Semantic UI:
# as a heading (h1, h2, etc) and as a div. The former scales in rems
# while the latter in ems. It is easier to implement the latter, since
# no overloads or conditionals will be required, but we should think
# whether it makes sense to leave only this option.


def header(*args, class_name: Optional[str] = ""):
    return tags.div(*args, class_=f"ui {class_name} header")


def subheader(*args):
    return tags.div(*args, class_="sub header")
