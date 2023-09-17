import pygame
from src.scenes.components.button import Button
from src import constants as c


class PlayButton(Button):
    """Button that transfers the user to the play scene."""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        super().__init__(screen)
        self._create_button(0.5, 0.25, 300, 100, "Play")

    def _activate(self) -> None:
        """Execute button function."""
        self._emitter = c.PLAY_SCENE_INDEX
