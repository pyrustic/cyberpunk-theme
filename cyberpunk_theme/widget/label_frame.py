import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.LabelFrame()
    style.font = (font_family, font_size, "normal")
    style.background = constant.BACKGROUND_COLOR
    style.foreground = "#B0B0B0"
    style.borderWidth = 1
    return style
