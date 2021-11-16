import tkstyle
from cyberpunk_theme import constant


def get_style(**kwargs):
    style = tkstyle.Toplevel()
    style.background = constant.BACKGROUND_COLOR
    return style
