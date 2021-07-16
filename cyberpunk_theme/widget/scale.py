import tkstyle
from cyberpunk_theme import constant


def get_style():
    style = tkstyle.Scale()
    style.font = constant.FONT_FAV_NORMAL
    style.foreground = "#B0B0B0"
    style.background = constant.COLOR_BLACK
    style.troughColor = "#1C2024"
    style.activeBackground = "#004B64"
    style.selectBackground = "#105B74"
    style.selectForeground = "#D5D5FF"
    style.readonlyBackground = "#181C20"
    style.inactiveSelectBackground = "#105B74"
    style.disabledBackground = "#15191D"
    style.insertBackground = "#9B9B9B"
    style.highlightThickness = 0
    style.highlightBackground = "#1C2024"
    style.highlightColor = "yellow"
    style.borderWidth = 0
    style.relief = "flat"
    style.sliderRelief = "sunken"
    return style
