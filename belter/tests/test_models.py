from py2d.Math import Polygon

from ..models import Ship

def test_Ship():
    actual = Ship()
    assert isinstance(actual.shape, Polygon)
    assert len(actual.shape) == 3

