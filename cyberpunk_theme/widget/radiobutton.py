import stylebase
from cyberpunk_theme import constant


def get_style():
    style = stylebase.Radiobutton()
    style.background = constant.COLOR_BLACK
    style.foreground = "#CFCFCF"
    style.foreground = "#B4C7EF"
    style.font = constant.FONT_FAV_NORMAL
    style.highlightThickness = 0
    style.selectColor = constant.COLOR_CHECKBUTTON
    style.activeBackground = constant.COLOR_CHECKBUTTON
    style.activeForeground = constant.COLOR_ALMOST_WHITE
    return style
