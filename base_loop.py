import pygame
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
    # creating  essence
    gf.create_entity(ns_settings, screen, all_sprites)

    """starting the main loop simulation"""
    while True:
        gf.check_events()

        all_sprites.update()

        gf.update_screen(ns_settings, screen, all_sprites)
        clock.tick(30)


run_simulation()
