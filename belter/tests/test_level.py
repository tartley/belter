from ..items import Asteroid, Ship
from ..level import initial_items

def test_initial_items():
    actual = initial_items()

    actuals = list(actual)
    assert len(actual) > 0
    assert sum(isinstance(item, Ship) for item in actuals) == 1
    assert sum(isinstance(item, Asteroid) for item in actuals) >= 1

