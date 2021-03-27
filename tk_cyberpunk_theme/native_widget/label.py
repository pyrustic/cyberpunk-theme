from pyrustic import default_style
from tk_cyberpunk_theme import constant


def get_style():
    style = default_style.Label()
    style.font = constant.FONT_FAV_NORMAL
    style.background = constant.COLOR_BLACK
    style.foreground = "#CFCFCF"
    return style
