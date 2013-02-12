import pygame
import random

class Aliens(pygame.sprite.Sprite):
        """Enemies that we kill"""

        def __init__(self,screen_size):

            pygame.sprite.Sprite.__init__(self)
            self.screen_width, self.screen_height = screen_size
            self.image = pygame.Surface(self.rect.size)
            alien_ship = pygame.image.load('tyrian.shp.010008.png')
            pygame.sprite.Sprite.__init__(self)

            self.rect = pygame.Rect(0,0, col1)
            pygame.sprite.Group()

        def update(self):

                self.rect.move_ip(self.vx, self.vy)

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
