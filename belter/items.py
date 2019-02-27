from py2d.Math import Polygon, Vector

class Ship:
    shape = Polygon.from_pointlist([
        Vector(0, 0.8),
        Vector(-0.6, -0.8),
        Vector(+0.8, -0.8),
    ])

