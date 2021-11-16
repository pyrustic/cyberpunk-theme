from cyberpunk_theme.widget import label
from cyberpunk_theme.widget import toplevel
from cyberpunk_theme import constant


# == toast theme
def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = toplevel.get_style()
    style.background = constant.BACKGROUND_COLOR
    style.add(_get_toast_header_label_style(font_family=font_family,
                                            font_size=font_size),
              pattern="*label_header")
    style.add(_get_toast_message_label_style(), pattern="*label_message")
    return style


# ========================================
#                PRIVATE
# ========================================

# toast header
def _get_toast_header_label_style(font_family=constant.FONT_FAMILY,
                                  font_size=constant.FONT_SIZE):
    style = label.get_style()
    style.font = (font_family, font_size, "bold")
    style.background = "#101818"
    style.foreground = "#B4C7EF"
    return style


# toast message
def _get_toast_message_label_style():
    style = label.get_style()
    style.foreground = "#C8C8C8"
    style.background = "#101818"
    return style
