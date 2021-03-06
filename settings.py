import pygame


class Settings():
    """ class for storing all simulation settings """

    def __init__(self):
        """ Initializes simulation settings """

        # screen parameters
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (23, 23, 23)
        self.now = pygame.time.get_ticks()

        # food item parameters
        self.food_width = 5
        self.food_height = 5
        self.food_color = 255, 0, 255
        
        # essence item parameters
        self.entity_width = 3
        self.entity_height = 3
        self.entity_color = 255, 140, 0

        self.entity_dt = 0
        self.counter = 0 

