import pygame
import random
from model import Model
from dataManager import DataManager
import constants as c


class Logic:

    def __init__(self):
        self._data = []
        self._submitted = False
        self._model = None

    def update(self):
        pass

    @staticmethod
    def _await_mouse_lift():
        mouse_press = pygame.mouse.get_pressed(num_buttons=3)
        if mouse_press[0]:
            return False
        return True

    def _submit_array(self):
        pass

    def _clear(self):
        self._data[:-1] = [0 for _ in range(c.TILE_AMOUNT)]

    def _reset_data(self):
        self._data = [0 for _ in range(c.TILE_AMOUNT)] + [random.randrange(-1, 10)]

    # Checks if user is colouring tiles or is erasing
    def _request_draw(self):
        mouse_position = pygame.mouse.get_pos()
        if self._is_within_canvas(mouse_position[1]):
            mouse_press = pygame.mouse.get_pressed(num_buttons=3)
            if mouse_press[0]:
                self._draw()
            elif mouse_press[2]:
                self._erase()

    # Waits for user to submit or reset array
    def _request_submit_drawing(self):
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

    # Uses sklearn model to predict
    def _predict(self):
        self._prediction = self._model.predict([self._data[:-1]])

    # Editing Data
    def _draw(self):
        array_position = self._convert_mouse_position()
        self._data[array_position] = 1

    def _erase(self):
        array_position = self._convert_mouse_position()
        self._data[array_position] = 0

    @staticmethod
    # Converts mouse position to array position
    def _convert_mouse_position():
        mouse_position = pygame.mouse.get_pos()
        x = mouse_position[0] * c.TILE_X_AMOUNT // c.CANVAS_SIZE
        y = (mouse_position[1] - c.TEXT_HEIGHT) * c.TILE_Y_AMOUNT // c.CANVAS_SIZE
        array_position = x + y * c.TILE_X_AMOUNT
        return array_position

    @staticmethod
    # Check if the mouse in within the drawing canvas
    def _is_within_canvas(y):
        if y > c.TEXT_HEIGHT:
            return True

    # Machine Learning Model
    def _make_model(self):
        data = DataManager.get_data()
        data = DataManager.convert_data(data)
        self._model = Model(data)

    def get_data(self):
        return self._data
