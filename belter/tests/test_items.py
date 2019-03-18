from py2d.Math import Polygon
from colortuple import Color

from ..items import Asteroid, Ship

def test_Ship():
    actual = Ship(1, 2)
    assert isinstance(actual.color, Color)
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3
    assert actual.x == 1
    assert actual.y == 2

def test_Asteroid():
    actual = Asteroid(3, 4)
    assert isinstance(actual.color, Color)
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3
    assert actual.x == 3
    assert actual.y == 4

