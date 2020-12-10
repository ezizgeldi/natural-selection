import sys
import pygame
from essence import Essence
from food import Food


def check_events():
    # handles keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def create_essence(ns_settings, screen, essence_group,  all_sprites):
    for i in range(3):
        essence = Essence(ns_settings, screen)
        all_sprites.add(essence)
        essence_group.add(essence)


def create_food(ns_settings, screen, food_group, all_sprites):
    for i in range(50):
        foodd = Food(ns_settings, screen)
        all_sprites.add(foodd)
        food_group.add(foodd)


def update_screen(ns_settings, screen, essence_group,
                         food_group, all_sprites):
    """ update the image on the screen and displays a new screen """
    # the screen is redrawn in every cycle
    screen.fill(ns_settings.bg_color)
    all_sprites.update()

    for food in food_group.sprites():
        food.draw_food()

    for essence_sprite in essence_group.sprites():
        essence_sprite.update()
        essence_sprite.draw_essence()

    # displaying the last drawn screen
        pygame.display.flip()
