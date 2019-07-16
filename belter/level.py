from math import cos, pi, sin

from .items import create_asteroid, create_ship

def initial_items():
    yield create_ship(4, 0)
    NUM = 1000 # number of asteroids
    radius = 80 # radius of circle
    r_factor = 0.999
    theta = 0
    dtheta = 2 * pi / NUM * 4
    for num in range(NUM):
        yield create_asteroid(
            radius * sin(theta), radius * cos(theta),
            1 * cos(theta), -1 * sin(theta),
        )
        theta += dtheta
        radius *= r_factor

