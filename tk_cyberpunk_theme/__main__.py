from pyrustic.app import App
from tk_cyberpunk_theme.main import Cyberpunk
from tk_cyberpunk_theme.demo.demo_view import DemoView


if __name__ == "__main__":
    # The App
    app = App(__package__)
    # Set theme
    app.theme = Cyberpunk()
    # Set view
    app.view = DemoView(app)
    # Center the window
    app.center()
    # Lift off !
    app.start()
