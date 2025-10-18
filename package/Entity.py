import pygame

from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, name: str, position: tuple, size: tuple = None):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

        if size:
            self.surf = pygame.transform.scale(self.surf, size)

    @abstractmethod
    def move(self):
        pass
