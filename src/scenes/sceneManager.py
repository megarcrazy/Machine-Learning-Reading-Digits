import pygame
from src.scenes.menuScene import MenuScene
from src.scenes.playScene import PlayScene
from src.scenes.trainScene import TrainScene
from src.calculation.evaluateModelLogic import EvaluateModelLogic
from src.scenes.loadingScene import LoadingScene
from src import constants as c


class SceneManager:
    """
    A class that manages scenes. Scene manager is responsible for updating,
    rending and scene transitions.
    """

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self._screen = screen
        self._current_scene_index = c.MENU_SCENE_INDEX
        self._current_scene = MenuScene(self._screen)

    def update(self) -> None:
        """Method to run for each pygame frame."""
        self._event_listener()  # Check if there is scene change request
        self._current_scene.update()

    def render(self) -> None:
        """Graphics to render each frame."""
        self._current_scene.render()

    def _event_listener(self) -> None:
        """
        Listen to user inputs to check if there is a request for a scene
        change.
        """
        # Check if the user wants to return back to the menu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self._return_to_menu()

        # Event listeners for activate menu buttons to transfer to different
        # scenes.
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

    def _return_to_menu(self) -> None:
        """Return back to the menu scene."""
        self._current_scene_index = c.MENU_SCENE_INDEX
        self._current_scene = MenuScene(self._screen)
