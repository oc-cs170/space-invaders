import pygame
from invaders import Invader
from invaders import Bullet
from ship import Ship
from ship import Bunker

import random


WINDOW_TITLE = "Space Invaders"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 420
FPS = 30


class Space_Invaders(object):

    def __init__(self):
        pygame.init()

        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.SysFont("monospace", 15)

        self.new_game()


    def new_game(self):

        # Make ship and Sprite Groups
        self.ship = Ship(self.screen)
        self.ship_sprite = pygame.sprite.Group(self.ship)
        self.invader_sprites = pygame.sprite.Group()
        self.hero_bullets = pygame.sprite.Group()
        self.inv_bullets = pygame.sprite.Group()
        self.bunkers = pygame.sprite.Group()


        # Make invaders
        for i in range(10):
                badguy = Invader(self.screen, 0)
                self.invader_sprites.add(badguy)
                badguy.rect.topleft = ((WINDOW_WIDTH/4)+i*30, (WINDOW_HEIGHT/8))

        for i in range(1,3):
            for j in range(10):
                badguy = Invader(self.screen, 1)
                self.invader_sprites.add(badguy)
                badguy.rect.topleft = ((WINDOW_WIDTH/4)+j*30, (WINDOW_HEIGHT/8)+i*40)

        for i in range(3,5):
            for j in range(10):
                badguy = Invader(self.screen, 2)
                self.invader_sprites.add(badguy)
                badguy.rect.topleft = ((WINDOW_WIDTH/4)+j*30, (WINDOW_HEIGHT/8)+i*40)


        # Make Bunkers
        for i in range(100, 551, 50):
            self.bunkers.add(Bunker((i, WINDOW_HEIGHT*.8)))

        self.score = 0
        self.points = [100, 50, 20]
        self.lives = 3

        self.clock = pygame.time.Clock()
        self.now = pygame.time.get_ticks()



    def game_over(self):
        end = self.font.render("GAME OVER", 2, (255,255,0))
        self.screen.blit(end, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        pygame.display.flip()
        pygame.time.wait(3000)
        self.new_game()



    def play(self):
        running = True

        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.move = -5
                    elif event.key == pygame.K_RIGHT:
                        self.ship.move = 5
                    elif event.key == pygame.K_SPACE:
                        self.hero_bullets.add(Bullet(self.ship.rect.midtop, 'hero'))


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.ship.move = 0



            # If hero hits something
            for bullet in self.hero_bullets.sprites():
                # hits an enemy
                collision = pygame.sprite.spritecollide(bullet, self.invader_sprites, True,
                                                        pygame.sprite.collide_mask)
                if collision:
                    self.score += self.points[collision[0].bird]
                    self.hero_bullets.remove(bullet)
                    if not self.invader_sprites.sprites():
                        self.game_over()
                # hits a bunker
                bunker_hit = pygame.sprite.spritecollide(bullet, self.bunkers, False,
                                                        pygame.sprite.collide_mask)
                if bunker_hit:
                    bunker_hit[0].update(bullet)
                    self.hero_bullets.remove(bullet)



            # If enemy hits something 
            for bullet in self.inv_bullets.sprites():
                collision = pygame.sprite.spritecollide(bullet, self.ship_sprite, False,
                                                        pygame.sprite.collide_mask)
                if collision:
                    self.lives -= 1
                    if not self.lives:
                        self.ship_sprite.empty()
                        self.game_over()
                    self.inv_bullets.remove(bullet)
                bunker_hit = pygame.sprite.spritecollide(bullet, self.bunkers, False,
                                                        pygame.sprite.collide_mask)
                if bunker_hit:
                    bunker_hit[0].update(bullet)
                    self.inv_bullets.remove(bullet)



            self.ship_sprite.update()
            self.ship_sprite.draw(self.screen)

            self.hero_bullets.update()
            self.hero_bullets.draw(self.screen)

            self.inv_bullets.update()
            self.inv_bullets.draw(self.screen)

            self.bunkers.draw(self.screen)

            # Updates invaders at calculated intervals
            if (pygame.time.get_ticks() - self.now) > max(len(self.invader_sprites.sprites())*20, 100):
                self.invader_sprites.update()
                self.inv_bullets.add(Bullet(random.choice(self.invader_sprites.sprites()).rect.midbottom, 'invader'))
                # if an edge is near then change the direction all the invaders move
                if Invader.edge:
                    Invader.direction = not Invader.direction
                    Invader.edge = not Invader.edge
                    self.invader_sprites.update(30)
                self.now = pygame.time.get_ticks()
            self.invader_sprites.draw(self.screen)

            score = self.font.render("Score: " + str(self.score), 2, (255,255,0))
            self.screen.blit(score, (0, 14))
            lives = self.font.render("Lives: " + str(self.lives), 2, (255,255,0))
            self.screen.blit(lives, (0, 28))
            


            pygame.display.flip()
            self.screen.fill(pygame.Color('black'))





if __name__ == '__main__':
    game = Space_Invaders()
    game.play()
