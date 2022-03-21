import tkstyle
from cyberpunk_theme.widget import frame
from cyberpunk_theme.widget import label
from cyberpunk_theme.widget import listbox
from cyberpunk_theme.widget import scrollbar
from cyberpunk_theme import constant


# == table theme
def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = tkstyle.Frame()
    style.extend(_get_table_header_frame_style(), pattern="*frame_background*Frame")
    style.extend(_get_table_header_style(font_family=font_family,
                                      font_size=font_size),
              pattern="*Label")
    style.extend(_get_table_column_style(), pattern="*Listbox")
    style.extend(_get_table_hsb_style(), pattern="*hsb")
    style.extend(_get_table_vsb_style(), pattern="*vsb")
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
def _get_table_header_style(font_family=constant.FONT_FAMILY,
                            font_size=constant.FONT_SIZE):
    style = label.get_style()
    style.font = (font_family, font_size, "normal")
    style.foreground = "#C8EBEB"
    style.background = "#486B6B"
    style.highlightThickness = 1
    style.highlightBackground = "#43474B"
    return style


# column
def _get_table_column_style():
    style = listbox.get_style()
    style.highlightThickness = 1
    style.highlightBackground = "#43474B"
    style.highlightBackground = "#1C1922"
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
