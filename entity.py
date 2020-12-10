import pygame
import random


class Entity(pygame.sprite.Sprite):

    def __init__(self, ns_settings, screen):
        pygame.sprite.Sprite.__init__(self)
        """" initializes entity and sets the starting position """

        self.ns_settings = ns_settings
        self.screen = screen

        # Create food at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(
            0, 0, ns_settings.entity_width, ns_settings.entity_height)

        # each new entity appers at the bottom of the screen
        self.rect.x = random.randrange(10, ns_settings.screen_width)
        self.rect.y = random.randrange(10, ns_settings.screen_height)
        self.entity_color = ns_settings.entity_color

        self.last_update = pygame.time.get_ticks()
        self.entity_timer = 10
        self.entity_dt = 0

    def draw_entity(self):
        """ Draws entity in  the current position """
        pygame.draw.rect(self.screen, self.entity_color, self.rect)
