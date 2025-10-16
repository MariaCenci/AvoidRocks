import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from package.Constants import WINDOW_WIDTH


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
            self.menu_text(60, 'Water', (255, 178, 102),(390, 145), 'Impact')
            self.menu_text(60, 'Shoot', (255, 178, 102), (538, 145), 'Impact')
            self.menu_text(35, 'START', (255, 255, 255), ((WINDOW_WIDTH / 2), 240), 'Consolas')
            self.menu_text(35, 'QUIT', (255, 255, 255), ((WINDOW_WIDTH / 2), 290), 'Consolas')
            pygame.display.flip()
            # print('before handle events')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # close window
                    print('quit')
                    quit() # end init pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple, text_font: str):
        text_font: Font = pygame.font.SysFont(name=text_font, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)














































