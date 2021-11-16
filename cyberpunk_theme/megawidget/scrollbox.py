import tkstyle
from cyberpunk_theme import constant


# == scrollbox theme
def get_style(font_family=None, font_size=None):
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    return style
