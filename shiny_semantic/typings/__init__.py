from enum import Enum


class ButtonType(Enum):
    default = ""
    primary = "primary"
    secondary = "secondary"
    positive = "positive"
    negative = "negative"


class ButtonFill(Enum):
    solid = ""
    outline = "basic"
    underline = "tertiary"


class ButtonColor(Enum):
    default = ""
    red = "red"
    orange = "orange"
    yellow = "yellow"
    olive = "olive"
    green = "green"
    teal = "teal"
    blue = "blue"
    violet = "violet"
    purple = "purple"
    pink = "pink"
    brown = "brown"
    grey = "grey"
    black = "black"
