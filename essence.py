import pygame
import random


class Essence(pygame.sprite.Sprite):

    def __init__(self, ns_settings, screen):
        pygame.sprite.Sprite.__init__(self)
        """" initializes essence and sets the starting position """
        self.ns_settings = ns_settings
        self.screen = screen

        # loading an image and getting a rectangle
        self.image = pygame.image.load("p1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # each new essence appers at the bottom of the screen
        self.rect.x = random.randrange(10, ns_settings.screen_width)
        self.rect.y = random.randrange(10, ns_settings.screen_height)

        self.last_update = pygame.time.get_ticks()

    def blitme(self):
        """ Draws essence in  the current position """
        self.screen.blit(self.image,  self.rect)
