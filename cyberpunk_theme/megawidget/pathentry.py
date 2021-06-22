from themebase import Theme
from cyberpunk_theme.widget import frame, button
from cyberpunk_theme import constant


# == confirm theme
def get_theme():
    theme = Theme()
    theme.add_style(_get_frame_style(), scope="*Pathentry.")
    theme.add_style(_get_button_style(), scope="*Pathentry.Button.")
    return theme


# ========================================
#                PRIVATE
# ========================================
# frame style
def _get_frame_style():
    style = frame.get_style()
    return style

# button style
def _get_button_style():
    style = button.get_style()
    style.padX = 0
    style.padY = 0
    style.borderWidth = 0
    style.highlightThickness = 0
    return style
