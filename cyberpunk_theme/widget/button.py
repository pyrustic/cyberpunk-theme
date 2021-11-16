import tkstyle
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    return get_button_dark_style(font_family=font_family, font_size=font_size)


def get_button_dark_style(font_family=constant.FONT_FAMILY,
                          font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#111519"
    style.foreground = "#A098A0"
    style.activeBackground = "#191D21"
    style.activeForeground = "#A098A0"
    style.highlightBackground = "#484048"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_dark_filled_style(font_family=constant.FONT_FAMILY,
                                 font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#191D21"
    style.foreground = "#A098A0"
    style.activeBackground = "#111519"
    style.activeForeground = "#A098A0"
    style.highlightBackground = "#484048"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_blue_style(font_family=constant.FONT_FAMILY,
                          font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#131723"
    style.foreground = "#2E9CB5"
    style.activeBackground = "#004B64"
    style.activeForeground = "#74BFD8"
    style.highlightBackground = "#004B64"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_blue_filled_style(font_family=constant.FONT_FAMILY,
                                 font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#004B64"
    style.foreground = "#74BFD8"
    style.activeBackground = "#131723"
    style.activeForeground = "#2E9CB5"
    style.highlightBackground = "#004B64"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_green_style(font_family=constant.FONT_FAMILY,
                           font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#111C19"
    style.foreground = "#55977D"
    style.activeBackground = "#094431"
    style.activeForeground = "#84BFAC"
    style.highlightBackground = "#094431"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_green_filled_style(font_family=constant.FONT_FAMILY,
                                  font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#094431"
    style.foreground = "#84BFAC"
    style.activeBackground = "#111C19"
    style.activeForeground = "#55977D"
    style.highlightBackground = "#094431"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_yellow_style(font_family=constant.FONT_FAMILY,
                            font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#222219"
    style.foreground = "#956300"
    style.activeBackground = "#956300"
    style.activeForeground = "#E5E59F"
    style.highlightBackground = "#956300"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_yellow_filled_style(font_family=constant.FONT_FAMILY,
                                   font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#956300"
    style.foreground = "#E5E59F"
    style.activeBackground = "#222219"
    style.activeForeground = "#956300"
    style.highlightBackground = "#956300"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_red_style(font_family=constant.FONT_FAMILY,
                         font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#1B1519"
    style.foreground = "#AA2323"
    style.activeBackground = "#AA2323"
    style.activeForeground = "#FFB8B8"
    style.highlightBackground = "#AA2323"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style


def get_button_red_filled_style(font_family=constant.FONT_FAMILY,
                                font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#AA2323"
    style.foreground = "#FFB8B8"
    style.activeBackground = "#1B1519"
    style.activeForeground = "#AA2323"
    style.highlightBackground = "#AA2323"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.cursor = "hand1"
    return style
