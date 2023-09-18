import pygame


class Scene:
    """Abstract class that handles scenes."""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self._screen = screen
        self._buttons = []
        self._texts = []

    def update(self) -> None:
        """Method to run for each pygame frame."""
        pass

    def render(self) -> None:
        """Graphics to render each frame."""
        pass

    def emit(self) -> int:
        """
        Detect if a change scene request has been triggered when a button
        is pressed.
        """
        for button in self._buttons:
            event = button.emit()  # Check if a button is activated
            if event:
                return event
