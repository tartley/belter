from ..level import initial_items
from ..models import Ship

def test_initial_items():
    actual = initial_items()

    actuals = list(actual)
    assert len(actual) > 0
    assert sum(isinstance(item, Ship) for item in actuals) == 1

