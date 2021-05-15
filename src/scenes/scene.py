class Scene:

    def __init__(self, screen):
        self._screen = screen
        self._buttons = []
        self._texts = []

    def update(self):
        pass

    def render(self):
        pass

    def emit(self):
        for button in self._buttons:
            event = button.emit()
            if event:
                return event
