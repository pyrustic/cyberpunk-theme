import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_toplevel_style_1()


def get_toplevel_style_1():
    style = tkstyle.Toplevel()
    style.background = constant.COLOR_BLACK
    return style
