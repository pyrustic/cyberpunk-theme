import stylebase
from cyberpunk_theme import constant


def get_style():
    style = stylebase.Entry()
    style.font = constant.FONT_FAV_NORMAL
    style.relief = "flat"
    style.selectBackground = "#B4C7EF"
    style.inactiveSelectBackground = "#B4C7EF"
    style.background = "#101818"
    style.highlightThickness = 0
    style.foreground = "#B4C7EF"
    style.relief = "flat"
    style.inactiveSelectBackground = "#B4C7EF"
    style.insertBackground = "#B4C7EF"
    style.readonlyBackground = "#101818"
    return style


"""
def get_style():
    style = stylebase.Entry()
    style.font = constant.FONT_FAV_NORMAL
    style.readonlyBackground = "#EFEFEF"
    style.highlightThickness = 0
    style.foreground = constant.COLOR_BLACK
    style.relief = "flat"
    style.selectBackground = "#B4C7EF"
    return style
"""