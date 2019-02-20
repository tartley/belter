from unittest.mock import call, Mock

from ..render import Render

def test_render_constructor():
    pygwin = Mock()
    render = Render(pygwin)
    assert render.window == pygwin
    assert render.fps_display == pygwin.get_fps_display.return_value

def test_on_draw():
    pygwin = Mock()
    render = Render(pygwin)

    render.on_draw()

    assert pygwin.clear.call_args == call()
    assert render.fps_display.draw.call_args == call()

