from themebase import Theme
from cyberpunk_theme.widget import button
from cyberpunk_theme.widget import canvas
from cyberpunk_theme.widget import checkbutton
from cyberpunk_theme.widget import entry
from cyberpunk_theme.widget import frame
from cyberpunk_theme.widget import label
from cyberpunk_theme.widget import label_frame
from cyberpunk_theme.widget import listbox
from cyberpunk_theme.widget import menu
from cyberpunk_theme.widget import menubutton
from cyberpunk_theme.widget import option_menu
from cyberpunk_theme.widget import paned_window
from cyberpunk_theme.widget import radiobutton
from cyberpunk_theme.widget import scale
from cyberpunk_theme.widget import scrollbar
from cyberpunk_theme.widget import spinbox
from cyberpunk_theme.widget import text
from cyberpunk_theme.widget import toplevel
from cyberpunk_theme.megawidget import choice
from cyberpunk_theme.megawidget import confirm
from cyberpunk_theme.megawidget import pathentry
from cyberpunk_theme.megawidget import scrollbox
from cyberpunk_theme.megawidget import table
from cyberpunk_theme.megawidget import toast
from cyberpunk_theme.megawidget import tree


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
