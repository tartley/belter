from functools import partial
from belter import render, window, world

import pyglet

# TODO tests which run with -O off, all warnings on, for max debug
# TODO always use -O when running application
# TODO key to switch screen

def main():
    win = window.create()
    pyglet.clock.schedule(world.update)
    win.set_handler('on_draw', lambda: render.on_draw(win))
    render.init(win)
    window.main_loop(win)

if __name__ == "__main__":
    main()

