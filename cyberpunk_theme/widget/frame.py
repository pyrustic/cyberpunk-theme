import tkstyle
from cyberpunk_theme import constant


def get_style(**kwargs):
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    style.highlightBackground = "gray"
    style.highlightColor = "white"
    return style
