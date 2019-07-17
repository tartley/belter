from math import atan2, cos, sin
from random import randint

from colortuple import Color

from py2d.Math import Polygon, Vector

DEFAULT_COLOR = Color(50, 50, 50)

class Entity:

    def __init__(
        self, x, y, dx=0, dy=0, rot=0, drot=0, shape=None, color=DEFAULT_COLOR
    ):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rot = rot
        self.drot = drot
        self.shape = shape
        self.color = color

    def update(self, dt):
        # force due to gravity
        distance2 = self.x * self.x + self.y * self.y
        theta = atan2(self.y, self.x)
        fx = (-400 * cos(theta) / distance2) if distance2 > 10 else 0
        fy = (-400 * sin(theta) / distance2) if distance2 > 10 else 0
        # accelleration
        ddx = fx
        ddy = fy
        # position
        self.x += dt * self.dx
        self.y += dt * self.dy
        # velocity
        self.dx += dt * ddx
        self.dy += dt * ddy
        # orientation
        self.rot += dt * self.drot

def create_ship(x, y):
    return Entity(
        x, y,
        shape=Polygon.from_pointlist([
            Vector(+0, +8),
            Vector(-5, -8),
            Vector(+5, -8),
        ]),
        color=Color(50, 100, 200),
    )

def create_asteroid(x, y, **kwargs):
    bright = randint(20, 50)
    return Entity(
        x, y,
        shape=Polygon.from_pointlist([
            Vector(+0, -6),
            Vector(-5, +6),
            Vector(+5, +6),
        ]),
        color=Color(1 * bright, 3 * bright, 2 * bright),
        **kwargs,
    )

