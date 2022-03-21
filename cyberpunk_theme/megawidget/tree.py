import tkstyle
from cyberpunk_theme import constant


# == tree theme
def get_style(**kwargs):
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    style.extend(_get_tree_node_style(), pattern="*FrameNode")
    style.extend(_get_tree_header_style(), pattern="*frame_header")
    style.extend(_get_tree_box_style(), pattern="*frame_box")
    return style


# ========================================
#                   PRIVATE
# ========================================

# tree node
def _get_tree_node_style():
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    return style


# tree header
def _get_tree_header_style():
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    return style


# tree box
def _get_tree_box_style():
    style = tkstyle.Frame()
    style.background = constant.BACKGROUND_COLOR
    return style
