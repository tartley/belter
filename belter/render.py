import pyglet

fps_display = None

def init(win):
    global fps_display
    fps_display = pyglet.window.FPSDisplay(win)

def on_draw(win):
    win.clear()
    fps_display.draw()

