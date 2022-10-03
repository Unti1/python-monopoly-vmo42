from settings.config import *
from items import *
import pygame
import random


class Game():
    def __init__(self):

        self.__StatusBar = {
            "MainMenu": False,
            "StartGame": False
        }

        pygame.init()
        pygame.mixer.init()  # для звука
        pygame.display.set_caption("Monopoly")

        self.screen = pygame.display.set_mode(self.screen_size_setup)
        self.clock = pygame.time.Clock()
        self.running = True

    """
    Контроль нажатых клавишь на клавиатуре
    """

    def keyboard_control(self, event: pygame.event):
        match event.type:
            case pygame.KEYDOWN:
                match event.unicode:
                    case '\x1b':  # esc (пока что просто выход)
                        self.running = False
            case pygame.KEYUP:
                pass
    """
    Обработчик событий на 
    """

    def event_control(self):
        for event in pygame.event.get():
            print(event)
            self.keyboard_control(event)
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                self.running = False
    @property
    def map_init(self):
        Map = items.Map()
        Map.set_MapImagePath(config['FilePath']['PLAYGROUND'])
        Map.set_SessionID(random.randrange(100000000, 999999999))
        return(Map)

    def start_game(self):
        self.Map = self.map_init()

    @property
    def screen_size_setup(self):
        width, height = int(config['Display']['WIDTH']), int(
            config['Display']['WIDTH'])
        return (width, height)

    @property
    def bg_color_setup(self):
        color = list(map(int, config['Screen']['BACKGROUND_COLOR'].split(",")))
        return (color)

    @property
    def fps_setup(self):
        return (int(config['Display']['FPS']))

    def run(self):
        self.screen.fill(self.bg_color_setup)
        pygame.display.flip()
        self.start_game()
        while self.running:
            self.clock.tick(self.fps_setup)
            self.event_control()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
