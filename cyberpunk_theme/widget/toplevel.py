import stylebase
from cyberpunk_theme import constant


def get_style():
    style = stylebase.Toplevel()
    style.background = constant.COLOR_BLACK
    return style
