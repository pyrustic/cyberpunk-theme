import tkstyle
from cyberpunk_theme.widget import frame
from cyberpunk_theme import constant


# == confirm theme
def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = frame.get_style()
    style.extend(_get_button_style(font_family=font_family,
                                font_size=font_size),
              pattern="*Button")
    return style


# ========================================
#                PRIVATE
# ========================================

# button style
def _get_button_style(font_family=constant.FONT_FAMILY,
                      font_size=constant.FONT_SIZE):
    style = tkstyle.Button()
    style.font = (font_family, font_size, "normal")
    style.background = "#191D21"
    style.foreground = "#A098A0"
    style.activeBackground = "#132021"
    style.activeForeground = "#A098A0"
    style.highlightBackground = "#191D21"
    style.highlightColor = "white"
    style.highlightThickness = 1
    style.relief = "flat"
    style.padY = 0
    style.padX = 0
    style.cursor = "hand1"
    return style
