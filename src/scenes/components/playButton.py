from src.scenes.components.button import Button
from src import constants as c


class PlayButton(Button):

    def __init__(self, screen):
        super().__init__(screen)
        self._create_button(0.5, 0.25, 300, 100, "Play")

    def _activate(self):
        self._emitter = c.PLAY_SCENE_INDEX
