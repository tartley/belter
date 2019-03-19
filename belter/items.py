from colortuple import Color
import random

from py2d.Math import Polygon, Vector

class Item:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = (random.random() - 0.5) / 1000
        self.dy = (random.random() - 0.5) / 1000

    def update(self):
        self.x += self.dx
        self.y += self.dy

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
    def __init__(self, *args):
        super().__init__(*args)
        l = random.randint(25, 100)
        self.color = Color(l, l, l)

