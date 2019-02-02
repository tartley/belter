"""
Windowing, done using pyglet.
"""
import pyglet

def create():
    return pyglet.window.Window(
        caption="Belter", fullscreen=False, vsync=False
    )

def main_loop():
    pyglet.app.run()
