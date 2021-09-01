import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_checkbutton_style_1()


def get_checkbutton_style_1():
    style = tkstyle.Checkbutton()
    style.background = constant.COLOR_BLACK
    style.foreground = "#9B9B9B"
    style.font = constant.FONT_FAV_NORMAL
    style.highlightThickness = 0
    style.selectColor = constant.COLOR_BLACK
    style.activeBackground = constant.COLOR_BLACK
    style.activeForeground = "#B9B9B9"
    return style
