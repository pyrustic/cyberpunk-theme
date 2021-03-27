from pyrustic import default_style
from tk_cyberpunk_theme import constant


def get_style():
    style = default_style.Toplevel()
    style.background = constant.COLOR_BLACK
    return style
