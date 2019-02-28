import struct
from unittest.mock import call, Mock, patch

from py2d.Math import Polygon, Vector

from ..render import Render
from ..world import World

@patch('belter.render.moderngl')
def test_constructor(my_moderngl):

    render = Render(World())

    assert render.ctx == my_moderngl.create_context()
    assert render.vaos == {}
    assert render.shader is None

@patch('belter.render.moderngl')
def test_constructor_should_subscribe_to_world_on_add_item(_):
    class MyRender(Render):
        add_item = Mock()
    world = World()
    render = MyRender(world)

    world.add_item('item1')

    assert render.add_item.call_args == call('item1')

@patch('belter.render.moderngl')
def test_compile_shader(my_moderngl):
    render = Render(World())

    render.compile_shader()

    ctx = my_moderngl.create_context()
    assert render.shader == ctx.program()

def test_get_packed_verts():
    render = Render(Mock())
    polygon = Polygon.from_pointlist([
        Vector(1.1, 2.2),
        Vector(3.3, 4.4),
        Vector(5.5, 6.6),
    ])

    actual = render.pack_vertices(polygon)

    assert actual == struct.pack('6f', 1.1, 2.2, 3.3, 4.4, 5.5, 6.6)

def test_get_vao():
    render = Render(Mock())
    render.ctx = Mock()
    render.shader = 'my shader'
    render.pack_vertices = Mock()

    actual = render.get_vao('my packed verts')

    assert actual == render.ctx.simple_vertex_array.return_value
    assert render.ctx.simple_vertex_array.call_args == call(
        'my shader',
        render.ctx.buffer.return_value,
        'vert',
    )
    assert render.ctx.buffer.call_args == call('my packed verts')

def test_add_item():
    render = Render(Mock())
    render.get_vao = Mock(return_value='my vao')
    render.pack_vertices = Mock(return_value='my packed verts')
    item = Mock()

    render.add_item(item)

    assert render.vaos == {id(item): 'my vao'}
    assert render.get_vao.call_args == call('my packed verts')
    assert render.pack_vertices.call_args == call(item.shape)

@patch('belter.render.moderngl')
def test_draw(_):
    item1 = object()
    item2 = object()
    world = Mock()
    world.items = [item1, item2]
    render = Render(world)
    vao1 = Mock()
    vao2 = Mock()
    render.vaos = {
        id(item1): vao1,
        id(item2): vao2,
    }

    render.draw()

    assert vao1.render.call_args == call()
    assert vao2.render.call_args == call()
    assert render.ctx.finish.call_args == call()

