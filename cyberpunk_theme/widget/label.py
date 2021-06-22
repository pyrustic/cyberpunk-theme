import stylebase
from cyberpunk_theme import constant


def get_style():
    style = stylebase.Label()
    style.font = constant.FONT_FAV_NORMAL
    style.background = constant.COLOR_BLACK
    style.foreground = "#CFCFCF"
    return style
