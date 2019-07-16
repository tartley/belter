from math import atan2, cos, sin
from random import randint, uniform

from colortuple import Color

from py2d.Math import Polygon, Vector

DEFAULT_COLOR = Color(50, 50, 50)

class Entity:

    def __init__(self, x, y, dx=0, dy=0, shape=None, color=DEFAULT_COLOR):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.shape = shape
        self.color = color

    def update(self):
        self.x += self.dx
        self.y += self.dy
        distance2 = self.x * self.x + self.y * self.y
        theta = atan2(self.y, self.x)
        self.dx -= 0.01 * cos(theta) / min(distance2, 1)
        self.dy -= 0.01 * sin(theta) / min(distance2, 1)

def create_ship(x, y):
    return Entity(
        x, y + 1,
        shape=Polygon.from_pointlist([
            Vector(+0, +8),
            Vector(-5, -8),
            Vector(+5, -8),
        ]),
        color=Color(50, 100, 200),
    )

def create_asteroid(x, y, dx=None, dy=None):
    bright = randint(20, 50)
    return Entity(
        x, y,
        dx=dx, dy=dy,
        shape=Polygon.from_pointlist([
            Vector(+0, -6),
            Vector(-5, +6),
            Vector(+5, +6),
        ]),
        color=Color(bright, 3 * bright, 2 * bright),
    )

