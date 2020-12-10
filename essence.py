import pygame
import random


class Essence(pygame.sprite.Sprite):

    def __init__(self, ns_settings, screen):
        pygame.sprite.Sprite.__init__(self)
        """" initializes essence and sets the starting position """

        self.ns_settings = ns_settings
        self.screen = screen

        # Create food at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(
            0, 0, ns_settings.essence_width, ns_settings.essence_height)

        # each new essence appers at the bottom of the screen
        self.rect.x = random.randrange(10, ns_settings.screen_width)
        self.rect.y = random.randrange(10, ns_settings.screen_height)
        self.essence_color = ns_settings.essence_color

        self.last_update = pygame.time.get_ticks()
        self.essence_timer = 10
        self.essence_dt = 0

    def draw_essence(self):
        """ Draws essence in  the current position """
        pygame.draw.rect(self.screen, self.essence_color, self.rect)
