from unittest.mock import call, Mock

from ..render import Render
from ..world import World

def test_constructor():
    pygwin = Mock()
    render = Render(pygwin, World())
    assert render.window == pygwin
    assert render.fps_display == pygwin.get_fps_display.return_value

def test_constructor_should_subscribe_on_add_item():
    called = Mock()

    class MyRender(Render):
        def on_add_item(self, item):
            called(item)

    world = World()
    render = MyRender(Mock(), world)
    render.on_add_item = Mock()

    world.add_item('item1')

    assert called.call_args == call('item1')

def test_on_draw():
    pygwin = Mock()
    render = Render(pygwin, Mock())

    render.on_draw()

    assert pygwin.clear.call_args == call()
    assert render.fps_display.draw.call_args == call()

