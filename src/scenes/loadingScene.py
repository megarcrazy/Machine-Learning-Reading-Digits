import pygame
from src.scenes.scene import Scene
from src import constants as c


class LoadingScene(Scene):
    """
    Scene between scenes to display to the user that the next scene is
    currently loading.
    """

    def __init__(self, screen: pygame.surface.Surface) -> None:
        super().__init__(screen)
        self._my_font = pygame.font.SysFont("Comic Sans MS", size=c.TEXT_SIZE)
        self._texts = []
        self._initiate_text()
        self.render()

    def _initiate_text(self) -> None:
        """Initialise pygame text objects on the scene."""
        self._texts.append(
            self._my_font.render("Loading Please Wait", False, c.BLACK)
        )

    def update(self) -> None:
        """Method to run for each pygame frame."""
        pass

    def render(self) -> None:
        """Graphics to render each frame."""
        for i, text in enumerate(self._texts):
            self._screen.blit(text, (c.TEXT_SIZE, i * c.TEXT_SIZE))
        pygame.display.flip()
