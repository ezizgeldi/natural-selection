import sys
import pygame
from entity import Entity
from food import Food


def check_events(ns_settings, screen, food_group, all_sprites):
    # handles keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            new_food = Food(ns_settings, screen)
            all_sprites.add(new_food)
            food_group.add(new_food)


def create_entity(ns_settings, screen, entity_group,  all_sprites):
    entity = Entity(ns_settings, screen)
    all_sprites.add(entity)
    entity_group.add(entity)


def create_food(ns_settings, screen, food_group, all_sprites):
    for i in range(50):
        foodd = Food(ns_settings, screen)
        all_sprites.add(foodd)
        food_group.add(foodd)


def update_screen(ns_settings, screen, entity_group,
                  food_group, all_sprites):
    """ update the image on the screen and displays a new screen """
    # the screen is redrawn in every cycle
    screen.fill(ns_settings.bg_color)
    all_sprites.update()

    for food in food_group.sprites():
        food.draw_food()

    for entity_sprite in entity_group.sprites():
        entity_sprite.update()
        entity_sprite.draw_entity()

    # displaying the last drawn screen
        pygame.display.flip()
