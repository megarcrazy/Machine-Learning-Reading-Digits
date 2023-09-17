import pygame
from src.scenes.components.button import Button
from src import constants as c


class TrainButton(Button):
    """Button that transfers the user to the train scene."""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        super().__init__(screen)
        self._create_button(0.5, 0.50, 300, 100, "Train")

    def _activate(self) -> None:
        """Execute button function."""
        self._emitter = c.TRAIN_SCENE_INDEX
