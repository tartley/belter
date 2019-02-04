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
        # TODO extract to get_keys()
        self.keys = {
            key.F10: self.toggle_fullscreen,
        }
        self.win.set_handler('on_key_press', self.on_key_press)

    def set_on_draw(self, on_draw):
        self.win.set_handler('on_draw', on_draw)

    def get_fps_display(self):
        return pyglet.window.FPSDisplay(self.win)

    def _get_next_screen(self):
        current = self.win.screen
        screens = self.win.display.get_screens()
        for index, screen in enumerate(screens):
            if screen == current:
                next_index = (index + 1) % len(screens)
                return screens[next_index]
        else:
            raise RuntimeError(f"Screen not found {current} in  {screens}")

    def toggle_fullscreen(self):
        if self.win.fullscreen:
            self.win.set_fullscreen(fullscreen=False)
        else:
            self.win.set_fullscreen(screen=self._get_next_screen())

    def clear(self):
        self.win.clear()

    def on_key_press(self, symbol, modifiers):
        if symbol in self.keys:
            self.keys[symbol]()
            return EVENT_HANDLED

    def main_loop(self, world):
        pyglet.clock.schedule(world.update)
        pyglet.app.run()

