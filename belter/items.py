from colortuple import Color

from py2d.Math import Polygon, Vector

class Ship:
    shape = Polygon.from_pointlist([
        Vector(+0.0, +0.8),
        Vector(-0.5, -0.8),
        Vector(+0.5, -0.8),
    ])
    color = Color(0.5, 0.6, 0.7)

class Asteroid:
    shape = Polygon.from_pointlist([
        Vector(+0.0, -0.6),
        Vector(-0.5, +0.6),
        Vector(+0.5, +0.6),
    ])
    color = Color(0.5, 0.7, 0.6)

