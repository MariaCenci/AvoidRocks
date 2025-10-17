import random

import pygame.key

from package.Entity import Entity


class Enemy(Entity):
    def __init__(self, position: tuple):
        super().__init__('slimeFire', position)
        self.speed = 4

    def move(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.rect.bottom = 0
            self.rect.x = random.randint(0, 900)


