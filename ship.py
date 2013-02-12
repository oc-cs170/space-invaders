import pygame

class Ship(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        
        pygame.sprite.Sprite.__init__(self)
        self.screen_width, self.screen_height = screen.get_size()
        
        self.sheet = pygame.image.load("tyrian.shp.010008.png").convert_alpha()
        self.ship = self.sheet.subsurface(pygame.Rect(48, 56, 48, 32))
       
        self.image = self.ship
        self.image.set_colorkey(pygame.Color(191, 220, 191))


        # The space image
        # self.ship = self.sheet.subsurface(pygame.Rect(48, 56, 48, 32))
        
        self.rect = pygame.Rect(0, 0, self.imgae.get_size())
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - (self.rect.height * 2)

        self.move = 0
        # self.rect.center = screen.get_rect().center
        
        
        # self.image = self.ship

        # Set ship location
        # self.rect = self.art.get_rect()
        # self.rect.centerx = self.image.get_rect()

