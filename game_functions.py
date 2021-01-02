import sys
import pygame
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from entity import Entity
from food import Food


def check_events(ns_settings, screen,entity_group, food_group, all_sprites):
    # handles keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_graph()
            sys.exit()

        elif event.type == pygame.USEREVENT:
            new_food = Food(ns_settings, screen)
            all_sprites.add(new_food)
            food_group.add(new_food)
            data_recording(entity_group,food_group, ns_settings)
            ns_settings.counter += 0.5

def create_data():
    filename = "statistics.csv"
    with open(filename, mode="w") as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(['year', 'food', 'entity'])

def data_recording(entity_group, food_group, ns_settings):
    filename = "statistics.csv"
    year = ns_settings.counter
    food_len = len(food_group)
    entity_len = len(entity_group)
    len_all = str(food_len), str(entity_len)

    with open(filename, "a", newline="") as file:
        data = [year, food_len, entity_len]
        writer = csv.writer(file)
        writer.writerow(data)


def create_entity(ns_settings, screen, entity_group,  all_sprites):
    entity = Entity(ns_settings, screen)
    all_sprites.add(entity)
    entity_group.add(entity)


def create_food(ns_settings, screen, food_group, all_sprites):
    for i in range(50):
        foodd = Food(ns_settings, screen)
        all_sprites.add(foodd)
        food_group.add(foodd)

def screen_graph():
    fig = plt.figure()
    df = pd.read_csv("statistics.csv")

    x = df['year']
    y1 = df['food']
    y2 = df['entity']

    plt.figure(figsize=(8,5), dpi=100)
    plt.plot(x, y1, x, y2)
    plt.plot(x, y1,  label = 'food')
    plt.plot(x, y2, 'r',  label = 'entity')

    
    plt.title('Natural Selection', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()

    plt.savefig('graph.png', dpi=300)


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
                # print(" + 10 healthy ")
                create_entity(ns_settings, screen, entity_group, all_sprites)
        else:
            entity_sprite.kill()
        entity_sprite.draw_entity()
