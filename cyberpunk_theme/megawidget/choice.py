import tkstyle
from cyberpunk_theme.widget import radiobutton
from cyberpunk_theme.widget import text
from cyberpunk_theme.widget import label
from cyberpunk_theme import constant


def get_style():
    return get_choice_style_1()


def get_choice_style_1():
    style = tkstyle.Toplevel()
    style.foreground = "#C8C8C8"
    style.background = constant.COLOR_BLACK
    style.font = constant.FONT_FAV_NORMAL
    style.add(_get_radiobutton_style(), pattern="*Radiobutton")
    style.add(_get_text_style(), pattern="*Text")
    style.add(_get_header_style(), pattern="*label_header")
    return style

# ========================================
#                PRIVATE
# ========================================


# radiobuttons
def _get_radiobutton_style():
    style = radiobutton.get_style()
    style.foreground = "#C8C8C8"
    style.background = constant.COLOR_BLACK
    style.font = constant.FONT_FAV_NORMAL
    style.activeBackground = constant.COLOR_BLACK
    style.activeForeground = "#C8C8C8"
    style.selectColor = constant.COLOR_BLACK
    style.relief = "flat"
    style.highlightThickness = 0
    return style

# header
def _get_header_style():
    style = label.get_style()
    style.font = constant.FONT_FAV_BOLD
    return style

# text
def _get_text_style():
    style = text.get_style()
    style.highlightThickness = 0
    return style
