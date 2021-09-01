import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_canvas_style_1()


def get_canvas_style_1():
    style = tkstyle.Canvas()
    style.background = constant.COLOR_BLACK
    style.highlightThickness = 0
    return style
