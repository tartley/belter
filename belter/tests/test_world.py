from unittest.mock import call, Mock

from ..world import World

def test_add_item_should_add_to_items():
    world = World()
    world.add_item('item1')
    assert world.items == {'item1'}

def test_add_item_should_fire_event_on_add_item():
    listener = Mock()
    world = World()
    world.on_add_item.subscribe(listener)

    world.add_item('item1')

    assert listener.call_args == call('item1')

