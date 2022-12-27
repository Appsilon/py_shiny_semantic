from typing import Optional

from htmltools import TagAttrArg, tags


def emoji(emoji_name: str, *, class_: Optional[str] = None, **kwargs: TagAttrArg):
    return tags.em(data_emoji=f":{emoji_name}:", class_=class_, **kwargs)
