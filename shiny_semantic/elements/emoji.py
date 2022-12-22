from typing import Optional

from htmltools import TagAttrArg, tags


def emoji(emoji_name: str, **kwargs: TagAttrArg):
    return tags.em(data_emoji=f":{emoji_name}:", **kwargs)
