from colortuple import Color

from py2d.Math import Polygon, Vector

DEFAULT_COLOR = Color(50, 50, 50)

class Entity:

    def __init__(self, x, y, shape=None, color=DEFAULT_COLOR):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy

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

def create_asteroid(x, y):
    return Entity(
        x, y,
        shape=Polygon.from_pointlist([
            Vector(+0, -6),
            Vector(-5, +6),
            Vector(+5, +6),
        ]),
        color=Color(50, 150, 100),
    )

