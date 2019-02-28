from random import uniform

from py2d.Math import Polygon, Vector

class Ship:
    shape = Polygon.from_pointlist([
        Vector(0, 0.8),
        Vector(-0.5, -0.8),
        Vector(+0.5, -0.8),
    ])

class Asteroid:
    def __init__(self):
        self.shape = Polygon.from_pointlist([
            Vector(uniform(-1, +1), uniform(-1, +1)),
            Vector(uniform(-1, +1), uniform(-1, +1)),
            Vector(uniform(-1, +1), uniform(-1, +1)),
        ])
