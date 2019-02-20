from unittest.mock import call, Mock

from ..event import Event

def test_event_call_should_call_subscribers():
    m1 = Mock()
    m2 = Mock()
    event = Event()
    event.subscribe(m1)
    event.subscribe(m2)

    event('arg1', kwarg='value')

    assert m1.call_args == call('arg1', kwarg='value')
    assert m2.call_args == call('arg1', kwarg='value')

