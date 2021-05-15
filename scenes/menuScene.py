import pygame
from scenes.scene import Scene
from scenes.components.playButton import PlayButton
from scenes.components.trainButton import TrainButton
from scenes.components.evaluateModelButton import EvaluateModelButton
import constants as c


class MenuScene(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self._my_font = pygame.font.SysFont("Comic Sans MS", size=c.TEXT_SIZE)
        self._texts = []
        self._initiate_buttons()
        self._initiate_text()

    def _initiate_buttons(self):
        self._buttons.append(PlayButton(self._screen))
        self._buttons.append(TrainButton(self._screen))
        self._buttons.append(EvaluateModelButton(self._screen))

    def _initiate_text(self):
        self._texts.append(self._my_font.render("Escape to menu: Esc", False, c.BLACK))
        self._texts.append(self._my_font.render("Submit canvas: Space", False, c.BLACK))
        self._texts.append(self._my_font.render("Reset canvas: R", False, c.BLACK))
        self._texts.append(self._my_font.render("Draw: Left Click", False, c.BLACK))
        self._texts.append(self._my_font.render("Erase: Right Click", False, c.BLACK))

    def update(self):
        for button in self._buttons:
            button.update()

    def render(self):
        for button in self._buttons:
            button.render()
        for i, text in enumerate(self._texts):
            self._screen.blit(text, (0, i * c.TEXT_SIZE))
