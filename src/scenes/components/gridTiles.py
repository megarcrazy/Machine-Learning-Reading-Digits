from typing import List
import pygame
from src import constants as c


class GridTiles:
    """Class that handles canvas pixel updates."""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self._screen = screen
        self._data = []
        self._prediction = None
        self._tile_width = c.CANVAS_SIZE // c.TILE_X_AMOUNT
        self._tile_height = c.CANVAS_SIZE // c.TILE_Y_AMOUNT

    def update(self, data: List[int]) -> None:
        """Method to run for each pygame frame."""
        self._data = data

    def render(self) -> None:
        """Render the pixels on the application canvas."""
        for i in range(len(self._data)):
            if self._data[i] == 1:
                x = (i % c.TILE_X_AMOUNT) * self._tile_width
                y = (i // c.TILE_Y_AMOUNT) * self._tile_height + c.TEXT_HEIGHT
                pygame.draw.rect(
                    self._screen,
                    c.BLACK,
                    [x, y, self._tile_width, self._tile_height],
                )
