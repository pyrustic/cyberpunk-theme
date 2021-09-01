import tkstyle
from cyberpunk_theme.widget import label, toplevel
from cyberpunk_theme import constant


# == confirm theme
def get_style():
    return get_confirm_style_1()


def get_confirm_style_1():
    style = toplevel.get_style()
    style.add(_get_confirm_label_header_style(), pattern="*label_header")
    style.add(_get_confirm_label_message_style(), pattern="*label_message")
    return style


# ========================================
#                PRIVATE
# ========================================


# confirm header label
def _get_confirm_label_header_style():
    style = label.get_style()
    style.font = constant.FONT_FAV_BOLD
    return style


# confirm message label
def _get_confirm_label_message_style():
    style = label.get_style()
    return style
