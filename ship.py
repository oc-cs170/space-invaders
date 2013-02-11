"""Ship class"""

## Ship image is created here.
## Upadate controls when to move ship.

import pygame
import random

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        self.ship = pygame.image.load("tyrian.shp.010008.png").convert_alpha()

        # The space image
        # self.ship = self.sheet.subsurface(pygame.Rect(48, 56, 48, 32))
       
        # This is where the gorilla stands
        self.rect = pygame.Rect(0, 0, 40, 32)
        self.image = self.ship

        # Set ship location
        self.rect = self.art.get_rect()
        self.rect.centerx = self.location
        self.image = self.art
        