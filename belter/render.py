class Render:

    def __init__(self, window, world):
        self.window = window
        world.on_add_item.subscribe(self.on_add_item)
        self.fps_display = window.get_fps_display()

    def on_add_item(self, item):
        pass

    def on_draw(self):
        self.window.clear()
        self.fps_display.draw()

