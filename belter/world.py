
class World:

    def __init__(self):
        self.items = set()

    def add_items(self, items):
        for item in items:
            self.items.add(item)

    def update(self, _):
        pass

