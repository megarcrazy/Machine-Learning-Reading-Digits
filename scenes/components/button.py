import pygame
import constants as c


class Button:

    def __init__(self, screen):
        self._screen = screen
        self._centre_x, self._centre_y = None, None
        self._rect = None
        self._text = None
        self._emitter = None
        self._stepper = True
        self._font = pygame.font.SysFont("Comic Sans MS", 40)
        self._colour = c.MEDIUM_SEA_GREEN

    # Initialising
    def _create_button(self, x, y, width, height, text=None):
        screen_width, screen_height = self._screen.get_width(), self._screen.get_height()
        self._centre_x, self._centre_y = x * screen_width, y * screen_height
        self._create_rect(width, height)
        if text is not None:
            self._create_text(text)

    def _create_rect(self, width, height):
        # x and y are the proportion coefficients of the screen size
        rect = [self._centre_x, self._centre_y, width, height]
        self._rect = self._centre_rectangle(rect)

    def _create_text(self, text):
        self._text = self._font.render(text, True, c.BLACK)

    # Updating
    def update(self):
        self._check_activate()

    # Rendering
    def render(self):
        pygame.draw.rect(self._screen, self._colour, self._rect)
        if self._text is not None:
            text_rect = self._text.get_rect(center=(self._centre_x, self._centre_y))
            self._screen.blit(self._text, text_rect)

    # Requesting
    def _check_activate(self):
        if self._check_click():
            self._activate()

    # Execute button function
    def _activate(self):
        pass

    # Pass method to scene manager
    def emit(self):
        return self._emitter

    # Helper

    def _check_hover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self._rect[0] < mouse_x < self._rect[0] + self._rect[2]:
            if self._rect[1] < mouse_y < self._rect[1] + self._rect[3]:
                return True
        return False

    def _check_click(self):
        mouse_press = pygame.mouse.get_pressed(num_buttons=3)
        if self._check_hover():
            self._colour = c.SEA_GREEN
            if not self._stepper and mouse_press[0]:
                return True
            self._stepper = mouse_press[0]
        else:
            self._colour = c.MEDIUM_SEA_GREEN
            self._stepper = True
        return False

    # Change centre coordinate to top left coordinate of a rectangle
    @staticmethod
    def _centre_rectangle(rect):
        # Using pygame rect [start_x, start_y, width, height]
        rect[0] -= rect[2] // 2
        rect[1] -= rect[3] // 2
        return rect
