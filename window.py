import pygame
from scenes.sceneManager import SceneManager
import constants as c


class Window:

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((c.CANVAS_SIZE, c.CANVAS_SIZE + c.TEXT_HEIGHT))
        self._scene_manager = SceneManager(self._screen)
        pygame.display.set_caption("Machine Learning Reading Digits")

    def run(self):
        clock = pygame.time.Clock()
        state = True
        while state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False

            self._screen.fill(c.WHITE)
            self._scene_manager.update()
            self._scene_manager.render()

            pygame.display.flip()
            clock.tick(c.FPS)
