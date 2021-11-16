import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Label()
    style.font = (font_family, font_size, "normal")
    style.background = constant.BACKGROUND_COLOR
    style.foreground = "#A8A8A8"
    style.highlightThickness = 0
    style.borderWidth = 0
    style.padX = 0
    style.padY = 0
    return style
