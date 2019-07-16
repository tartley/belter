from math import cos, pi, sin

from .items import create_asteroid, create_ship

def initial_items():
    yield create_ship(0, 0)
    NUM = 24 # number of asteroids
    SPREAD = 100 # radius of circle
    RANGE = 0.75 # create ships around 0.75 of a full circle
    theta = 0
    for num in range(NUM + 1):
        yield create_asteroid(SPREAD * sin(theta), SPREAD * cos(theta))
        theta += pi * 2 / NUM * RANGE

