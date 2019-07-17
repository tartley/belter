from py2d.Math import Polygon
from colortuple import Color

from ..entities import create_asteroid, create_ship

def test_ship():
    actual = create_ship(1, 2)
    assert actual.x == 1
    assert actual.y == 2
    assert isinstance(actual.color, Color)
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3

def test_asteroid():
    actual = create_asteroid(1, 2)
    assert actual.x == 1
    assert actual.y == 2
    assert isinstance(actual.color, Color)
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3

