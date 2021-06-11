import pygame
from src.scenes.menuScene import MenuScene
from src.scenes.playScene import PlayScene
from src.scenes.trainScene import TrainScene
from src.calculation.evaluateModelLogic import EvaluateModelLogic
from src.scenes.loadingScene import LoadingScene
from src import constants as c


class SceneManager:

    def __init__(self, screen):
        self._screen = screen
        self._current_scene_index = c.MENU_SCENE_INDEX
        self._current_scene = MenuScene(self._screen)

    def update(self):
        self._event_listener()
        self._current_scene.update()

    def render(self):
        self._current_scene.render()

    def _event_listener(self):
        self._back_to_menu_listener()
        event = self._current_scene.emit()
        if event is not None:
            LoadingScene(self._screen)
            if event == c.PLAY_SCENE_INDEX:
                self._current_scene = PlayScene(self._screen)
            elif event == c.TRAIN_SCENE_INDEX:
                self._current_scene = TrainScene(self._screen)
            elif event == c.EVALUATE_MODEL_SCENE_INDEX:
                EvaluateModelLogic()
                self._return_to_menu()

    def _back_to_menu_listener(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self._return_to_menu()

    def _return_to_menu(self):
        self._current_scene_index = c.MENU_SCENE_INDEX
        self._current_scene = MenuScene(self._screen)
