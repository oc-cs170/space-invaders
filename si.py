
"""Main file with game loop for Space Invaders"""


import pygame
import random
from ship import Ship

WINDOW_TITLE = 'Space Invaders'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 638


class Space_Invaders(object):
    """Create a game of Space Invaders."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Fill the screen with black while space is being created
        self.screen.fill(pygame.Color('Black'))
        pygame.display.flip()
        self.background = self.create_background(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.ship = Ship(self.screen)

    def create_background(self, width, height):
        """A black background, filled with stars... The Final Frontier.

        The background is randomly filled with 1x1 pixel white "stars" whose
        alpha (transparency) varies from 6-50%.
        """
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
        """Start Space Invaders program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """

        running = True
        while running:

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.move = -4
                    elif event.key == pygame.K_RIGHT:
                        self.ship.move = 4
                    elif event.key == pygame.K_SPACE:
                        self.hero_bullets.add(Bullet(self.ship.rect.midtop, 'hero'))


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.ship.move = 0
            
            # Draw the scene
            self.screen.blit(self.background, (0, 0))  

            # Ship image is drawn to screen.
            self.ship.update()
            self.screen.blit(self.ship.image, self.ship.rect)

            pygame.display.flip()


if __name__ == '__main__':
    game = Space_Invaders()
    game.play()
