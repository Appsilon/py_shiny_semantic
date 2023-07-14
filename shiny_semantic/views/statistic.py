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
    """
    Generate a statistic element with a value and label.

    This function creates an HTML statistic element with a provided value and label. The statistic element
    is structured as a container consisting of a value and label, which can be arranged in different orders.
    
    Args:
        value (TagChildArg): The HTML content representing the value to be displayed in the statistic.
        label (str): The label associated with the value, providing context or description.
        value_first (bool, optional): If True, the value is displayed above the label. If False, the label
            is displayed above the value. Defaults to True.
        class_ (str, optional): Additional CSS class(es) to be added to the statistic element.
        **kwargs (TagAttrArg): Additional HTML attributes to be included in the <div> tag.

    Returns:
        str: A string representing the generated HTML statistic element.

    Example:
        value_content = tags.span("42", class_ = "value-content")
        stat_element = statistic(
          value_content,
          label = "Total Items",
          value_first = False,
          class_ = "highlight"
        )
        print(stat_element)

    """
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
