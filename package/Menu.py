import pygame.image
from pygame import Surface, Rect


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/bgMenu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        option_menu = 0
        pygame.mixer_music.load('./assets/music.mp3')
        pygame.mixer_music.play(-1) # in loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()
            # print('before handle events')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # close window
                    print('quit')
                    quit() # end init pygame

            # print('after handle events')






