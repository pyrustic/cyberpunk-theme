from pyrustic import default_style
from tk_cyberpunk_theme import constant


def get_style():
    style = default_style.Scrollbar()
    style.activeBackground = constant.COLOR_ALMOST_WHITE
    style.activeBackground = "#383838"
    style.background = "gray"
    style.background = "#282828"
    style.highlightBackground = constant.COLOR_BLACK
    style.highlightColor = constant.COLOR_BLACK
    style.troughColor = constant.COLOR_BLACK
    style.relief = "flat"
    style.highlightThickness = 0
    style.borderWidth = 0
    return style
