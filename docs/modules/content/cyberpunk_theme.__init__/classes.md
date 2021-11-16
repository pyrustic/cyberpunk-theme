Back to [Modules overview](https://github.com/pyrustic/cyberpunk-theme/blob/master/docs/modules/README.md)
  
# Module documentation
>## cyberpunk\_theme.\_\_init\_\_
No description
<br>
[constants (2)](https://github.com/pyrustic/cyberpunk-theme/blob/master/docs/modules/content/cyberpunk_theme.__init__/constants.md) &nbsp;.&nbsp; [classes (1)](https://github.com/pyrustic/cyberpunk-theme/blob/master/docs/modules/content/cyberpunk_theme.__init__/classes.md)


## Classes
```python
class Cyberpunk(tkstyle.Theme):
    """
    A theme is a collection of styles and... others theme.
    """

    def __init__(self, font_family='Liberation Mono', font_size=11):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from tkstyle.Theme
    @property
    def styles(self):
        """
        Get a list of styles that this theme contains
        """

    # inherited from tkstyle.Theme
    def add(self, style, pattern=None):
        """
        Add a style to this theme.
        The style is an instance of 'pyrustic.default_style._Style'.
        You don't have to directly subclass the private class '_Style'.
        Instead, subclass one of the public classes in the module 'pyrustic.default_style'.
        The scope here is an optional string.
        When you don't set the scope, the style will be applied as it.
        Example. If you add a Button style in your theme, this style will be
        applied to all buttons widgets. But you can restrict this effect to a scope.
        This scope could be by example "*Canvas*Button.", meaning all buttons
        that are living on all Canvas, are candidates for the given style.
        """

    # inherited from tkstyle.Theme
    def target(self, root):
        """
        Set this theme to master. Master here should be the root widget of your app.
        You need to set the theme to master before installing others widgets on the master.
        """

    def _add_megawidgets(self, font_family, font_size):
        """
        
        """

    def _add_widgets(self, font_family, font_size):
        """
        
        """

```

