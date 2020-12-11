import pygame
from pygame.locals import *
from settings import Settings
import game_functions as gf


def run_simulation():
    """initializes pygame, settings and a screen object"""
    pygame.init()
    ns_settings = Settings()
    screen = pygame.display.set_mode(
        (ns_settings.screen_width, ns_settings.screen_height))
    pygame.display.set_caption("Natural Selection")
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    entity_group = pygame.sprite.Group()
    food_group = pygame.sprite.Group()

    # creating  essence
    gf.create_entity(ns_settings, screen, all_sprites, entity_group)
    gf.create_food(ns_settings, screen, food_group, all_sprites)

    """starting the main loop simulation"""
    while True:
        hits = pygame.sprite.groupcollide(
            entity_group, food_group, False, True)
        gf.check_events(ns_settings, screen, food_group, all_sprites)
        # the screen is redrawn in every cycle
        screen.fill(ns_settings.bg_color)
        all_sprites.update()
        gf.update_screen(ns_settings, screen, entity_group,
                         food_group, all_sprites, hits)

        # displaying the last drawn screen
        pygame.display.flip()
        ns_settings.entity_dt = clock.tick(25) / 1000


run_simulation()
