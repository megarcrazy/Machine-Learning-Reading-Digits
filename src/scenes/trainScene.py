import pygame
from src.scenes.components.gridTiles import GridTiles
from src.calculation.trainLogic import TrainLogic
from src.scenes.scene import Scene
from src import constants as c


class TrainScene(Scene):
    """
    Scene for generating new training data for the machine learning model by
    giving the user instructions to draw new numbers for the saved training
    set.
    """

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self._my_font = pygame.font.SysFont("Comic Sans MS", size=c.TEXT_SIZE)
        self._logic = TrainLogic()
        self._gridTiles = GridTiles(self._screen)

    def update(self) -> None:
        """Method to run for each pygame frame."""
        self._logic.update()
        self._gridTiles.update(self._logic.get_data())

    def render(self) -> None:
        """Graphics to render each frame."""
        self._gridTiles.render()
        self._render_text()

    def _render_text(self) -> None:
        """Render screen pygame text."""
        # Get the canvas pixel data in the form of an integer array
        data = self._logic.get_data()

        # Display the intructions for the user to create a new
        # training data set
        number_holder = "None" if data[-1] == -1 else data[-1]
        text = f"Draw the number: {number_holder}"
        text_surface = self._my_font.render(text, False, c.BLACK)
        self._screen.blit(text_surface, (c.TEXT_SIZE, 0))
