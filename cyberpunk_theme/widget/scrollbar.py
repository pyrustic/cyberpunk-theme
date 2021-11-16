import tkstyle
from cyberpunk_theme import constant


def get_style(**kwargs):
    style = tkstyle.Scrollbar()
    style.activeBackground = "#292D31"
    style.background = "#191D21"
    style.highlightBackground = constant.BACKGROUND_COLOR
    style.highlightColor = constant.BACKGROUND_COLOR
    style.troughColor = constant.BACKGROUND_COLOR
    style.relief = "flat"
    style.highlightThickness = 0
    style.borderWidth = 0
    return style
