from settings.config import *
from items import *
import pygame
import random


class Game():
    def __init__(self):
        self.__StatusBar = {
            "MainMenu": True,
            "Game": False
        }

        # Позиция для игровой доски
        self.__Outofboard = tuple(map(lambda x: x//4, self.screen_size_setup))
        pygame.init()
        pygame.mixer.init()  # для звука
        pygame.display.set_caption("Monopoly")
        self.screen = pygame.display.set_mode(self.screen_size_setup)
        self.clock = pygame.time.Clock()
        self.running = True
        self.cards_areas = []
        self.__CardsMap = []
        set_display_maxsize()

    def keyboard_control(self, event: pygame.event):
        """
        Отслеживаний действий на клавиатуре
        Args:
            event (pygame.event): передать окно в котором происходит событие
        """
        match event.type:
            case pygame.KEYDOWN:
                match event.unicode:
                    case '\x1b':  # esc (пока что просто выход)
                        if self.__StatusBar['MainMenu']:
                            exit(0)
                        else:
                            self.screen.fill(self.bg_color_setup)
                            self.__StatusBar["MainMenu"], self.__StatusBar["Game"] = self.__StatusBar["Game"], \
                                self.__StatusBar["MainMenu"]
                            self.mainmenu_game()

            case pygame.KEYUP:
                pass

    def mouse_control(self, event: pygame.event):
        """
        Модуль отслеживания мыши
        TODO: Доделать наведение на карточку(увеличение её размера) и переворот карты
        Args:
            event (pygame.event): передать окно в котором происходит событие
        """
        match event.type:
            case pygame.MOUSEMOTION:
                if self.__StatusBar['Game']:
                    for i in range(len(self.cards_areas)):
                        if (event.pos[0] in self.cards_areas[i][0]) and (event.pos[1] in self.cards_areas[i][1]):
                            self.Map.get_MapCards[i].hover = True
                            self.Map.get_MapCards[i].hovered(self.screen)
                            break
                        else:
                            self.Map.get_MapCards[i].hover = False

                    if True not in list(map(lambda x: x.hover, self.Map.get_MapCards)):
                        self.screen.blit(self.play_ground,
                                         self.play_ground_box)
                else:
                    for i in range(len(self.btn_areas)):
                        if (event.pos[0] in self.btn_areas[i][0]) and (event.pos[1] in self.btn_areas[i][1]):
                            self.mm.hover = True
                            self.mm.hovered(self.screen, i)
                            break
                        else:
                            self.mm.hover = False
                    if not self.mm.hover:
                        self.screen.blit(self.mm_hov,
                                         self.mm_hov_box)

            case pygame.MOUSEBUTTONDOWN:
                if self.__StatusBar['Game']:
                    for i in range(len(self.cards_areas)):
                        if (event.pos[0] in self.cards_areas[i][0]) and (event.pos[1] in self.cards_areas[i][1]):
                            if self.Map.get_MapCards[i].active == False:
                                self.Map.get_MapCards[i].active = True
                                Y = (
                                    (self.Map.get_MapCards[i].Size[1] + self.Map.get_MapCards[i].card_offset)*(len(self.Map.get_MapCards) - 22)//3)
                                X = (
                                    (self.Map.get_MapCards[i].Size[0] + self.Map.get_MapCards[i].card_offset)*(len(self.Map.get_MapCards) - 22)//5)*5
                                print("Нажата карта:",
                                      self.Map.get_MapCards[i].Name, "ID карты: ", self.Map.get_MapCards[i].ID)
                                self.back_card_rect = (
                                    self.screen, X, Y, self.Map.get_MapCards[i].Size[0]*5, self.Map.get_MapCards[i].Size[1]*4)
                                self.Map.get_MapCards[i].back_draw(self.screen, X, Y, (
                                    self.Map.get_MapCards[i].Size[0]*5, self.Map.get_MapCards[i].Size[1]*4))
                                break

                        if self.Map.get_MapCards[i].active == True:
                            self.Map.get_MapCards[i].active = False
                            self.screen.blit(
                                self.Map.get_MapCards[i].bg_before, (self.Map.get_MapCards[i].back_rect.x, self.Map.get_MapCards[i].back_rect.y))
                            break
                else:
                    for i in range(len(self.btn_areas)):
                        if (event.pos[0] in self.btn_areas[i][0]) and (event.pos[1] in self.btn_areas[i][1]):
                            match i:
                                case 0:
                                    self.mm.btn_animation(0)
                                    pygame.display.flip()
                                    self.__StatusBar["MainMenu"], self.__StatusBar[
                                        "Game"] = self.__StatusBar["Game"], self.__StatusBar["MainMenu"]
                                    self.screen.fill(self.bg_color_setup)

                                    self.start_game()
                                    return (True)
                                case 3:
                                    self.config_wind()
                                    return (True)
                                case 2:
                                    self.running = False

    def event_control(self):
        """
        Обработчик событий всех событий (клавиатура и мышь)
        TODO: Возможно потребуется обработка действий в отдельном потоке
        """
        for event in pygame.event.get():
            # print(event)
            self.keyboard_control(event)
            self.mouse_control(event)
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                self.running = False

    def playerlist_render(self):
        '''
        TODO: Завершить модуль по списку игроков. Нужен класс игрока
        '''
        self.Players = self.playerlist_init
        self.Players.draw(self.screen)

    def map_render(self):
        """
            Генерирует кару и карточки на карте.

        """
        self.Map = self.map_init  # Создания объекта карты
        self.cards_init  # Cоздание пустых объектов для карт
        x, y = self.__Outofboard  # Отступ от угла окна
        card_width = 80  # Ширина карты
        card_height = 120  # Высота карты
        card_counter = 0  # счетчик для обычных карт
        corner_counter = 0  # счетчик для угловых карт
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
                                x += card.Size[1] + card.card_offset
                                corner_counter += 1
                            case 1:
                                card = self.Map.get_MapCards[1]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
                                x += card.Size[1] + card.card_offset
                                corner_counter += 1
                            case 2:
                                card = self.Map.get_MapCards[2]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
                                x += card.Size[1] + card.card_offset
                                corner_counter += 1
                            case 3:
                                card = self.Map.get_MapCards[3]
                                card.XYpos = (x, y)
                                card.Size = (card_height, card_height)
                                card.draw(self.screen)
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
        # ВАЖНО! Задает области карточек в отдельный список для последующей работы
        self.cards_areas = list(
            map(lambda x: x.card_area, self.Map.get_MapCards))

    @property
    def playerlist_init(self):
        """
        Рендерит область игроков
        TODO: Доработка 
        """
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
        """
        Задает начальные параметры и инициирует объект карты

        Returns:
            Map : объект карты
        """
        Map = items.Map()
        Map.set_MapImagePath(config['FilePath']['PLAYGROUND'])
        Map.set_SessionID(random.randrange(100000000, 999999999))
        return (Map)

    @property
    def screen_size_setup(self):
        """ Выставляет параметры экрана из конфигурационного файла

        Returns:
            (width,height): (ширина,высота)
        """
        width, height = int(config['Display']['WIDTH']), int(
            config['Display']['WIDTH'])
        return (width, height)

    @property
    def bg_color_setup(self):
        """ Устанавливает цвет заднего фона

        Returns:
            color:  цвет фона
        """
        color = list(map(int, config['Screen']['BACKGROUND_COLOR'].split(",")))
        return (color)

    @property
    def fps_setup(self):
        """
        Значение ограничение частоты кадров из конфигурационного файла
        """
        return (int(config['Display']['FPS']))

    def start_game(self):
        """
        Функция запуска начала игры
        """
        self.__StatusBar["Game"], self.__StatusBar["MainMenu"] = True, False
        self.map_render()
        self.playerlist_render()

    def config_wind(self):
        """
        Окно настроек
        """
        cfg_wnd = interface.ConfigWind()
        cfg_wnd.Draw(self.screen)

    def mainmenu_game(self):
        """
        Функция запуска главного меню
        TODO: Требуется разработка
        """
        self.__StatusBar["Game"], self.__StatusBar["MainMenu"] = False, True
        self.mm = interface.MainMenu()
        self.mm.buttons_draw(self.screen)
        self.btn_areas = self.mm.get_btn_areas()
        self.mm_hov_box = Rect(0, 0, self.screen_size_setup[0], self.screen_size_setup[1])
        self.mm_hov = self.screen.subsurface(self.mm_hov_box).copy()

    def testing(self):
        """Для тестирования"""
        self.screen.fill(self.bg_color_setup)
        pygame.display.flip()  # обновление кадра
        self.mainmenu_game()
        # self.start_game()
        while self.running:
            self.clock.tick(self.fps_setup)
            self.event_control()
            pygame.display.flip()

        pygame.quit()

    def run(self):
        """
            Запускает саму игру
        """
        self.screen.fill(self.bg_color_setup)
        pygame.display.flip()  # обновление кадра
        self.mainmenu_game()
        self.start_game()
        while self.running:
            self.clock.tick(self.fps_setup)
            self.event_control()
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    Game().testing()
