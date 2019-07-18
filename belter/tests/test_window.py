from unittest.mock import call, patch, Mock

from pyglet.window import key
from pyglet.event import EVENT_HANDLED
import pytest

from ..window import Window

def test_constructor():
    window = Window()
    assert window.pygwin is None

@patch('belter.window.pyglet')
def test_create(mypyglet):
    window = Window()

    window.create("mytitle")

    assert mypyglet.window.Window.call_args == \
        call(
            caption='mytitle',
            config=mypyglet.gl.Config(),
            fullscreen=True,
            resizable=True,
            vsync=False
        )
    pygwin = mypyglet.window.Window()
    assert pygwin.set_handler.call_args == \
        call('on_key_press', window.on_key_press)

def test_resize():
    window = Window()
    render = Mock()

    actual = window.on_resize(render, 111, 222)

    assert actual == EVENT_HANDLED
    assert render.on_win_resize.call_args == call(111, 222)

def setup_toggle_fullscreen(screens, current):

    def set_fullscreen(fullscreen=True, screen=None):
        window.pygwin.fullscreen = fullscreen
        if screen:
            window.pygwin.screen = screen

    window = Window()
    window.pygwin = Mock(fullscreen=False)
    window.pygwin.display = Mock(get_screens=lambda: screens)
    window.pygwin.screen = current
    window.pygwin.set_fullscreen.side_effect = set_fullscreen
    return window

def test_toggle_fullscreen_one():
    window = setup_toggle_fullscreen(['s0'], 's0')
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(screen='s0')
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(fullscreen=False)
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(screen='s0')
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(fullscreen=False)

def test_toggle_fullscreen_multiple():
    window = setup_toggle_fullscreen(['s0', 's1'], 's0')
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(screen='s1')
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(fullscreen=False)
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(screen='s0')
    window.toggle_fullscreen()
    assert window.pygwin.set_fullscreen.call_args == call(fullscreen=False)

def test_toggle_fullscreen_fails():
    window = setup_toggle_fullscreen(['s0', 's1'], 's99')
    with pytest.raises(RuntimeError) as excinfo:
        window.toggle_fullscreen()
    assert str(excinfo.value) == "Current screen s99 not found in ['s0', 's1']"

def test_on_key_press_recognized():
    window = Window()
    my_toggle = Mock()
    window.keys[key.F10] = my_toggle

    actual = window.on_key_press(key.F10, "modifiers")

    assert actual == EVENT_HANDLED
    assert my_toggle.call_args == call()

def test_on_key_press_unrecognized():
    window = Window()
    actual = window.on_key_press("unrecognized", "modifiers")
    assert actual is None

def test_clear():
    window = Window()
    window.pygwin = Mock()

    window.clear()

    assert window.pygwin.clear.call_args == call()

def test_set_handler():
    window = Window()
    window.pygwin = Mock()
    my_on_draw = Mock()

    window.set_handler('my event name', my_on_draw)

    assert window.pygwin.set_handler.call_args == \
        call('my event name', my_on_draw)

@patch('belter.window.pyglet')
def test_main_loop(my_pyglet):
    window = Window()
    my_world = Mock()

    window.main_loop(my_world)

    assert my_pyglet.clock.schedule.call_args == call(my_world.update)
    assert my_pyglet.app.run.call_args == call()


