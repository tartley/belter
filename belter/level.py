from math import cos, pi, sin

from .items import create_asteroid, create_ship

def initial_items():
    yield create_ship(0, 0)
    NUM = 1000 # number of asteroids
    spread = 100 # radius of circle
    RANGE = 10 # how many spiral cycles
    theta = 0
    for num in range(NUM + 1):
        yield create_asteroid(
            spread * sin(theta), spread * cos(theta),
            1 * cos(theta), -1 * sin(theta),
        )
        theta += pi * 2 / NUM * RANGE
        spread *= 0.999

