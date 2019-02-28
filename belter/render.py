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

    def get_packed_vertices(self, _):
        # TODO, should used passed polygon
        return self.ctx.buffer(
            struct.pack('6f', 0.0, 0.8, -0.6, -0.8, 0.6, -0.8)
        )

    def get_vao(self, packed_verts):
        return self.ctx.simple_vertex_array(self.shader, packed_verts, 'vert')

    def add_item(self, item):
        self.vaos[id(item)] = self.get_vao(
            self.get_packed_vertices(item.shape)
        )

    def draw(self):
        self.ctx.clear()
        for item in self.world.items:
            self.vaos[id(item)].render()
        self.ctx.finish()

