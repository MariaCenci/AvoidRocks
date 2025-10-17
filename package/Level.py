import pygame.image

from package.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from package.Enemy import Enemy
from package.Player import Player


class Level:

    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load('./assets/bgMenu.png').convert_alpha()

        self.player = Player((WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100))

        self.enemies = [Enemy((100, -50)), Enemy((300, -150)), Enemy((500, -250))]

    def run(self):
        game_run = True
        while game_run:
            self.window.blit(self.bg, (0, 0))

            self.player.move()
            self.window.blit(self.player.surf, self.player.rect)

            for enemy in self.enemies:
                enemy.move()
                self.window.blit(enemy.surf, enemy.rect)

                if self.player.rect.colliderect(enemy.rect):
                    print('Game over :(')
                    game_run = False

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()







