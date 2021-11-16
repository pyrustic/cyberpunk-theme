from cyberpunk_theme.widget import label, toplevel
from cyberpunk_theme import constant


# == confirm theme
def get_style(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    style = toplevel.get_style()
    style.add(_get_confirm_label_header_style(font_family=font_family,
                                              font_size=font_size),
              pattern="*label_header")
    style.add(_get_confirm_label_message_style(), pattern="*label_message")
    return style


# ========================================
#                PRIVATE
# ========================================


# confirm header label
def _get_confirm_label_header_style(font_family=constant.FONT_FAMILY,
                                    font_size=constant.FONT_SIZE):
    style = label.get_style()
    style.font = (font_family, font_size, "bold")
    return style


# confirm message label
def _get_confirm_label_message_style():
    style = label.get_style()
    return style
