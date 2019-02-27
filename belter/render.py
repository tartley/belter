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
        world.on_add_item.subscribe(self.on_add_item)
        self.ctx = moderngl.create_context()

        # TODO untested
        window.set_handler('on_draw', self.on_draw)
        window.set_handler('on_resize')

        vbo = self.ctx.buffer(
            struct.pack('6f', 0.0, 0.8, -0.6, -0.8, 0.6, -0.8)
        )
        program = self.ctx.program(
            vertex_shader=VERTEX,
            fragment_shader=FRAGMENT,
        )
        self.vao = self.ctx.simple_vertex_array(program, vbo, 'vert')

    def on_add_item(self, item):
        pass

    def on_draw(self):
        self.window.clear()
        self.vao.render()
        self.ctx.finish()

