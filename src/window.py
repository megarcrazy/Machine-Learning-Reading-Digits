import pygame
from src.scenes.sceneManager import SceneManager
import src.constants as c


class WindowApplication:
    """Application class to run pygame application."""

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode(
            (c.CANVAS_SIZE, c.CANVAS_SIZE + c.TEXT_HEIGHT)
        )
        self._scene_manager = SceneManager(self._screen)
        pygame.display.set_caption("Machine Learning Reading Digits")

    def run(self):
        """
        Run constant loop to render application and listen to user inputs.
        """
        clock = pygame.time.Clock()
        state = True
        while state:
            # Check if exit button is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False

            # Clear pygame application image each loop
            self._screen.fill(c.WHITE)

            # Update backend and frontend of application
            self._scene_manager.update()
            self._scene_manager.render()

            pygame.display.flip()  # Draw image on application
            clock.tick(c.FPS)
