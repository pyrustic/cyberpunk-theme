import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.OptionMenu()
    style.font = (font_family, font_size, "normal")
    style.relief = "flat"
    style.selectBackground = "#B4C7EF"
    style.highlightThickness = 0
    style.borderWidth = 0
    style.foreground = "#B4C7EF"
    style.relief = "flat"
    style.inactiveSelectBackground = "#B4C7EF"
    style.insertBackground = "#B4C7EF"
    style.highlightColor = "gray"
    return style
