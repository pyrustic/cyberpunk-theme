import tkstyle
from cyberpunk_theme import constant


def get_style():
    style = tkstyle.PanedWindow()
    style.background = constant.COLOR_BLACK
    return style
