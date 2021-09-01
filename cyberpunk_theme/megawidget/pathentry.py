import tkstyle
from cyberpunk_theme.widget import frame, button
from cyberpunk_theme import constant


# == confirm theme
def get_style():
    return get_pathentry_style_1()


def get_pathentry_style_1():
    style = frame.get_style()
    style.add(_get_button_style(), pattern="*Button")
    return style


# ========================================
#                PRIVATE
# ========================================

# button style
def _get_button_style():
    style = tkstyle.Button()
    style.font = constant.FONT_FAV_NORMAL
    style.background = "#191D21"
    style.foreground = "#A098A0"
    style.activeBackground = "#132021"
    style.activeForeground = "#A098A0"
    style.highlightBackground = "#484048"
    style.highlightColor = "white"
    style.highlightThickness = 0
    style.relief = "flat"
    style.padY = 0
    style.padX = 0
    style.cursor = "hand1"
    return style
