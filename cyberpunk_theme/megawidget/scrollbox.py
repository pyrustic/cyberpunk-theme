import stylebase
from cyberpunk_theme import constant
from themebase import Theme


# == scrollbox theme
def get_theme():
    theme = Theme()
    theme.add_style(_get_scrollbox_style(), scope="*Scrollbox.")
    return theme


# scrollbox style
def _get_scrollbox_style():
    style = stylebase.Frame()
    style.background = constant.COLOR_BLACK
    return style
