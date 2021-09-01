import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_frame_style_1()


def get_frame_style_1():
    style = tkstyle.Frame()
    style.background = constant.COLOR_1
    style.highlightBackground = "gray"
    style.highlightColor = "white"
    return style
