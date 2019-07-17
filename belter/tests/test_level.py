from ..entities import Entity
from ..level import initial_entities

def test_initial_entities():
    actual = initial_entities()

    actuals = list(actual)
    assert len(actuals) > 1
    for entity in actuals:
        assert isinstance(entity, Entity)
        assert isinstance(entity.x, (int, float))
        assert isinstance(entity.y, (int, float))

