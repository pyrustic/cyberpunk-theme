import tkstyle
from cyberpunk_theme import constant
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
from cyberpunk_theme.megawidget import confirmation
from cyberpunk_theme.megawidget import pathfield
from cyberpunk_theme.megawidget import scrollbox
from cyberpunk_theme.megawidget import table
from cyberpunk_theme.megawidget import toast
from cyberpunk_theme.megawidget import tree


WIDGETS = (button, canvas, checkbutton, entry,
           frame, label, label_frame, listbox,
           menu, menubutton, option_menu, paned_window,
           radiobutton, scale, scrollbar, spinbox, text, toplevel)


MEGAWIDGETS = (("Choice", choice), ("Confirmation", confirmation),
               ("PathField", pathfield), ("ScrollBox", scrollbox),
               ("Table", table), ("Toast", toast), ("Tree", tree))


class Cyberpunk(tkstyle.Theme):
    def __init__(self, font_family=constant.FONT_FAMILY,
                 font_size=constant.FONT_SIZE):
        super().__init__()
        self._add_widgets(font_family, font_size)
        self._add_megawidgets(font_family, font_size)

    def _add_widgets(self, font_family, font_size):
        for item in WIDGETS:
            self.add(item.get_style(font_family=font_family,
                                    font_size=font_size))

    def _add_megawidgets(self, font_family, font_size):
        for name, item in MEGAWIDGETS:
            self.add(item.get_style(font_family=font_family,
                                    font_size=font_size),
                     pattern="*{}".format(name))
