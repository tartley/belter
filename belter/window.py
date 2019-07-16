"""
Windowing, done using pyglet.
"""
import pyglet
from pyglet.window import key
from pyglet.event import EVENT_HANDLED

class Window:

    def __init__(self):
        self.pygwin = None
        self.keys = {
            key.F10: self.toggle_fullscreen,
        }

    def create(self, title):
        self.pygwin = pyglet.window.Window(
            config=pyglet.gl.Config(major_version=3, minor_version=3),
            caption=title, fullscreen=True, resizable=True, vsync=False
        )
        self.pygwin.set_handler('on_key_press', self.on_key_press)
        return self.pygwin.context.get_info().get_version()

    def resize(self, render, width, height):
        render.set_viewport(width, height)
        return EVENT_HANDLED

    def _get_current_screen_index(self):
        current = self.pygwin.screen
        screens = self.pygwin.display.get_screens()
        for index, screen in enumerate(screens):
            if screen == current:
                return index
        raise RuntimeError(f"Current screen {current} not found in {screens}")

    def _get_next_screen(self):
        screens = self.pygwin.display.get_screens()
        current_index = self._get_current_screen_index()
        next_index = (current_index + 1) % len(screens)
        return screens[next_index]

    def toggle_fullscreen(self):
        if self.pygwin.fullscreen:
            self.pygwin.set_fullscreen(fullscreen=False)
        else:
            self.pygwin.set_fullscreen(screen=self._get_next_screen())

    def on_key_press(self, symbol, _):
        if symbol in self.keys:
            self.keys[symbol]()
            return EVENT_HANDLED

    def clear(self):
        self.pygwin.clear()

    def set_handler(self, event_name, handler=None):
        self.pygwin.set_handler(event_name, handler)

    def main_loop(self, world):
        pyglet.clock.schedule(world.update)
        pyglet.app.run()

