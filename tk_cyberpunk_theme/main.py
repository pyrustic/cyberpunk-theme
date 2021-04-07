from pyrustic.theme import Theme
from tk_cyberpunk_theme.native_widget import button
from tk_cyberpunk_theme.native_widget import canvas
from tk_cyberpunk_theme.native_widget import checkbutton
from tk_cyberpunk_theme.native_widget import entry
from tk_cyberpunk_theme.native_widget import frame
from tk_cyberpunk_theme.native_widget import label
from tk_cyberpunk_theme.native_widget import label_frame
from tk_cyberpunk_theme.native_widget import listbox
from tk_cyberpunk_theme.native_widget import menu
from tk_cyberpunk_theme.native_widget import menubutton
from tk_cyberpunk_theme.native_widget import option_menu
from tk_cyberpunk_theme.native_widget import paned_window
from tk_cyberpunk_theme.native_widget import radiobutton
from tk_cyberpunk_theme.native_widget import scale
from tk_cyberpunk_theme.native_widget import scrollbar
from tk_cyberpunk_theme.native_widget import spinbox
from tk_cyberpunk_theme.native_widget import text
from tk_cyberpunk_theme.native_widget import toplevel
from tk_cyberpunk_theme.pyrustic_widget import choice
from tk_cyberpunk_theme.pyrustic_widget import confirm
from tk_cyberpunk_theme.pyrustic_widget import pathentry
from tk_cyberpunk_theme.pyrustic_widget import scrollbox
from tk_cyberpunk_theme.pyrustic_widget import table
from tk_cyberpunk_theme.pyrustic_widget import toast
from tk_cyberpunk_theme.pyrustic_widget import tree


class Cyberpunk(Theme):
    def __init__(self):
        super().__init__()
        _add_native_widget_style(self)
        _add_pyrustic_widget_style(self)


def _add_native_widget_style(theme):
    elements = (button, canvas, checkbutton, entry,
                frame, label, label_frame, listbox,
                menu, menubutton, option_menu, paned_window,
                radiobutton, scale, scrollbar, spinbox, text, toplevel)
    for element in elements:
        theme.add_style(element.get_style())


def _add_pyrustic_widget_style(theme):
    elements = (choice, confirm, pathentry, scrollbox,
                table, toast, tree)
    for element in elements:
        theme.add_theme(element.get_theme())
