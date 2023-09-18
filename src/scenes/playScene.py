import pygame
from src.scenes.scene import Scene
from src.calculation.playLogic import PlayLogic
from src.scenes.components.gridTiles import GridTiles
from src import constants as c


class PlayScene(Scene):
    """
    Scene where the user draws on a canvas and the computer guesses the number.
    """

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self._my_font = pygame.font.SysFont("Comic Sans MS", size=c.TEXT_SIZE)
        self._logic = PlayLogic()
        self._gridTiles = GridTiles(self._screen)
        self._prediction = None

    def update(self) -> None:
        """Method to run for each pygame frame."""
        self._logic.update()
        self._gridTiles.update(self._logic.get_data())
        self._prediction = self._logic.get_prediction()

    def render(self) -> None:
        """Graphics to render each frame."""
        self._gridTiles.render()
        self._render_text()

    def _render_text(self) -> None:
        """Render screen pygame text."""
        # Display computer generated prediction of user drawn number
        number = "None" if self._prediction[0] == -1 else self._prediction[0]
        probability = round(self._prediction[1] * 100, 2)
        text = (
            f"Draw any number from 0 to 9. "
            f"Prediction: {number}, "
            f"Chance: {probability}%."
        )
        text_surface = self._my_font.render(text, False, c.BLACK)
        self._screen.blit(text_surface, (c.TEXT_SIZE, 0))
