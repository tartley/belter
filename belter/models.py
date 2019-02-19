from py2d.Math import Polygon, Vector

class Ship:
    shape = Polygon.from_pointlist([
        Vector(0, 0),
        Vector(10, 0),
        Vector(0, 20),
    ])

