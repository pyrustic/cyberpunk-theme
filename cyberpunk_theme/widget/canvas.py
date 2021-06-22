import stylebase
from cyberpunk_theme import constant


def get_style():
    style = stylebase.Canvas()
    style.background = constant.COLOR_BLACK
    style.highlightThickness = 0
    return style
