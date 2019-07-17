from .event import Event

class World:

    def __init__(self):
        self.entities = set()
        self.on_add_entity = Event()

    def add_entity(self, entity):
        self.entities.add(entity)
        self.on_add_entity(entity)

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)

