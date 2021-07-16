import tkstyle
from cyberpunk_theme import constant


def get_style():
    style = tkstyle.Menubutton()
    style.background = "#0C1014"
    style.foreground = "#B0B0B0"
    style.activeBackground = "#1E2226"
    style.activeForeground = "#ABABAB"
    style.borderWidth = 0
    style.activeBorderWidth = 0
    style.highlightThickness = 0
    style.highlightBackground = "#101010"
    style.relief = "flat"
    style.cursor = "hand1"
    style.font = constant.FONT_DEFAULT_FAMILY, 11, "normal"
    return style
