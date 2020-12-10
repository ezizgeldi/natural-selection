import pygame

class Settings():
    """ class for storing all simulation settings """

    def __init__(self):
        """ Initializes simulation settings """

        # screen parameters
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.now = pygame.time.get_ticks()
