from functools import partial

from . import level
from .render import Render
from .window import Window
from .world import World

def main():
    world = World()

    window = Window()
    window.create("Belter")

    render = Render(world)
    render.compile_shader()

    window.set_handler('on_draw', render.draw)
    window.set_handler('on_resize', partial(window.resize, render))

    for entity in level.initial_items():
        world.add_item(entity)
    window.main_loop(world)

if __name__ == "__main__":
    main()

