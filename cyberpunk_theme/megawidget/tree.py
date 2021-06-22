import stylebase
from themebase import Theme
from cyberpunk_theme import constant


# == tree theme
def get_theme():
    theme = Theme()
    theme.add_style(_get_tree_body_style(), scope="*Tree.")
    theme.add_style(_get_tree_node_style(), scope="*Tree*FrameNode.")
    theme.add_style(_get_tree_header_style(), scope="*Tree*frame_header.")
    theme.add_style(_get_tree_box_style(), scope="*Tree*frame_box.")
    return theme


# ========================================
#                   PRIVATE
# ========================================
# tree body
def _get_tree_body_style():
    style = stylebase.Frame()
    style.background = constant.COLOR_BLACK
    return style


# tree node
def _get_tree_node_style():
    style = stylebase.Frame()
    style.background = constant.COLOR_BLACK
    return style


# tree header
def _get_tree_header_style():
    style = stylebase.Frame()
    style.background = constant.COLOR_BLACK
    return style


# tree box
def _get_tree_box_style():
    style = stylebase.Frame()
    style.background = constant.COLOR_BLACK
    return style
