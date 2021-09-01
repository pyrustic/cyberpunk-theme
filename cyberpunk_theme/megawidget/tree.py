import tkstyle
from cyberpunk_theme import constant


# == tree theme
def get_style():
    return get_tree_style_1()


def get_tree_style_1():
    style = tkstyle.Frame()
    style.background = constant.COLOR_1
    style.add(_get_tree_node_style(), pattern="*FrameNode")
    style.add(_get_tree_header_style(), pattern="*frame_header")
    style.add(_get_tree_box_style(), pattern="*frame_box")
    return style


# ========================================
#                   PRIVATE
# ========================================

# tree node
def _get_tree_node_style():
    style = tkstyle.Frame()
    style.background = constant.COLOR_BLACK
    return style


# tree header
def _get_tree_header_style():
    style = tkstyle.Frame()
    style.background = constant.COLOR_BLACK
    return style


# tree box
def _get_tree_box_style():
    style = tkstyle.Frame()
    style.background = constant.COLOR_BLACK
    return style
