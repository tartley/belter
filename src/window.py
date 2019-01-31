"""
Windowing, done using pyglet.
"""
import pyglet

def create():
    return pyglet.window.Window(fullscreen=True, vsync=False)

def main_loop(win):
    while not win.has_exit:
        pyglet.clock.tick()
        win.dispatch_events()
        fps = pyglet.clock.get_fps()
        label = pyglet.text.Label(f'{fps:.0f}fps', x=10, y=10, font_size=20)
        win.clear()
        label.draw()
        win.flip()

