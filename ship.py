import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self, screen):

        # ship image
        pygame.sprite.Sprite.__init__(self)
        self.screen_width, self.screen_height = screen.get_size()

        self.sheet = pygame.image.load("tyrian.shp.010008.png").convert_alpha()
        self.ship = self.sheet.subsurface(pygame.Rect((96, 33), (25, 16)))
        
        self.image = self.ship
        self.image.set_colorkey(pygame.Color(191, 220, 191))

        self.rect = pygame.Rect((0, 0,) self.image.get_size())
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - self.rect.height*2

        self.move = 0

##    def update

        # where the ship updates
        # need stuff
