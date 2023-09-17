from typing import List
import pygame
from src import constants as c


class Button:
    """Abstract class of a pygame button."""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self._screen = screen
        self._centre_x, self._centre_y = None, None
        self._rect = None
        self._text = None
        self._emitter = None
        self._stepper = True
        self._font = pygame.font.SysFont("Comic Sans MS", 40)
        self._colour = c.MEDIUM_SEA_GREEN

    def _create_button(
        self, x: int, y: int, width: int, height: int, text: str = ""
    ) -> None:
        """Initialise button dimensions and text."""
        screen_width, screen_height = (
            self._screen.get_width(),
            self._screen.get_height(),
        )
        self._centre_x, self._centre_y = x * screen_width, y * screen_height
        self._create_rect(width, height)
        if text != "":
            self._create_text(text)

    def _create_rect(self, width: int, height: int) -> None:
        """Set the coorindates of the rectangular button corners."""
        # x and y are the proportion coefficients of the screen size
        rect = [self._centre_x, self._centre_y, width, height]
        self._rect = self._centre_rectangle(rect)

    def _create_text(self, text: str) -> None:
        """Create pygame text object."""
        self._text = self._font.render(text, True, c.BLACK)

    def update(self) -> None:
        """Method to run for each pygame frame."""
        self._check_activate()

    def render(self) -> None:
        """Render the button on the pygame application."""
        pygame.draw.rect(self._screen, self._colour, self._rect)
        if self._text is not None:
            text_rect = self._text.get_rect(
                center=(self._centre_x, self._centre_y)
            )
            self._screen.blit(self._text, text_rect)

    def _check_activate(self) -> None:
        """Check if the user has activated this button."""
        if self._check_click():
            self._activate()

    def _activate(self) -> None:
        """Execute button function."""
        pass

    def emit(self) -> None:
        """Pass scene number to scene manager."""
        return self._emitter

    def _check_hover(self) -> bool:
        """Check if the user's mouse if hovering over the button."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self._rect[0] < mouse_x < self._rect[0] + self._rect[2]:
            if self._rect[1] < mouse_y < self._rect[1] + self._rect[3]:
                return True
        return False

    def _check_click(self) -> bool:
        """
        Check if the user has clicked on the button and render button colours.
        """
        mouse_press = pygame.mouse.get_pressed()
        if self._check_hover():
            self._colour = c.SEA_GREEN
            if not self._stepper and mouse_press[0]:
                return True
            self._stepper = mouse_press[0]
        else:
            self._colour = c.MEDIUM_SEA_GREEN
            self._stepper = True
        return False

    @staticmethod
    def _centre_rectangle(rect: List[int]) -> List[int]:
        """Change centre coordinate to top left coordinate of a rectangle."""
        # Using pygame rect (start_x, start_y, width, height)
        rect[0] -= rect[2] // 2
        rect[1] -= rect[3] // 2
        return rect
