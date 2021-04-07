from pyrustic import default_style
from tk_cyberpunk_theme import constant


def get_style():
    style = default_style.Menu()
    style.background = "#003333"
    style.background = "#002323"
    style.foreground = "#98CBCB"
    style.foreground = "#90ABAB"
    style.foreground = "#C0DBDB"
    style.activeBackground = "#003333"
    style.activeForeground = "#C8FBFB"
    style.borderWidth = 0
    style.activeBorderWidth = 0
    style.relief = "flat"
    style.font = constant.FONT_DEFAULT_FAMILY, 11, "normal"
    return style
