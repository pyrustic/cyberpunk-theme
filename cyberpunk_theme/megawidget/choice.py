import tkstyle
from cyberpunk_theme.widget import radiobutton
from cyberpunk_theme.widget import text
from cyberpunk_theme.widget import label
from cyberpunk_theme import constant


def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Toplevel()
    style.foreground = "#C8C8C8"
    style.background = constant.BACKGROUND_COLOR
    style.font = (font_family, font_size, "normal")
    style.extend(_get_radiobutton_style(), pattern="*Radiobutton")
    style.extend(_get_text_style(), pattern="*Text")
    style.extend(_get_header_style(), pattern="*label_header")
    return style

# ========================================
#                PRIVATE
# ========================================


# radiobuttons
def _get_radiobutton_style(font_family=constant.FONT_FAMILY,
                           font_size=constant.FONT_SIZE):
    style = radiobutton.get_style()
    style.foreground = "#C8C8C8"
    style.background = constant.BACKGROUND_COLOR
    style.font = (font_family, font_size, "normal")
    style.activeBackground = constant.BACKGROUND_COLOR
    style.activeForeground = "#C8C8C8"
    style.selectColor = constant.BACKGROUND_COLOR
    style.relief = "flat"
    style.highlightThickness = 0
    return style


# header
def _get_header_style(font_family=constant.FONT_FAMILY,
                      font_size=constant.FONT_SIZE):
    style = label.get_style()
    style.font = (font_family, font_size, "bold")
    return style


# text
def _get_text_style():
    style = text.get_style()
    style.highlightThickness = 0
    return style
