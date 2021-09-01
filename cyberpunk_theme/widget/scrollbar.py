import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_scrollbar_style_1()


def get_scrollbar_style_1():
    style = tkstyle.Scrollbar()
    style.activeBackground = "#292D31"
    style.background = "#191D21"
    style.highlightBackground = constant.COLOR_BLACK
    style.highlightColor = constant.COLOR_BLACK
    style.troughColor = constant.COLOR_BLACK
    style.relief = "flat"
    style.highlightThickness = 0
    style.borderWidth = 0
    return style
