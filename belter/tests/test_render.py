from collections import defaultdict
import struct
from unittest.mock import call, Mock, patch

from colortuple import Color
from py2d.Math import Polygon, Vector

from ..entities import create_ship
from ..render import Render
from ..world import World

@patch('belter.render.moderngl')
def test_constructor(my_moderngl):

    render = Render(World())

    assert render.ctx == my_moderngl.create_context()
    assert render.vaos == {}
    assert render.shader is None

@patch('belter.render.moderngl')
def test_constructor_should_subscribe_to_world_on_add_entity(_):
    class MyRender(Render):
        add_entity = Mock()
    world = World()
    render = MyRender(world)
    ship = create_ship(1, 2)

    world.add_entity(ship)

    assert render.add_entity.call_args == call(ship)

def test_on_win_resize():
    render = Render(World())
    render.on_win_resize(11, 222)
    assert render.ctx.viewport == (0, 0, 11, 222)
    assert render.ortho_matrix = 0 # TODO

@patch('belter.render.moderngl')
def test_compile_shader(my_moderngl):
    render = Render(World())

    render.compile_shader()

    ctx = my_moderngl.create_context()
    assert render.shader == ctx.program()

def get_triangle():
    return Polygon.from_pointlist([
        Vector(1.1, 2.2),
        Vector(3.3, 4.4),
        Vector(5.5, 6.6),
    ])

def test_pack_verts():
    render = Render(World())
    entity = Mock(shape=get_triangle())

    actual = render.pack_verts(entity)

    assert actual == struct.pack('6f', 1.1, 2.2, 3.3, 4.4, 5.5, 6.6)

def test_pack_colors():
    render = Render(World())
    entity = Mock(
        shape=get_triangle(),
        color=Color(11, 22, 33, 44),
    )

    actual = render.pack_colors(entity)

    assert actual == struct.pack(
        '9B',
        11, 22, 33,
        11, 22, 33,
        11, 22, 33,
    )

def test_pack_indices():
    render = Render(World())
    entity = Mock()
    entity.shape = [1, 2, 3]

    actual = render.pack_indices(entity)

    assert actual == struct.pack('3B', 0, 1, 2)

def test_get_vao():
    render = Render(World())
    render.ctx = Mock()
    render.shader = 'my shader'

    actual = render.get_vao('verts', 'colors', 'indices')

    assert actual == render.ctx.vertex_array.return_value
    assert render.ctx.vertex_array.call_args == call(
        'my shader',
        [
            (render.ctx.buffer.return_value, '2f', 'vert'),
            (render.ctx.buffer.return_value, '3f1', 'color_in'),
        ],
        render.ctx.buffer.return_value,
        index_element_size=1,
    )
    assert render.ctx.buffer.call_args_list == [
        call('verts'),
        call('colors'),
        call('indices'),
    ]

def test_add_entity():
    render = Render(World())
    render.get_vao = Mock(return_value='vao')
    render.pack_verts = Mock(return_value='verts')
    render.pack_colors = Mock(return_value='colors')
    render.pack_indices = Mock(return_value='indices')
    entity = Mock()

    render.add_entity(entity)

    assert render.vaos == {id(entity): 'vao'}
    assert render.get_vao.call_args == call('verts', 'colors', 'indices')
    assert render.pack_verts.call_args == call(entity)
    assert render.pack_colors.call_args == call(entity)
    assert render.pack_indices.call_args == call(entity)

@patch('belter.render.moderngl')
def test_draw(_):
    entity1 = Mock(x=1, y=2)
    entity2 = Mock(x=3, y=4)
    world = World()
    world.entities = [entity1, entity2]
    render = Render(world)
    render.shader = defaultdict(Mock)
    positions = []
    def save_positions():
        positions.append(
            render.shader['entity_pos'].value
        )
    vao1 = Mock(render=Mock(side_effect=save_positions))
    vao2 = Mock(render=Mock(side_effect=save_positions))
    render.vaos = {
        id(entity1): vao1,
        id(entity2): vao2,
    }

    render.draw()

    assert vao1.render.call_args == call()
    assert vao2.render.call_args == call()
    assert positions == [
        (1, 2),
        (3, 4),
    ]
    assert render.ctx.finish.call_args == call()

