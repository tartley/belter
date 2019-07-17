import struct

import moderngl

VERTEX = '''\
#version 330
uniform vec2 entity_pos;
uniform float entity_rot;
uniform float zoom;
in vec2 vert;
in vec3 color_in;
out vec3 color_vert;
void main() {
    vec2 vert_rot = vec2(
        vert.x * cos(entity_rot) - vert.y * sin(entity_rot),
        vert.x * sin(entity_rot) + vert.y * cos(entity_rot));
    gl_Position = vec4(
        (entity_pos + vert_rot) * zoom,
        0.0,
        1.0);
    color_vert = color_in;
}
'''
FRAGMENT = '''\
#version 330
in vec3 color_vert;
out vec4 color;
void main() {
    color = vec4(color_vert, 1.0);
}
'''

class Render:

    def __init__(self, world):
        self.world = world
        self.ctx = moderngl.create_context()
        self.vaos = {}
        self.shader = None
        world.on_add_entity.subscribe(self.add_entity)
        self.frames = 0

    def set_viewport(self, width, height):
        self.ctx.viewport = 0, 0, width, height

    def compile_shader(self):
        self.shader = self.ctx.program(
            vertex_shader=VERTEX,
            fragment_shader=FRAGMENT,
        )

    def pack_verts(self, entity):
        assert len(entity.shape) == 3
        return struct.pack(
            '6f',
            *(
                coord
                for p in entity.shape
                for coord in (p.x, p.y)
            ),
        )

    def pack_colors(self, entity):
        assert len(entity.shape) == 3
        return struct.pack(
            '9B',
            *(
                coord
                for _ in entity.shape
                for coord in (entity.color.r, entity.color.g, entity.color.b)
            ),
        )

    def pack_indices(self, entity):
        assert len(entity.shape) < 256 # the '3B' arg
        assert len(entity.shape) == 3 # the '0, 1, 2' args
        return struct.pack(
            '3B',
            0, 1, 2,
        )

    def get_vao(self, verts, colors, indices):
        assert len(verts) < 256
        return self.ctx.vertex_array(
            self.shader,
            [
                (self.ctx.buffer(verts), '2f', 'vert'),
                (self.ctx.buffer(colors), '3f1', 'color_in'),
            ],
            self.ctx.buffer(indices),
            index_element_size=1,
        )

    def add_entity(self, entity):
        self.vaos[id(entity)] = self.get_vao(
            self.pack_verts(entity),
            self.pack_colors(entity),
            self.pack_indices(entity),
        )

    def print_frames(self, _): # dummy dt arg
        print(self.frames)
        self.frames = 0

    def draw(self):
        self.ctx.clear()
        self.shader['zoom'].value = 0.01
        for entity in self.world.entities:
            self.shader['entity_pos'].value = entity.x, entity.y
            self.shader['entity_rot'].value = entity.rot
            self.vaos[id(entity)].render()
        self.ctx.finish()
        self.frames += 1

