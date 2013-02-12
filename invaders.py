import pygame
import random


class Invaders(pygame.sprite.Sprite):
    """Controls the Invaders (enemies) that you shoot for points

    """
    def __init__(self, screen_size, size=3):
        """Create the Invaders.

        Args:
            screen_size: a 2-int tuple, the width and height of the screen
            size: an int (optional), ranging from 1-3 to determine asteroid size
        """
        # Call inherited initialization
        # super(pygame.sprite.Sprite, self).__init__()
        pygame.sprite.Sprite.__init__(self)

        # Creation parameters
        self.screen_width, self.screen_height = screen_size

        # Establish the size and location of the asteroid
        

        # Draw and load Invader's
        ships = pygame.image.load(["/tyrian.shp.010008.png"]) # "Other Image", "Other Image", "Other Image", "Final Image")
            for i in range (7):
                build_ships.append(ships)

        invader_ship_col1 = pygame.image.load('/tyrian.shp.010008.png')
        invader_ship_col2 = pygame.image.load('/tyrian.shp.010008.png') #need the rest of the images
        invader_ship_col3 = pygame.image.load('/tyrian.shp.010008.png') #need the rest of the images
        invader_ship_col4 = pygame.image.load('/tyrian.shp.010008.png') #need the rest of the images
        invader_ship_col5 = pygame.image.load('/tyrian.shp.010008.png') #need the rest of the images
        

        pygame.sprite.Sprite.__init__(self)


        
        # Initial location and velocity
        self.rect = pygame.Rect(0, 0, col1)
        invader_ships = pygame.sprite.Group(invader_ships)
        for i in range(7):
            pygame.sprite.add(invader_ship_col1)
            pygame.sprite.add(invader_ship_col2)
            pygame.sprite.add(invader_ship_col3)
            pygame.sprite.add(invader_ship_col4)
            pygame.sprite.add(invader_ship_col5)

        

    def update(self):
        """Update the position of the asteroid.

        Object moves through space at a constant velocity, wrapping when its
        leading-edge leaves the screen.
        """
        pygame.sprite.Group(invader_ships).rect.move_ip(self.vx, self.vy)

        # Vertical "leading-edge" screen wrapping
        if self.rect.bottom > self.screen_height:
            self.rect.top = 0

        elif self.rect.top < 0:
            self.rect.bottom = self.screen_height
            
        # Horizontal "leading-edge" screen wrapping
        elif self.rect.right > self.screen_width:
            self.rect.left = 0
        
        elif self.rect.left < 0:
            self.rect.right = self.screen_width