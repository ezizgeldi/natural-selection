import pygame
from pygame.locals import *

from pygame.sprite import Group

from settings import Settings
from essence import Essence
import game_functions as gf


def run_simulation():
    """initializes pygame, settings and a screen object"""
    pygame.init()
    ns_settings = Settings()
    screen = pygame.display.set_mode(
        (ns_settings.screen_width, ns_settings.screen_height))
    pygame.display.set_caption("Natural Selection")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    essence_group = pygame.sprite.Group()
    food_group = pygame.sprite.Group()

    # creating  essence
    gf.create_essence(ns_settings, screen, all_sprites, essence_group)
    gf.create_food(ns_settings, screen, food_group, all_sprites)

    """starting the main loop simulation"""
    while True:
        gf.check_events()
        # the screen is redrawn in every cycle
        screen.fill(ns_settings.bg_color)
        all_sprites.update()

        gf.update_screen(ns_settings, screen, essence_group,
                         food_group, all_sprites)


        clock.tick(30)


run_simulation()
