from .items import Asteroid, Ship

def initial_items():
    yield Ship(0, 0)
    for _ in range(20):
        yield Asteroid(0, 0)

