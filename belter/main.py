from belter import window
from belter.render import Render
from belter.world import World

# TODO tests which run with -O off, all warnings on, for max debug
# TODO always use -O when running application
# TODO key to switch screen

def main():
    world = World()
    win = window.create()
    render = Render(win)
    win.set_handler('on_draw', render.on_draw)
    window.main_loop(world)

if __name__ == "__main__":
    main()

