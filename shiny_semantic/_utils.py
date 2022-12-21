def squash_whitespace(txt: str) -> str:
    """Removes extra spaces, e.g. in generated semantic class names"""
    return " ".join(txt.split())
