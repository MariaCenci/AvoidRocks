import pygame
from package.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from package.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            print('called menu run')
            menu.run()

    print('testing feature branch')



