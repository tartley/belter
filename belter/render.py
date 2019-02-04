import pyglet

class Render:

    def __init__(self, win):
        self.win = win
        self.fps_display = pyglet.window.FPSDisplay(win)
        win.set_handler('on_draw', self.on_draw)

    def on_draw(self):
        self.win.clear()
        self.fps_display.draw()

