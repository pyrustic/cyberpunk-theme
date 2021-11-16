import tkstyle
from cyberpunk_theme import constant


# == scrollbox theme
def get_style(**kwargs):
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    return style
