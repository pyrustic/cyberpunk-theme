import stylebase
from cyberpunk_theme import constant


def get_style():
    style = stylebase.Menubutton()
    style.font = constant.FONT_FAV_NORMAL
    style.background = "#101818"
    style.foreground = "#B4C7EF"
    style.relief = "flat"
    style.borderWidth = 0
    style.highlightThickness = 0
    style.highlightBackground = "#101010"
    style.activeBackground = constant.COLOR_CHECKBUTTON
    style.activeForeground = constant.COLOR_ALMOST_WHITE
    return style
