from colortuple import Color
import random

from py2d.Math import Polygon, Vector

class Item:

    COLOR = Color(50, 50, 50)

    def __init__(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = self.COLOR

    def update(self):
        self.x += self.dx
        self.y += self.dy

class Ship(Item):
    shape = Polygon.from_pointlist([
        Vector(+0.0, +0.8),
        Vector(-0.5, -0.8),
        Vector(+0.5, -0.8),
    ])
    COLOR = Color(50, 100, 200)

class Asteroid(Item):
    shape = Polygon.from_pointlist([
        Vector(+0.0, -0.6),
        Vector(-0.5, +0.6),
        Vector(+0.5, +0.6),
    ])
    COLOR = Color(50, 150, 100)

