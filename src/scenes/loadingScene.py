import pygame
from src.scenes.scene import Scene
from src import constants as c


class LoadingScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self._my_font = pygame.font.SysFont("Comic Sans MS", size=c.TEXT_SIZE)
        self._texts = []
        self._initiate_text()
        self.render()

    def _initiate_text(self):
        self._texts.append(
            self._my_font.render("Loading Please Wait", False, c.BLACK)
        )

    def update(self):
        pass

    def render(self):
        for i, text in enumerate(self._texts):
            self._screen.blit(text, (c.TEXT_SIZE, i * c.TEXT_SIZE))
        pygame.display.flip()
