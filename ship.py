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
        col1 = (25*3, 48*3)
        col2 = (25*3, 48*4)
        col3 = (25*3, 48*5)
        col4 = (25*3, 48*6)
        for i in range(7):
            

        ship = pygame.transform.scale(ship, (62, 40))     

        self.image = ship
        self.image.set_colorkey(pygame.Color('#bfdcbf'))
        
        self.rect = pygame.Rect((0, 0), self.image.get_size())
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - self.rect.height

        self.move = 0

    def update(self):

        # Ship moves left and right here
        self.rect.left += self.move
        self.rect.left = min(max(self.rect.left, 0), self.screen_width - self.rect.width)

class Bullet(pygame.sprite.Sprite):

    bullet = pygame.Surface((3,3))
    bullet.set_colorkey(pygame.Color('black'))
    pygame.draw.circle(bullet, pygame.Color('white'), (2, 2), 2)

    def __init__(self, location, ship):
        pygame.sprite.Sprite.__init__(self)
        if ship == 










class Bullet(pygame.sprite.Sprite):
    
    bullet = pygame.Surface((4,4))
    bullet.set_colorkey(pygame.Color('black'))
    pygame.draw.circle(bullet, pygame.Color('white'), (2, 2), 2)
    
    def __init__(self, location, ship):
        pygame.sprite.Sprite.__init__(self)
        if ship == 'invader':
            self.yv = 5
        elif ship == 'hero':
            self.yv = -5

        self.image = self.bullet
        self.rect = pygame.Rect((0,0), self.image.get_size())
        self.rect.midbottom = location




    def update(self):
        self.rect.centery += self.yv

