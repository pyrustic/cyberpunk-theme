import tkstyle
from cyberpunk_theme import constant


def get_style():
    style = tkstyle.Listbox()
    style.font = constant.FONT_FAV_NORMAL
    style.relief = "flat"
    style.selectBackground = "#105B74"
    style.selectForeground = "#D5D5FF"
    style.background = "#1C2024"
    style.foreground = "#9B9B9B"
    style.highlightThickness = 0
    style.relief = "flat"
    return style
