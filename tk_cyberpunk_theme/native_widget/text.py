from pyrustic import default_style
from tk_cyberpunk_theme import constant


def get_style():
    style = default_style.Text()
    style.font = constant.FONT_FAV_NORMAL
    style.relief = "flat"
    style.selectBackground = "#B4C7EF"
    style.inactiveSelectBackground = "#B4C7EF"
    style.background = "#101818"
    style.highlightThickness = 0
    style.foreground = "#B4C7EF"
    style.relief = "flat"
    style.inactiveSelectBackground = "#B4C7EF"
    return style
