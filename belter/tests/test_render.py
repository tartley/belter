from unittest.mock import call, Mock, patch

from ..render import Render
from ..world import World

@patch('belter.render.moderngl')
def test_constructor(my_moderngl):
    pygwin = Mock()

    render = Render(pygwin, World())

    assert render.window == pygwin
    assert render.ctx == my_moderngl.create_context()
    assert render.vaos == {}
    assert render.shader is None

@patch('belter.render.moderngl')
def test_constructor_should_subscribe_to_world_on_add_item(_):
    class MyRender(Render):
        add_item = Mock()
    world = World()
    render = MyRender(Mock(), world)

    world.add_item('item1')

    assert render.add_item.call_args == call('item1')

def test_constructor_should_subscribe_to_window_events():
    window = Mock()

    render = Render(window, Mock())

    assert window.set_handler.call_args_list == [
        call('on_draw', render.draw),
        call('on_resize'),
    ]

@patch('belter.render.moderngl')
def test_compile_shader(my_moderngl):
    pygwin = Mock()
    render = Render(pygwin, World())

    render.compile_shader()

    ctx = my_moderngl.create_context()
    assert render.shader == ctx.program()

def test_add_item():
    render = Render(Mock(), Mock())
    render.get_vao = Mock(return_value=123)
    item = Mock()

    render.add_item(item)

    assert render.vaos == {id(item): 123}
    assert render.get_vao.call_args == call(item.shape)

@patch('belter.render.moderngl')
def test_draw(_):
    pygwin = Mock()
    item1 = object()
    item2 = object()
    world = Mock()
    world.items = [item1, item2]
    render = Render(pygwin, world)
    vao1 = Mock()
    vao2 = Mock()
    render.vaos = {
        id(item1): vao1,
        id(item2): vao2,
    }

    render.draw()

    assert pygwin.clear.call_args == call()
    assert vao1.render.call_args == call()
    assert vao2.render.call_args == call()
    assert render.ctx.finish.call_args == call()

