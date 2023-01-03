from typing import Any, Dict


def squash_whitespace(txt: str) -> str:
    """Removes extra spaces, e.g. in generated semantic class names"""
    return " ".join(txt.split())


# Credit: https://github.com/rstudio/py-shiny/blob/a55a11161ab394f2dce579bf636f92b01133cc5f/shiny/_utils.py#L48 # noqa: E501
def drop_none(x: Dict[str, Any]) -> Dict[str, object]:
    return {k: v for k, v in x.items() if v is not None}
