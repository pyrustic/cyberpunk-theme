import tkstyle
from cyberpunk_theme import constant


def get_style():
    return get_option_menu_style_1()


def get_option_menu_style_1():
    style = tkstyle.OptionMenu()
    style.font = constant.FONT_FAV_NORMAL
    style.relief = "flat"
    style.selectBackground = "#B4C7EF"
    style.background = "blue"
    style.highlightThickness = 0
    style.borderWidth = 0
    style.foreground = "#B4C7EF"
    style.relief = "flat"
    style.inactiveSelectBackground = "#B4C7EF"
    style.insertBackground = "#B4C7EF"
    return style
