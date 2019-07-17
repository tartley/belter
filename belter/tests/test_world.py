from unittest.mock import call, Mock

from ..entities import create_ship
from ..world import World

def test_add_entity_should_add_to_entities():
    world = World()
    ship = create_ship(1, 2)

    world.add_entity(ship)

    assert world.entities == {ship}

def test_add_entity_should_fire_event_on_add_entity():
    listener = Mock()
    world = World()
    ship = create_ship(1, 2)
    world.on_add_entity.subscribe(listener)

    world.add_entity(ship)

    assert listener.call_args == call(ship)

def test_update_should_update_all_entities():
    ship1 = create_ship(1, 2)
    ship1.update = Mock()
    ship2 = create_ship(3, 4)
    ship2.update = Mock()
    world = World()
    world.add_entity(ship1)
    world.add_entity(ship2)
    dt = 0.123

    world.update(dt)

    assert ship1.update.call_args == call(0.123)
    assert ship2.update.call_args == call(0.123)

