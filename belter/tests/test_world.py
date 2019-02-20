from ..world import World

def test_add_item():
    world = World()
    world.add_item('item1')
    assert world.items == {'item1'}

