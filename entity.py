import pygame
import random


class Entity(pygame.sprite.Sprite):

    def __init__(self, ns_settings, screen):
        pygame.sprite.Sprite.__init__(self)
        """" initializes entity and sets the starting position """

        self.ns_settings = ns_settings
        self.screen = screen

        # Create food at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(
            0, 0, ns_settings.entity_width, ns_settings.entity_height)

        # each new entity appers at the bottom of the screen
        self.rect.x = random.randint(10, ns_settings.screen_width)
        self.rect.y = random.randint(10, ns_settings.screen_height)
        self.entity_color = ns_settings.entity_color
        self.speed = random.randrange(1, 3)  # cell speed
        self.move = [None, None]  # realtive x and y coordinates to move to
        self.direction = None  # movement direction

        self.last_update = pygame.time.get_ticks()
        self.entity_timer = 30
        self.entity_dt = 0

    def update(self):
        """Метод движения машин"""
        directions = {
            "S": ((-1, 2), (1, self.speed)),  # down
            "SW": ((-self.speed, -1), (1, self.speed)),
            "W": ((-self.speed, -1), (-1, 2)),  # left
            "NW": ((-self.speed, -1), (-self.speed, -1)),
            "N": ((-1, 2), (-self.speed, -1)),  # up
            "NE": ((1, self.speed), (-self.speed, -1)),
            "E": ((1, self.speed), (-1, 2)),  # E
            "SE": ((1, self.speed), (1, self.speed))
        }

        directionsName = (
            "S", "SW", "W", "NW", "N", "NE", "E", "SE"
        )
        if random.randint(0, 5) == 2:  # move about once every 5 frames
            if self.direction == None:  # if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                # get the index of direction in directions list
                a = directionsName.index(self.direction)
                # set the direction to be the same, or one next to the current direction
                b = random.randint(a-1, a+2)
                # if direction index is outside the list, move back to the start
                if b > len(directionsName)-1:
                    b = 0
                self.direction = directionsName[b]
            self.move[0] = random.randint(
                directions[self.direction][0][0],
                directions[self.direction][0][1])
            self.move[1] = random.randint(
                directions[self.direction][1][0],
                directions[self.direction][1][1])
        # if cell is near the border of the screen, change direction
        if self.rect.x < 5 or self.rect.x > self.ns_settings.screen_width - 5 or self.rect.y < 5 or self.rect.y > self.ns_settings.screen_height - 5:

            if self.rect.x < 5:
                self.direction = "E"
            if self.rect.x > self.ns_settings.screen_width - 5:
                self.direction = "W"
            if self.rect.y < 5:
                self.direction = "S"
            if self.rect.y > self.ns_settings.screen_height - 5:
                self.direction = "N"

            self.move[0] = random.randint(
                directions[self.direction][0][0],
                directions[self.direction][0][1])
            # change relative x to a random number between min x and max x
            self.move[1] = random.randint(
                directions[self.direction][1][0],
                directions[self.direction][1][1])
            # change relative x to a random number between min x and max x
        if self.move[0] != None:  # add the relative coordinates to the cells coordinates
            self.rect.x += self.move[0]
            self.rect.y += self.move[1]

    def update_time(self):
        self.entity_timer -= self.ns_settings.entity_dt
        return self.entity_timer

    def draw_entity(self):
        """ Draws entity in  the current position """
        pygame.draw.rect(self.screen, self.entity_color, self.rect)
