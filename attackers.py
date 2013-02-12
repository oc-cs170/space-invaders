import pygame
import random


# class Asteroid(pygame.sprite.Sprite):
#     """An asteroid that is aware of pygame.

#     A round piece of space debris that comes in 3 sizes.
#     Coordinates are the center of the asteroid.
#     """
#     def __init__(self, screen_size, size=3):
#         """Create an asteroid.

#         Args:
#             screen_size: a 2-int tuple, the width and height of the screen
#             size: an int (optional), ranging from 1-3 to determine asteroid size
#         """
#         # Call inherited initialization
#         # super(pygame.sprite.Sprite, self).__init__()
#         pygame.sprite.Sprite.__init__(self)

#         # Creation parameters
#         self.screen_width, self.screen_height = screen_size

#         # Establish the size and location of the asteroid
#         self.rect = pygame.Rect(0, 0, size * 20, size * 20)

#         # Draw a simple circle
#         self.image = pygame.Surface(self.rect.size)
#         self.image.set_colorkey(pygame.Color('Black'))  # "Transparent" color
#         color = pygame.Color('Gray')                    # Asteroid color
#         pygame.draw.circle(self.image, color, self.rect.center,
#                            self.rect.width / 2)

#         # Initial location and velocity
#         side = random.randint(1,4)
#         # top
#         if side == 1:
#             self.rect.left = random.randint(0, screen_size[0] - self.rect.width)
#             self.vy = random.randint(1, 3)
#             self.vx = random.randint(-3, 3)
            
#         # bottom
#         elif side == 2:
#             self.rect.bottom = self.screen_height
#             self.rect.left = random.randint(0, screen_size[0] - self.rect.width)
#             self.vy = random.randint(-3, -1)
#             self.vx = random.randint(-3, 3)
            
#         # left
#         elif side == 3:
#             self.rect.top = random.randint(0, screen_size[1] - self.rect.height)
#             self.vx = random.randint(1, 3)
#             self.vy = random.randint(-3, 3)
            
#         # right
#         elif side == 4:
#             self.rect.right = self.screen_width
#             self.rect.top = random.randint(0, screen_size[1] - self.rect.height)
#             self.vx = random.randint(-3, -1)
#             self.vy = random.randint(-3, 3)
        
        

#     def update(self):
        


class Attackers(pygame.sprite.Sprite):
    def __init__(self):
        
        self.sheet = pygame.image.load("tyrian.shp.007D3C.png").convert_alpha()

        # The three gorilla images
        self.attacker_row1 = self.sheet.subsurface(pygame.Rect(32, 24, 48, 32))
        self.attacker_row2 = self.sheet.subsurface(pygame.Rect(104, 56, 40, 32))
        self.attacker_row3 = self.sheet.subsurface(pygame.Rect(152, 56, 48, 32))
        
        # # This is where the gorilla stands
        # self.rect = pygame.Rect(0, 0, 40, 32)
        # self.image = self.stand
        
        # # Gorilla image for player1 is randomly placed on the left of the screen.
        # if player == 1:
        #     position = random.randint(1,2)
        # # Gorilla image for player2 is randomly placed on the right of the screen.
        # elif player == 2:
        #     position = random.randint(-3,-2)

        # # The center of the gorilla is the center of the building
        # self.rect.centerx = self.buildings[position].rect.centerx
        # # The bottom of the gorilla is the top of the building
        # self.rect.bottom = self.buildings[position].rect.top
        
    # def update(self, phase):

    #     # When phase = 3, player1's gorlla image is changed to throwing
    #     if phase == 3:
    #         self.image = self.throw_right
    #     # When phase = 6, player2's gorlla image is changed to throwing
    #     elif phase == 6:
    #         self.image = self.throw_left
    #     # When phase = 1, 2, 4, 5, both gorilla images are standing.   
    #     else:
    #         self.image = self.stand
        
        
