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


def get_theme(font_family=constant.FONT_FAMILY,
              font_size=constant.FONT_SIZE):
    theme = tkstyle.Theme()
    _add_widgets_styles(theme, font_family=font_family, font_size=font_size)
    _add_megawidgets_styles(theme, font_family=font_family, font_size=font_size)
    return theme


def _add_widgets_styles(theme, font_family, font_size):
    # button
    theme.add(button.get_style(font_family=font_family, font_size=font_size))
    # canvas
    theme.add(canvas.get_style(font_family=font_family, font_size=font_size))
    # checkbutton
    theme.add(checkbutton.get_style(font_family=font_family, font_size=font_size))
    # entry
    theme.add(entry.get_style(font_family=font_family, font_size=font_size))
    # frame
    theme.add(frame.get_style(font_family=font_family, font_size=font_size))
    # label
    theme.add(label.get_style(font_family=font_family, font_size=font_size))
    # label_frame
    theme.add(label_frame.get_style(font_family=font_family, font_size=font_size))
    # listbox
    theme.add(listbox.get_style(font_family=font_family, font_size=font_size))
    # menu
    theme.add(menu.get_style(font_family=font_family, font_size=font_size))
    # menubutton
    theme.add(menubutton.get_style(font_family=font_family, font_size=font_size))
    # option_menu
    theme.add(option_menu.get_style(font_family=font_family, font_size=font_size))
    # paned_window
    theme.add(paned_window.get_style(font_family=font_family, font_size=font_size))
    # radiobutton
    theme.add(radiobutton.get_style(font_family=font_family, font_size=font_size))
    # scale
    theme.add(scale.get_style(font_family=font_family, font_size=font_size))
    # scrollbar
    theme.add(scrollbar.get_style(font_family=font_family, font_size=font_size))
    # spinbox
    theme.add(spinbox.get_style(font_family=font_family, font_size=font_size))
    # text
    theme.add(text.get_style(font_family=font_family, font_size=font_size))
    # toplevel
    theme.add(toplevel.get_style(font_family=font_family, font_size=font_size))


def _add_megawidgets_styles(theme, font_family, font_size):
    # Choice
    theme.add(choice.get_style(font_family=font_family, font_size=font_size),
              pattern="*Choice")
    # Confirmation
    theme.add(confirmation.get_style(font_family=font_family, font_size=font_size),
              pattern="*Confirmation")
    # PathField
    theme.add(pathfield.get_style(font_family=font_family, font_size=font_size),
              pattern="*PathField")
    # ScrollBox
    theme.add(scrollbox.get_style(font_family=font_family, font_size=font_size),
              pattern="*ScrollBox")
    # Table
    theme.add(table.get_style(font_family=font_family, font_size=font_size),
              pattern="*Table")
    # Toast
    theme.add(toast.get_style(font_family=font_family, font_size=font_size),
              pattern="*Toast")
    # Tree
    theme.add(tree.get_style(font_family=font_family, font_size=font_size),
              pattern="*Tree")
