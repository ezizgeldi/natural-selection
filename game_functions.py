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
                  food_group, all_sprites, hits):
    """ update the image on the screen and displays a new screen """

    for food in food_group.sprites():
        food.draw_food()

    for entity_sprite in entity_group.sprites():
        entity_sprite.update()
        entity_sprite.update_time()
        if entity_sprite.entity_timer >= 0:
            if entity_sprite in hits:
                entity_sprite.entity_timer += 10
                print(" + 10 healthy ")
                create_entity(ns_settings, screen, entity_group, all_sprites)
        else:
            entity_sprite.kill()
            print("was killed")
        print(entity_sprite.entity_timer)
        entity_sprite.draw_entity()
