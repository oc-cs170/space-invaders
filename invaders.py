import pygame

class Invader(pygame.sprite.Sprite):

    sheet = pygame.image.load("tyrian.shp.007D3C.png")
    ships = sheet.subsurface(pygame.Rect((23, 137), (75, 87)))
    invaders = [[None, None, None],
                [None, None, None],
                [None, None, None]]

    edge = False
    direction = True

    for i in range(3):
        for j in range(3):
            invader = ships.subsurface(pygame.Rect((j*25, i*29), (25, 29)))
            invader.set_colorkey(pygame.Color(191, 220, 191))
            invader = pygame.transform.rotate(invader, 180)
            invaders[i][j] = invader



    def __init__(self, screen, bird):
        pygame.sprite.Sprite.__init__(self)
        self.screen_width, self.screen_height = screen.get_size()
        self.stance = 1
        self.bird = bird
        self.image = self.invaders[self.bird][self.stance]
        self.rect = pygame.Rect((0, 0), self.image.get_size())




    def update(self, down=0):
        if self.stance:
            self.stance -= 1
        else:
            self.stance = 2

        if Invader.direction:
            self.rect.centerx += 20
        else:
            self.rect.centerx -= 20

        self.rect.centery += down

        self.image = self.invaders[self.bird][self.stance]

        if self.rect.right > self.screen_width*.95 or self.rect.left < self.screen_width*.05:
            Invader.edge = True





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



class Alien(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.sheet = pygame.image.load("tyrian.shp.007D3C.png")
        self.image = self.sheet.subsurface(pygame.Rect((190, 195), (15, 15)))
        self.image.set_colorkey(pygame.Color(191, 220, 191))
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = pygame.Rect((0, 0), self.image.get_size())

        self.alien_fire = 0
 
    def update(self):
        self.rect.left += 3    
