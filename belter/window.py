"""
Windowing, done using pyglet.
"""
import pyglet
from pyglet.window import key
from pyglet.event import EVENT_HANDLED

class Window:

    def __init__(self):
        self.win = None

    def create(self, title):
        self.win = pyglet.window.Window(
            caption=title, fullscreen=False, vsync=False
        )
        self.win.set_handler('on_key_press', self.on_key_press)

    def _get_current_screen_index(self):
        current = self.win.screen
        screens = self.win.display.get_screens()
        for index, screen in enumerate(screens):
            if screen == current:
                return index
        raise RuntimeError(f"Current screen {current} not found in {screens}")

    def _get_next_screen(self):
        screens = self.win.display.get_screens()
        current_index = self._get_current_screen_index()
        next_index = (current_index + 1) % len(screens)
        return screens[next_index]

    def toggle_fullscreen(self):
        if self.win.fullscreen:
            self.win.set_fullscreen(fullscreen=False)
        else:
            self.win.set_fullscreen(screen=self._get_next_screen())

    def on_key_press(self, symbol, _):
        if symbol in KEYS:
            KEYS[symbol](self)
            return EVENT_HANDLED
        return None

    def get_fps_display(self):
        return pyglet.window.FPSDisplay(self.win)

    def clear(self):
        self.win.clear()

    def set_on_draw(self, on_draw):
        self.win.set_handler('on_draw', on_draw)

    def main_loop(self, world):
        pyglet.clock.schedule(world.update)
        pyglet.app.run()

KEYS = {
    key.F10: Window.toggle_fullscreen,
}

