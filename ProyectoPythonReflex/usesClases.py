import reflex as rx

class State(rx.State):
    """The app state."""

    pass

class Contador(State):
    count: int = 0
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1