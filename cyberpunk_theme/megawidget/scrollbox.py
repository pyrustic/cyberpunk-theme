from cyberpunk_theme import constant
import tkstyle


# == scrollbox theme
def get_style():
    return get_scrollbox_style_1()


def get_scrollbox_style_1():
    style = tkstyle.Frame()
    style.background = constant.COLOR_1
    return style
