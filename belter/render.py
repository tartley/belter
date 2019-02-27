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

    def __init__(self, window, world):
        self.window = window
        self.world = world
        self.ctx = moderngl.create_context()
        self.vaos = {}
        self.shader = None

        world.on_add_item.subscribe(self.add_item)
        window.set_handler('on_draw', self.draw)
        window.set_handler('on_resize')

    def compile_shader(self):
        self.shader = self.ctx.program(
            vertex_shader=VERTEX,
            fragment_shader=FRAGMENT,
        )

    def get_vao(self, _):
        # TODO: untested. Should use item.shape for verts
        return self.ctx.simple_vertex_array(
            self.shader,
            self.ctx.buffer(
                struct.pack('6f', 0.0, 0.8, -0.6, -0.8, 0.6, -0.8)
            ),
            'vert'
        )

    def add_item(self, item):
        self.vaos[id(item)] = self.get_vao(item.shape)

    def draw(self):
        # todo, use ctx.clear, don't store window. don't pass window?
        # move set_handler calls up out of here?
        self.window.clear()
        for item in self.world.items:
            self.vaos[id(item)].render()
        self.ctx.finish()

