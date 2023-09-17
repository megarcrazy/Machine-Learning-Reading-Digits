from typing import List
import random
import pygame
from src.model import Model
from src.dataManager import DataManager
from src import constants as c


class Logic:
    """Abstract class that handles user inputs for different Pygame scenes."""

    def __init__(self) -> None:
        self._data = []
        self._submitted = False
        self._playing = False
        self._model = None

    def update(self) -> None:
        """Detect user input."""
        pass

    @staticmethod
    def _await_mouse_lift() -> bool:
        """Detect if left mouse click is not pressed down."""
        mouse_press = pygame.mouse.get_pressed()
        if mouse_press[0]:
            return False
        return True

    def _submit_array(self) -> None:
        """Method to run when the user presses the "Submit Canvas" hotkey."""
        pass

    def _clear(self) -> None:
        """Empty the canvas."""
        self._data[:-1] = [0 for _ in range(c.TILE_AMOUNT)]

    def _reset_data(self) -> None:
        """
        Clear stored data that represents the data on the canvas and
        generate random number at the end of the array.
        """
        self._data = [0 for _ in range(c.TILE_AMOUNT)] + [
            random.randrange(-1, 10)
        ]

    def _request_draw(self) -> None:
        """Checks user input for filling or erasing tiles."""
        mouse_position = pygame.mouse.get_pos()
        if self._is_within_canvas(mouse_position[1]):
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                self._draw()
            elif mouse_press[2]:
                self._erase()

    def _request_submit_drawing(self) -> None:
        """Detects if user wants to submit or reset canvas array."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if not self._submitted:
                self._clear()
                self._submitted = True
        elif keys[pygame.K_SPACE]:
            if not self._submitted:
                self._submit_array()
                self._submitted = True
        else:
            self._submitted = False

    def _predict(self) -> None:
        """Uses sklearn model to predict."""
        self._prediction = self._model.predict([self._data[:-1]])

    def _draw(self) -> None:
        """Add pixel is exist to array."""
        # 1: pixel
        # 0: no pixel
        array_position = self._convert_mouse_position()
        self._data[array_position] = 1

    def _erase(self) -> None:
        """Add pixel is not exist to array."""
        # 1: pixel
        # 0: no pixel
        array_position = self._convert_mouse_position()
        self._data[array_position] = 0

    @staticmethod
    def _convert_mouse_position() -> int:
        """Converts mouse position to array position."""
        mouse_position = pygame.mouse.get_pos()
        x = mouse_position[0] * c.TILE_X_AMOUNT // c.CANVAS_SIZE
        y = (
            (mouse_position[1] - c.TEXT_HEIGHT)
            * c.TILE_Y_AMOUNT
            // c.CANVAS_SIZE
        )
        array_position = x + y * c.TILE_X_AMOUNT
        return array_position

    @staticmethod
    def _is_within_canvas(y: int) -> bool:
        """Check if the mouse in within the drawing canvas."""
        if y > c.TEXT_HEIGHT:
            return True
        return False

    # Machine Learning Model
    def _make_model(self) -> None:
        """Generate machine learning model from data file."""
        data = DataManager.get_data()
        data = DataManager.convert_data(data)
        self._model = Model(data=data, playing=self._playing)

    def get_data(self) -> List[int]:
        """Return canvas data list."""
        return self._data
