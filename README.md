<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/cyberpunk-cover.png" alt="Figure" width="970">
    <p align="center">
    <i> Cyberpunk theme made with TkStyle </i>
    </p>
</div>

```bash
$ pip install cyberpunk-theme
```

```python
import tkinter as tk
from cyberpunk_theme import Cyberpunk
from cyberpunk_theme.widget.button import get_button_style_4


root = tk.Tk()
# apply the Cyberpunk theme to the GUI
cyberpunk_theme = Cyberpunk()
cyberpunk_theme.target(root)

# write your awesome code here
# ...
# ...

button = tk.Button(root, text="Button")
button.pack()

# do you need to set dynamically a specific style to a button ?
# there are 10 styles for buttons ! from the black to the red style !
button_style_4 = get_button_style_4()
button_style_4.target(button)

# mainloop
root.mainloop()


```

Do you want to create your own theme/style ?

Check out [TkStyle](https://github.com/pyrustic/tkstyle) !


This is a work in progress for early adopters.

Bookmark this project so you don't miss any updates !

You can visit my [website](https://pyrustic.github.io) to discover related cool projects !
