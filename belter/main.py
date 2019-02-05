from belter.render import Render
from belter.window import Window
from belter.world import World

# TODO tests which run with -O off, all warnings on, for max debug
# TODO always use -O when running application
# TODO key to switch screen

def main():
    world = World()
    window = Window()
    window.create("Belter")
    render = Render(window)
    window.set_on_draw(render.on_draw)
    window.main_loop(world)

if __name__ == "__main__":
    main()

