import sys
import pygame
from essence import Essence


def check_events():
    # handles keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def create_entity(ns_settings, screen,  all_sprites):
    for i in range(3):
        essence = Essence(ns_settings, screen)
        essence.last_update = ns_settings.now
        all_sprites.add(essence)


def update_screen(ns_settings,  screen, all_sprites):
    """ update the image on the screen and displays a new screen """
    # the screen is redrawn in every cycle
    screen.fill(ns_settings.bg_color)
    for essence_sprite in all_sprites.sprites():
        essence_sprite.update()
        essence_sprite.blitme()

    # displaying the last drawn screen
    pygame.display.flip()
