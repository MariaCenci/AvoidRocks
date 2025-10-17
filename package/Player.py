import pygame

from package.Entity import Entity


class Player(Entity):
    def __init__(self, position: tuple):
        super().__init__('slimeGreen', position)
        self.speed = 6

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

