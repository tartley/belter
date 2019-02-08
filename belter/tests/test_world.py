from belter.world import World

def test_add_items():
    world = World()
    world.add_items(['item1', 'item2'])
    assert world.items == {'item1', 'item2'}

