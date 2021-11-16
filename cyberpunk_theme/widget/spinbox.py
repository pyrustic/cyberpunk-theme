import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Spinbox()
    style.font = (font_family, font_size, "normal")
    style.foreground = "#9B9B9B"
    style.background = "#1C2024"
    style.selectBackground = "#105B74"
    style.selectForeground = "#D5D5FF"
    style.readonlyBackground = "#181C20"
    style.inactiveSelectBackground = "#105B74"
    style.disabledBackground = "#15191D"
    style.insertBackground = "#9B9B9B"
    style.highlightBackground = "#1C2024"
    style.highlightColor = "#262A2E"
    style.relief = "flat"
    return style
