import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Listbox()
    style.font = (font_family, font_size, "normal")
    style.relief = "flat"
    style.selectBackground = "#105B74"
    style.selectForeground = "#D5D5FF"
    style.background = "#1F2327"
    style.foreground = "#9B9B9B"
    style.highlightThickness = 0
    style.relief = "flat"
    return style
