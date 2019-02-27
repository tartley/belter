from unittest.mock import call, Mock, patch

from ..render import Render
from ..world import World

@patch('belter.render.moderngl')
def test_constructor(my_moderngl):
    pygwin = Mock()
    render = Render(pygwin, World())
    assert render.window == pygwin
    assert render.ctx == my_moderngl.create_context()

@patch('belter.render.moderngl')
def test_constructor_should_subscribe_on_add_item(_):
    called = Mock()

    class MyRender(Render):
        def on_add_item(self, item):
            called(item)

    world = World()
    render = MyRender(Mock(), world)
    render.on_add_item = Mock()

    world.add_item('item1')

    assert called.call_args == call('item1')

@patch('belter.render.moderngl')
def test_on_draw(_):
    pygwin = Mock()
    render = Render(pygwin, Mock())

    render.on_draw()

    assert pygwin.clear.call_args == call()

