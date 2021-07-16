from cyberpunk_theme.widget import label
from cyberpunk_theme.widget import toplevel
from cyberpunk_theme import constant
import tkstyle


# == toast theme
def get_style():
    style = toplevel.get_style()
    style.background = constant.COLOR_BLACK
    #style.add(_get_toast_header_label_style(), pattern="*label_header")
    #style.add(_get_toast_message_label_style(), pattern="*label_message")
    return style


# ========================================
#                PRIVATE
# ========================================

# toast header
def _get_toast_header_label_style():
    style = label.get_style()
    style.font = constant.FONT_FAV_BOLD
    style.background = "#101818"
    style.foreground = "#B4C7EF"
    return style


# toast message
def _get_toast_message_label_style():
    style = label.get_style()
    style.foreground = "#C8C8C8"
    style.background = "#101818"
    return style
