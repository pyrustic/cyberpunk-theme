import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Menubutton()
    style.font = (font_family, font_size, "normal")
    style.background = "#121C20"
    style.background = "#1C2024"
    style.foreground = "#B0B0B0"
    style.activeBackground = "#121C20"
    style.activeBackground = "#1C2125"
    style.activeForeground = "#ABABAB"
    style.borderWidth = 0
    style.activeBorderWidth = 0
    style.highlightThickness = 0
    style.highlightBackground = "#101010"
    style.relief = "flat"
    style.cursor = "hand1"
    style.padY = 3
    style.width = 16
    return style
