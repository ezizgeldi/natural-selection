import random
import pygame
from pygame.locals import *


class Food(pygame.sprite.Sprite):
    """Class 'food'  to be hunted by entities"""

    def __init__(self, ns_settings, screen):
        """Creates a food object at the current position."""

        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # Create food at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(
            0, 0, ns_settings.food_width, ns_settings.food_height)

        # each new food appers at the bottom of the screen
        self.rect.x = random.randrange(10, ns_settings.screen_width)
        self.rect.y = random.randrange(10, ns_settings.screen_height)

        self.food_color = ns_settings.food_color

    def draw_food(self):
        """"Displaying food on the screen."""

        pygame.draw.rect(self.screen, self.food_color, self.rect)
