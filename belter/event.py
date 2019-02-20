class Event:

    def __init__(self):
        self.listeners = set()

    def __call__(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)

    def subscribe(self, listener):
        self.listeners.add(listener)

