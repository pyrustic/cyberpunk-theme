import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_label_style_1()


def get_label_style_1():
    style = tkstyle.Label()
    style.font = constant.FONT_FAV_NORMAL
    style.background = constant.COLOR_BLACK
    style.foreground = "#B0B0B0"
    style.foreground = "#A8A8A8"
    return style
