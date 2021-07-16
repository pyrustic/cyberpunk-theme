import tkstyle
from cyberpunk_theme.widget import frame
from cyberpunk_theme.widget import label
from cyberpunk_theme.widget import listbox
from cyberpunk_theme.widget import scrollbar
from cyberpunk_theme import constant


# == table theme
def get_style():
    style = tkstyle.Frame()
    style.add(_get_table_header_frame_style(), pattern="*frame_background*Frame")
    style.add(_get_table_header_style(), pattern="*Label")
    style.add(_get_table_column_style(), pattern="*Listbox")
    style.add(_get_table_hsb_style(), pattern="*hsb")
    style.add(_get_table_vsb_style(), pattern="*vsb")
    return style


# ========================================
#                PRIVATE
# ========================================
# header frames
def _get_table_header_frame_style():
    style = frame.get_style()
    style.highlightBackground = "#003B3B"
    style.highlightThickness = 1
    return style


# header label
def _get_table_header_style():
    style = label.get_style()
    style.font = constant.FONT_FAV_NORMAL
    style.foreground = "#C8EBEB"
    style.background = "#486B6B"
    style.highlightThickness = 1
    style.highlightBackground = "#43474B"
    return style


# column
def _get_table_column_style():
    style = listbox.get_style()
    style.highlightThickness = "1"
    style.highlightBackground = "#43474B"
    style.highlightColor = "#43474B"
    return style


# hsb
def _get_table_hsb_style():
    style = scrollbar.get_style()
    return style


# vsb
def _get_table_vsb_style():
    style = scrollbar.get_style()
    return style
