import itertools
import struct

import moderngl

VERTEX = '''\
#version 330
in vec2 vert;
void main() {
    gl_Position = vec4(vert, 0.0, 1.0);
}
'''
FRAGMENT = '''\
#version 330
out vec4 color;
void main() {
    color = vec4(0.30, 0.50, 1.00, 1.0);
}
'''

class Render:

    def __init__(self, world):
        self.world = world
        self.ctx = moderngl.create_context()
        self.vaos = {}
        self.shader = None
        world.on_add_item.subscribe(self.add_item)

    def compile_shader(self):
        self.shader = self.ctx.program(
            vertex_shader=VERTEX,
            fragment_shader=FRAGMENT,
        )

    def pack_vertices(self, item):
        assert len(item.shape) == 3
        verts = struct.pack(
            '6f',
            *(itertools.chain.from_iterable((p.x, p.y) for p in item.shape))
        )
        indices = struct.pack(
            '3i',
            0, 1, 2,
        )
        return verts, indices

    def get_vao(self, packed_verts, indices):
        return self.ctx.vertex_array(
            self.shader,
            [
                (self.ctx.buffer(packed_verts), '2f', 'vert'),
            ],
            self.ctx.buffer(indices),
        )

    def add_item(self, item):
        self.vaos[id(item)] = self.get_vao(*self.pack_vertices(item))

    def draw(self):
        self.ctx.clear()
        for item in self.world.items:
            self.vaos[id(item)].render()
        self.ctx.finish()

