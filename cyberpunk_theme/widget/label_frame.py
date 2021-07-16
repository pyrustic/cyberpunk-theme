import tkstyle
from cyberpunk_theme import constant


def get_style():
    style = tkstyle.LabelFrame()
    style.font = constant.FONT_FAV_NORMAL
    style.background = constant.COLOR_BLACK
    style.foreground = "#B0B0B0"
    style.borderWidth = 1
    style.highlightBackground = "red"
    return style
