from functools import partial

from pyglet import clock

from . import level
from .render import Render
from .window import Window
from .world import World

def main():
    world = World()

    window = Window()
    print(window.create("Belter"))

    render = Render(world)
    render.compile_shader()

    window.set_handler('on_draw', render.draw)
    window.set_handler('on_resize', partial(window.on_resize, render))

    for entity in level.initial_entities():
        world.add_entity(entity)

    clock.schedule_interval(render.print_frames, 1)
    window.main_loop(world)

if __name__ == "__main__":
    main()

