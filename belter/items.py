from colortuple import Color

from py2d.Math import Polygon, Vector

class Item:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ship(Item):
    shape = Polygon.from_pointlist([
        Vector(+0.0, +0.8),
        Vector(-0.5, -0.8),
        Vector(+0.5, -0.8),
    ])
    color = Color(50, 100, 200)

class Asteroid(Item):
    shape = Polygon.from_pointlist([
        Vector(+0.0, -0.6),
        Vector(-0.5, +0.6),
        Vector(+0.5, +0.6),
    ])
    color = Color(50, 50, 50)

