import pygame
import random
from aliens import Aliens
from ship import Ship

WINDOW_TITLE = "SPACE INVADERS"
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 738

class Space_Invaders(object):
    """Create a game for Space Invaders"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill(pygame.Color('Black'))
        pygame.display.flip()
        self.background = self.new_background(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.ship= Ship(self.screen)

    def new_background(self, width, height):
        """Took this from asteroids background"""
        # Copy space from the main screen surface
        space = self.screen.copy()
        space.fill(pygame.Color('Black'))

        # Create a single pixel "star"
        star = pygame.Surface((1, 1))
        star.fill(pygame.Color('White'))

        # Randomly choose coordinates to blit a randomly bright "star"
        for i in range(0, width, 2):
            for j in range(0, height, 2):
                if random.randint(1, 1000) <= 3:             # 0.3% is a star
                    star.set_alpha(random.randint(16, 128))  # Random brightness
                    space.blit(star, (i, j))
        return space

    def play(self):
        
        running = True
        while running:

            #Even Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                   
                    if event.key == pygame.K_LEFT:
                        self.ship.move = -4
                    elif event.key == pygame.K_RIGHT:
                        self.ship.move = 4
##                    elif event.key == pygame.K_SPACE:
##                        self.ship.bullets
                
            self.screen.blit(self.background, (0,0))
            self.ship_spite.draw(self.screen)
            pygame.display.flip()

if __name__ =='__main__':
    game = Space_Invaders()
    game.play

      
