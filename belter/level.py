from math import cos, pi, sin

from .items import Asteroid, Ship

def initial_items():
    yield Ship(0, 0)
    NUM = 24
    RANGE = 0.75 # create ships around 0.75 of a full circle
    theta = 0
    for num in range(NUM):
        yield Asteroid(sin(theta), cos(theta))
        theta += pi * 2 / NUM * RANGE

