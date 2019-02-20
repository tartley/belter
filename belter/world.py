from .event import Event

class World:

    def __init__(self):
        self.items = set()
        self.on_add_item = Event()

    def add_item(self, item):
        self.items.add(item)
        self.on_add_item(item)

    def update(self, _):
        pass

