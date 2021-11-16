import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Menu()
    style.background = "#121C20"
    style.foreground = "#A1ABAF"
    style.activeBackground = "#121C20"
    style.activeForeground = "#D1DBDF"
    style.activeBorderWidth = 0
    style.borderWidth = 0
    style.relief = "flat"
    style.cursor = "hand1"
    style.font = (font_family, font_size, "normal")
    return style
