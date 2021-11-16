import tkstyle
from cyberpunk_theme import constant


def get_style(**kwargs):
    style = tkstyle.Canvas()
    style.background = constant.BACKGROUND_COLOR
    style.highlightThickness = 0
    return style
