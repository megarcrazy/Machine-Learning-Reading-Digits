import pygame
from src.scenes.components.gridTiles import GridTiles
from src.calculation.trainLogic import TrainLogic
from src.scenes.scene import Scene
from src import constants as c


class TrainScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self._my_font = pygame.font.SysFont("Comic Sans MS", size=c.TEXT_SIZE)
        self._logic = TrainLogic()
        self._gridTiles = GridTiles(self._screen)

    def update(self):
        self._logic.update()
        self._gridTiles.update(self._logic.get_data())

    def render(self):
        self._gridTiles.render()
        self._render_text()

    def _render_text(self):
        data = self._logic.get_data()
        number_holder = "None" if data[-1] == -1 else data[-1]
        text = f"Draw the number: {number_holder}"
        text_surface = self._my_font.render(text, False, c.BLACK)
        self._screen.blit(text_surface, (c.TEXT_SIZE, 0))
