from themebase import Theme
from cyberpunk_theme.widget import toplevel
from cyberpunk_theme.widget import label
from cyberpunk_theme import constant


# == confirm theme
def get_theme():
    theme = Theme()
    theme.add_style(_get_confirm_toplevel_style(), scope="*Confirm.")
    theme.add_style(_get_confirm_label_header_style(), scope="*Confirm*label_header*")
    theme.add_style(_get_confirm_label_message_style(), scope="*Confirm*label_message*")
    return theme


# ========================================
#                PRIVATE
# ========================================
# confirm toplevel
def _get_confirm_toplevel_style():
    style = toplevel.get_style()
    return style


# confirm header label
def _get_confirm_label_header_style():
    style = label.get_style()
    style.font = constant.FONT_FAV_BOLD
    return style


# confirm message label
def _get_confirm_label_message_style():
    style = label.get_style()
    return style
