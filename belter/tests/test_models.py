from ..models import Ship

def test_Ship():
    actual = Ship()
    assert isinstance(actual, Ship)

