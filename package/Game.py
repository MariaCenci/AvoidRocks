import pygame
from package.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
from package.Menu import Menu
from package.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return == MENU_OPTIONS[0]:
                level = Level(self.window)
                level_return = level.run()
            else:
                pygame.quit()
                quit()






