import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_paned_window_style_1()


def get_paned_window_style_1():
    style = tkstyle.PanedWindow()
    style.background = constant.COLOR_BLACK
    return style
