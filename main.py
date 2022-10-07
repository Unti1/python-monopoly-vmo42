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
        # Позиция для игровой доски
        self.__Outofboard = tuple(map(lambda x: x//4, self.screen_size_setup))
        pygame.init()
        pygame.mixer.init()  # для звука
        pygame.display.set_caption("Monopoly")

        self.screen = pygame.display.set_mode(self.screen_size_setup)
        self.clock = pygame.time.Clock()
        self.running = True
        self.__CardsMap = []

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

    def mouse_control(self, event: pygame.event):
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                print("Нажатие кнопкой мыши")
    """
    Обработчик событий на 
    """

    def event_control(self):
        for event in pygame.event.get():
            # print(event)
            self.keyboard_control(event)
            self.mouse_control(event)
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                self.running = False

    def playerlist_render(self):
        self.Players = self.playerlist_init
        self.Players.draw(self.screen)

    def map_render(self):
        self.Map = self.map_init
        x, y = self.__Outofboard  # Начальные координаты
        card_counter = 0
        for row in self.Map.get_MapStructure:  # вся строка
            for col in row:  # каждый символ
                if col == ".":  # для угловых карт
                    card = items.CardMap(x, y, 120, 120)
                    card.Name = f"{card_counter}"
                    card.draw(self.screen)
                    x += card.Size[1] + card.card_offset  # границы карточек
                    card_counter += 1
                elif col == "-":  # для карт по горизонтали
                    card = items.CardMap(x, y, 80, 120)
                    card.Name = f"{card_counter}"
                    card.draw(self.screen)
                    x += card.Size[0] + card.card_offset  # границы карточек
                    card_counter += 1
                elif col == "+":
                    card = items.CardMap(x, y, 120, 80)
                    card.Name = f"{card_counter}"
                    card.draw(self.screen)
                    x += card.Size[0] + card.card_offset  # границы карточек
                    card_counter += 1
                else:
                    card = None
                    x += 80 + 2  # границы карточек
            if row == self.Map.get_MapStructure[0] or row == self.Map.get_MapStructure[-1]:
                y += card.Size[0] + 2  # то же самое и с высотой
                x = self.__Outofboard[0]
            else:
                y += card.Size[1] + 2
            x = self.__Outofboard[0]
        return (x, y)

    @property
    def playerlist_init(self):
        PlayerList = interface.PlayerList()
        PlayerList.XYpos = (0, self.__Outofboard[1])
        PlayerList.Size = (400, 600)
        return (PlayerList)

    @property
    def map_init(self):
        Map = items.Map()
        Map.set_MapImagePath(config['FilePath']['PLAYGROUND'])
        Map.set_SessionID(random.randrange(100000000, 999999999))
        return (Map)

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

    def start_game(self):
        self.map_render()
        self.playerlist_render()

    def mainmenu_game(self):
        mm = interface.MainMenu()
        # mm.menu_draw(self.screen)
        mm.buttons_draw(self.screen)
        # print(mm.buttons_draw(self.screen))

    def run(self):
        self.screen.fill(self.bg_color_setup)
        pygame.display.flip()
        while self.running:
            self.start_game()
            # self.mainmenu_game()
            self.clock.tick(self.fps_setup)
            self.event_control()
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
