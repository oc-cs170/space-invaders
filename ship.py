"""Ship Class"""

## 

import pygame

class Ship(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        
        pygame.sprite.Sprite.__init__(self)
        self.screen_width, self.screen_height = screen.get_size()
        
        # Load ship image
        self.sheet = pygame.image.load("tyrian.shp.010008.png").convert()
        ship = self.sheet.subsurface(pygame.Rect((96, 33), (25, 16)))
        ship = pygame.transform.scale(ship, (62, 40))     

        self.image = ship
        self.image.set_colorkey(pygame.Color('#bfdcbf'))
        
        self.rect = pygame.Rect((0, 0), self.image.get_size())
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - (self.rect.height)

        self.move = 0

    def update(self):

        # Ship moves left and right here
        self.rect.left += self.move
        self.rect.left = min(max(self.rect.left, 0), self.screen_width - self.rect.width)

