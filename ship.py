import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self, screen):

        pygame.sprite.Sprite.__init__(self)
        self.screen_width, self.screen_height = screen.get_size()

        self.sheet = pygame.image.load("tyrian.shp.010008.png")
        self.ship = self.sheet.subsurface(pygame.Rect((96, 33), (25, 16)))
        
        self.image = self.ship
        self.image.set_colorkey(pygame.Color(191, 220, 191))

        self.rect = pygame.Rect((0, 0), self.image.get_size())
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - self.rect.height*2

        self.move = 0

    def update(self):
        self.rect.left += self.move
        self.rect.left = min(max(self.rect.left, 0), self.screen_width - self.rect.width)



class Bunker(pygame.sprite.Sprite):


    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        bunker = pygame.Surface((30, 20))
        bunker.set_colorkey(pygame.Color('black'))
        pygame.draw.circle(bunker, pygame.Color('green'), (15, 20), 20)
        pygame.draw.circle(bunker, pygame.Color('black'), (15, 20), 5)
        self.image = bunker
        self.rect = pygame.Rect((0, 0), self.image.get_size())
        self.rect.center = location


    def update(self, bullet):
        hole = (bullet.rect.centerx - self.rect.left, bullet.rect.top - self.rect.top)
        pygame.draw.circle(self.image, pygame.Color('black'), hole, 4)