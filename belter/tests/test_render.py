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

def test_pack_vertices():
    render = Render(World())
    polygon = Polygon.from_pointlist([
        Vector(1.1, 2.2),
        Vector(3.3, 4.4),
        Vector(5.5, 6.6),
    ])
    item = Mock(shape=polygon)

    verts, indices = render.pack_vertices(item)

    assert verts == struct.pack('6f', 1.1, 2.2, 3.3, 4.4, 5.5, 6.6)
    assert indices == struct.pack('3B', 0, 1, 2)

def test_get_vao():
    render = Render(World())
    render.ctx = Mock()
    render.shader = 'my shader'

    actual = render.get_vao('verts', 'indices')

    assert actual == render.ctx.vertex_array.return_value
    assert render.ctx.vertex_array.call_args == call(
        'my shader',
        [
            (render.ctx.buffer.return_value, '2f', 'vert'),
        ],
        render.ctx.buffer.return_value,
        index_element_size=1,
    )
    assert render.ctx.buffer.call_args_list == [
        call('verts'),
        call('indices'),
    ]

def test_add_item():
    render = Render(World())
    render.get_vao = Mock(return_value='vao')
    render.pack_vertices = Mock(return_value=('verts', 'indices'))
    item = Mock()

    render.add_item(item)

    assert render.vaos == {id(item): 'vao'}
    assert render.get_vao.call_args == call('verts', 'indices')
    assert render.pack_vertices.call_args == call(item)

@patch('belter.render.moderngl')
def test_draw(_):
    item1 = object()
    item2 = object()
    world = World()
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

