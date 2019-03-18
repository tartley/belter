from .items import Asteroid, Ship

def initial_items():
    return [
        Ship(0, 0),
        Asteroid(0.5, -0.25),
    ]

