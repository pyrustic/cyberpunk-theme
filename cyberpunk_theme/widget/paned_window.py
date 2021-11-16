import tkstyle
from cyberpunk_theme import constant


def get_style(**kwargs):
    style = tkstyle.PanedWindow()
    style.background = constant.BACKGROUND_COLOR
    return style
