from ..items import Entity
from ..level import initial_items

def test_initial_items():
    actual = initial_items()

    actuals = list(actual)
    assert len(actuals) > 1
    for entity in actuals:
        assert isinstance(entity, Entity)
        assert isinstance(entity.x, (int, float))
        assert isinstance(entity.y, (int, float))

