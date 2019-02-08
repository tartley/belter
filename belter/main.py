from . import level
from .render import Render
from .window import Window
from .world import World

def main():
    world = World()
    window = Window()
    window.create("Belter")
    render = Render(window)
    window.set_on_draw(render.on_draw)
    world.add_items(level.initial_items())
    window.main_loop(world)

if __name__ == "__main__":
    main()

