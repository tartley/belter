"""
Windowing, done using pyglet.
"""
from functools import partial

import pyglet
from pyglet.window import key
from pyglet.event import EVENT_HANDLED


class Window:

    def create(self):
        self.win = pyglet.window.Window(
            caption="Belter", fullscreen=False, vsync=False
        )
        self.keys = {
            key.F10: self.toggle_fullscreen,
        }
        self.win.set_handler('on_key_press', self.on_key_press)

    def set_on_draw(self, on_draw):
        self.win.set_handler('on_draw', on_draw)

    def get_fps_display(self):
        return pyglet.window.FPSDisplay(self.win)

    def toggle_fullscreen(self):
        self.win.set_fullscreen(fullscreen=not self.win.fullscreen)

    def clear(self):
        self.win.clear()

    def on_key_press(self, symbol, modifiers):
        if symbol in self.keys:
            self.keys[symbol]()
            return EVENT_HANDLED

    def main_loop(self, world):
        pyglet.clock.schedule(world.update)
        pyglet.app.run()

