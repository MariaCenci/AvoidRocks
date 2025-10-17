from abc import ABC

import pygame


class Entity (ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # posiçao generica
        self.speed = 0

    def move(self):
        pass