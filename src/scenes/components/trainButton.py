from src.scenes.components.button import Button
from src import constants as c


class TrainButton(Button):
    def __init__(self, screen):
        super().__init__(screen)
        self._create_button(0.5, 0.50, 300, 100, "Train")

    def _activate(self):
        self._emitter = c.TRAIN_SCENE_INDEX
