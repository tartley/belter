from unittest.mock import call, patch, Mock

from pyglet.window import key
from pyglet.event import EVENT_HANDLED
import pytest

from belter.window import Window

def test_constructor():
    window = Window()
    assert window.win is None

@patch('belter.window.pyglet')
def test_create(mypyglet):
    window = Window()

    window.create("mytitle")

    assert mypyglet.window.Window.call_args == \
        call(caption='mytitle', fullscreen=False, vsync=False)
    win = mypyglet.window.Window.return_value
    assert win.set_handler.call_args == \
        call('on_key_press', window.on_key_press)

def setup_toggle_fullscreen(screens, current):

    def set_fullscreen(fullscreen=True, screen=None):
        window.win.fullscreen = fullscreen
        if screen:
            window.win.screen = screen

    window = Window()
    window.win = Mock(fullscreen=False)
    window.win.display = Mock(get_screens=lambda: screens)
    window.win.screen = current
    window.win.set_fullscreen.side_effect = set_fullscreen
    return window

def test_toggle_fullscreen_one():
    window = setup_toggle_fullscreen(['s0'], 's0')
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(screen='s0')
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(fullscreen=False)
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(screen='s0')
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(fullscreen=False)

def test_toggle_fullscreen_multiple():
    window = setup_toggle_fullscreen(['s0', 's1'], 's0')
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(screen='s1')
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(fullscreen=False)
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(screen='s0')
    window.toggle_fullscreen()
    assert window.win.set_fullscreen.call_args == call(fullscreen=False)

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

@patch('belter.window.pyglet.window.FPSDisplay')
def test_get_fps_display(my_fps_display):
    window = Window()
    window.win = Mock()

    actual = window.get_fps_display()

    assert actual == my_fps_display.return_value
    assert my_fps_display.call_args == call(window.win)

def test_clear():
    window = Window()
    window.win = Mock()

    window.clear()

    assert window.win.clear.call_args == call()

def test_set_on_draw():
    window = Window()
    window.win = Mock()
    my_on_draw = Mock()

    window.set_on_draw(my_on_draw)

    assert window.win.set_handler.call_args == call('on_draw', my_on_draw)

@patch('belter.window.pyglet')
def test_main_loop(my_pyglet):
    window = Window()
    my_world = Mock()

    window.main_loop(my_world)

    assert my_pyglet.clock.schedule.call_args == call(my_world.update)
    assert my_pyglet.app.run.call_args == call()


