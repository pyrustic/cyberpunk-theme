import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Checkbutton()
    style.background = constant.BACKGROUND_COLOR
    style.foreground = "#9B9B9B"
    style.font = (font_family, font_size, "normal")
    style.highlightThickness = 0
    style.selectColor = constant.BACKGROUND_COLOR
    style.activeBackground = constant.BACKGROUND_COLOR
    style.activeForeground = "#B9B9B9"
    return style
