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

                for i in range(len(self.cards_areas)):
                    if (event.pos[0] in self.cards_areas[i][0]) and (event.pos[1] in self.cards_areas[i][1]):
                        print("Нажата карта:", self.Map.get_MapCards[i].Name)
                        break

    """
    Обработчик событий
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
        self.cards_init
        x, y = self.__Outofboard  # Начальные координаты
        card_width = 80
        card_height = 120
        card_counter = 0
        corner_counter = 0
        self.Map.reshuffle_cards()
        no_corners_cards = self.Map.get_MapCards[4:]
        for row in self.Map.get_MapStructure:  # вся строка
            for col in row:  # каждый символ
                match col:
                    case ".":  # для угловых карт
                        match corner_counter:
                            case 0:
                                card = self.Map.get_MapCards[0]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
                                # границы карточек
                                x += card.Size[1] + card.card_offset
                                corner_counter += 1
                            case 1:
                                card = self.Map.get_MapCards[1]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
                                # границы карточек
                                x += card.Size[1] + card.card_offset
                                corner_counter += 1
                            case 2:
                                card = self.Map.get_MapCards[2]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
                                # границы карточек
                                x += card.Size[1] + card.card_offset
                                corner_counter += 1
                            case 3:
                                card = self.Map.get_MapCards[3]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
                                # границы карточек
                                x += card.Size[0] + card.card_offset
                                corner_counter += 1
                    case "-":  # для карт по горизонтали
                        match card_counter <= 10:
                            case True:
                                card = no_corners_cards[card_counter]
                                card.XYpos = (x, y)
                                card.Size = (card_width, card_height)
                                card.draw(self.screen)
                                # границы карточек
                                x += card.Size[0] + card.card_offset
                                card_counter += 1
                            case False:
                                card = no_corners_cards[card_counter]
                                card.XYpos = (x, y)
                                card.Size = (card_width, card_height)
                                card.draw(self.screen, rotate=-180)
                                # границы карточек
                                x += card.Size[0] + card.card_offset
                                card_counter += 1
                    case "+":  # для карт по вертикали
                        match card_counter % 2:
                            case 0:
                                card = no_corners_cards[card_counter]
                                card.XYpos = (x, y)
                                card.Size = (card_width, card_height)
                                card.draw(self.screen, rotate=-90)
                                # границы карточек
                                x += card.Size[1] + card.card_offset
                                card_counter += 1
                            case 1:
                                card = no_corners_cards[card_counter]
                                card.XYpos = (x, y)
                                card.Size = (card_width, card_height)
                                card.draw(self.screen, rotate=90, miror=(0, 0))
                                # границы карточек
                                x += card.Size[1] + card.card_offset
                                card_counter += 1

                    case _:
                        x += card_width + 2  # границы карточек
            if row == self.Map.get_MapStructure[0] or row == self.Map.get_MapStructure[-1]:
                y += card_height + 2  # то же самое и с высотой
                x = self.__Outofboard[0]
            else:
                y += card_width + 2
            x = self.__Outofboard[0]
        self.cards_areas = list(map(lambda x: x.card_area, self.Map.get_MapCards))
        
    @property
    def playerlist_init(self):
        PlayerList = interface.PlayerList()
        PlayerList.XYpos = (0, self.__Outofboard[1])
        PlayerList.Size = (400, 600)
        return (PlayerList)

    @property
    def cards_init(self):
        """
            Задает массив шаблонов карточек с ориентацией на их названия.
            - Шаблоны без размеров и координат
            - Первые 4 ячейки в списке угловые
        """
        try:
            cards_img = os.listdir("assets/img/map")
            cor_count = 0
            counter = 4
            for f_name in cards_img:
                if "corner" in f_name:
                    self.Map.insert_card(cor_count, items.CardMap(
                        f_name, cor_count, 0, 0, 0, 0))
                    cor_count += 1
                elif "shans" in f_name:
                    for i in range(6):
                        self.Map.append_card(items.CardMap(
                            f_name, counter, 0, 0, 0, 0))
                        counter += 1
                else:
                    self.Map.append_card(items.CardMap(
                        f_name, counter, 0, 0, 0, 0))
                    counter += 1
            return (self.Map.get_MapCards)
        except AttributeError:
            print("Ошибка с переменной. Возможно не задан был объект \"Map\"")
        ###########################################################

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
        self.start_game()
        while self.running:
            # self.mainmenu_game()
            self.clock.tick(self.fps_setup)
            self.event_control()
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
