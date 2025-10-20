import pygame.image
import random

from package.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from package.Enemy import Enemy
from package.Player import Player


class Level:

    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load('./assets/bgMenu.png').convert_alpha()

        self.player = Player((WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100))

        self.enemies = [Enemy((100, -20)), Enemy((450, -100)), Enemy((630, -90)), Enemy((280, -170)),
                        Enemy((480, -220))]

        self.score = 0  # init score
        self.text_font = pygame.font.SysFont('Impact', 25)

    def run(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer_music.load('./assets/musicLevel.mp3')
        pygame.mixer_music.play(-1)  # in loop
        clock = pygame.time.Clock()
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

                if enemy.rect.bottom > WINDOW_HEIGHT:
                    enemy.rect.top = 0
                    enemy.rect.x = random.randint(0, WINDOW_WIDTH - enemy.rect.width)
                    self.score += 1

            score_surf = self.text_font.render(f'YOUR SCORE:  {self.score}', True, (255, 255, 255))
            self.window.blit(score_surf, (10, 10))

            pygame.display.flip()

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
