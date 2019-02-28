from py2d.Math import Polygon
from colortuple import Color

from ..items import Asteroid, Ship

def test_Ship():
    actual = Ship()
    assert isinstance(actual.color, Color)
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3

def test_Asteroid():
    actual = Asteroid()
    assert isinstance(actual.color, Color)
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3

