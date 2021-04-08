a
<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/demo-before-after-cyberpunk-theme.png" alt="Cover">
    <br>
    <p align="center">
    <b> Demo app without and with tk-cyberpunk-theme </b>
    </p>
</div>

<!-- Intro Text -->
## Cyberpunk Theme
`tk-cyberpunk-theme` is the default dark theme for [Pyrustic Framework](https://github.com/pyrustic/pyrustic#readme).

## Installation
Available on PyPI:

```bash
pip install tk-cyberpunk-theme
```

## Usage
With a `pyrustic` powered project:

```python
from pyrustic.app import App
from tk_cyberpunk_theme import Cyberpunk
from demo.view.main_view import MainView


def main():
    # The App
    app = App(__package__)
    # Set theme
    app.theme = Cyberpunk()
    # Set view
    app.view = MainView(app)  # it could be a Tkinter object
    # Center the window
    app.center()
    # Lift off !
    app.start()


if __name__ == "__main__":
    main()

```

With a basic `Tkinter` project:
```python
import tkinter as tk
from tk_cyberpunk_theme import Cyberpunk


# root
root = tk.Tk()

# apply the theme
theme = Cyberpunk()
theme.target(root)

# add widgets to root
button = tk.Button(root, text="Hello Friend !")
button.pack()

# and more...

# the main loop !
root.mainloop()

```

## Create your own theme
A guide will be written soon. This is a work in progress. Bookmark this project and come later...


## Desktop Apps Using tk-cyberpunk-theme As Base Theme
Learn more about these following desktop applications [here](https://github.com/pyrustic/pyrustic#some-desktop-apps-built-with-pyrustic) !

<br><br>

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/hubstore_cover.png" alt="Hubstore" width="650">
    <p align="center">
    <b> Hubstore - To Connect Apps With Users </b>
    </p>
</div>


<br><br>


<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/jupitest-screenshot.png" alt="Jupitest" width="650">
    <p align="center">
    <b> Jupitest - The Graphical Test Runner </b>
    </p>
</div>


<br><br>

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/rustiql-screenshot.png" alt="Rustiql" width="650">
    <p align="center">
    <b> Rustiql - The Graphical SQL Editor </b>
    </p>
</div>


<br><br>


<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/hubway-screenshot.png" alt="Hubway" width="650">
    <p align="center">
    <b> Hubway - Release Your App To The World </b>
    </p>
</div>
