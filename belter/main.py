from belter.render import Render
from belter.window import Window
from belter.world import World

def main():
    world = World()
    window = Window()
    window.create("Belter")
    render = Render(window)
    window.set_on_draw(render.on_draw)
    window.main_loop(world)

if __name__ == "__main__":
    main()

