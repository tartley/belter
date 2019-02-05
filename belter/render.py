class Render:

    def __init__(self, window):
        self.window = window
        self.fps_display = window.get_fps_display()

    def on_draw(self):
        self.window.clear()
        self.fps_display.draw()

