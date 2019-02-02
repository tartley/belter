import pyglet

from belter import window, world
from belter.render import Render

# TODO tests which run with -O off, all warnings on, for max debug
# TODO always use -O when running application
# TODO key to switch screen

def main():
    win = window.create()
    pyglet.clock.schedule(world.update)
    render = Render(win)
    win.set_handler('on_draw', render.on_draw)
    window.main_loop()

if __name__ == "__main__":
    main()

