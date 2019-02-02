"""
Windowing, done using pyglet.
"""
import time
import pyglet

def create():
    return pyglet.window.Window(caption="Belter", fullscreen=False, vsync=False)

def main_loop(win):
    pyglet.app.run()
