from settings.config import *
from items import *
import pygame
from items.player import Player

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
        display.set_caption("Монополия")

        self.screen = pygame.display.set_mode(self.screen_size_setup)
        self.clock = pygame.time.Clock()
        self.running = True
        self.__CardsMap = []

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
                        self.running = False
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
                for i in range(len(self.cards_areas)):
                    if (event.pos[0] in self.cards_areas[i][0]) and (event.pos[1] in self.cards_areas[i][1]):
                        self.Map.get_MapCards[i].hover = True
                        self.Map.get_MapCards[i].hovered(self.screen)
                        break
                    else:
                        self.Map.get_MapCards[i].hover = False

                if True not in list(map(lambda x: x.hover, self.Map.get_MapCards)):
                    self.screen.blit(
                        self.play_ground, self.play_ground_box)

            case pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.cards_areas)):
                    if (event.pos[0] in self.cards_areas[i][0]) and (event.pos[1] in self.cards_areas[i][1]):
                        if self.Map.get_MapCards[i].active == False:
                            self.Map.get_MapCards[i].active = True
                            Y_centering = (
                                self.Map.get_MapCards[i].Size[1]*(len(self.Map.get_MapCards) - 22)//3)
                            X_centering = (
                                self.Map.get_MapCards[i].Size[0]*(len(self.Map.get_MapCards) - 22)//2)
                            print("Нажата карта:",
                                  self.Map.get_MapCards[i].Name)
                            self.Map.get_MapCards[i].back_draw(self.screen, X_centering, Y_centering, (
                                self.Map.get_MapCards[i].Size[0]*3, self.Map.get_MapCards[i].Size[1]*3))
                            break

                    if self.Map.get_MapCards[i].active == True:
                        self.Map.get_MapCards[i].active = False
                        self.screen.blit(
                            self.play_ground, self.play_ground_box)
                        break

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
        self.Map.reshuffle_cards  # Тасовка карт на поле
        x, y = self.__Outofboard  # Отступ от угла окна
        card_width = 80  # Ширина карты
        card_height = 120  # Высота карты
        card_counter = 0  # счетчик для обычных карт
        corner_counter = 0  # счетчик для угловых карт
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
                                card.draw(self.screen, rotate=90,
                                          miror=(0, 0))
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
        self.Map.set_MapSize(
            (self.Map.get_MapCards[0].Size[0]*2 + (self.Map.get_MapCards[5].Size[0] + self.Map.get_MapCards[5].card_offset)
             * 9, (self.Map.get_MapCards[5].Size[1] + self.Map.get_MapCards[5].card_offset)*10)
        )
        self.play_ground_box = Rect(
            self.__Outofboard[0] - 100, self.__Outofboard[1] - 100, self.Map.get_MapSize[0]+100, self.Map.get_MapSize[0]+100)
        self.play_ground = self.screen.subsurface(self.play_ground_box).copy()
        self.cards_areas = list(
            map(lambda x: x.card_area, self.Map.get_MapCards))

    @ property
    def playerlist_init(self):
        """
        Рендерит область игроков
        TODO: Доработка
        """
        PlayerList = interface.PlayerList()
        PlayerList.XYpos = (0, self.__Outofboard[1])
        PlayerList.Size = (400, 600)
        return (PlayerList)

    @ property
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

    @ property
    def map_init(self) -> items.Map:
        """
        Задает начальные параметры и инициирует объект карты

        Returns:
            Map : объект карты
        """
        Map = items.Map()
        Map.set_MapImagePath(config['FilePath']['PLAYGROUND'])
        Map.set_SessionID(random.randrange(100000000, 999999999))
        return (Map)

    @ property
    def screen_size_setup(self):
        """ Выставляет параметры экрана из конфигурационного файла

        Returns:
            (width,height): (ширина,высота)
        """
        width, height = int(config['Display']['WIDTH']), int(
            config['Display']['WIDTH'])
        return (width, height)

    @ property
    def bg_color_setup(self):
        """ Устанавливает цвет заднего фона

        Returns:
            color:  цвет фона
        """
        color = list(map(int, config['Screen']['BACKGROUND_COLOR'].split(",")))
        return (color)

    @ property
    def fps_setup(self):
        """
        Значение ограничение частоты кадров из конфигурационного файла
        """
        return (int(config['Display']['FPS']))

    def start_game(self):
        """
        Функция запуска начала игры
        """
        self.map_render()
        self.playerlist_render()
        self.create_player()

    def create_player(self):
        """ 
        Функция инициализации игроков
        """

        count_players = 3  # len(self.Players) нужно взять количество игроков
        players = [Player() for _ in range(count_players)]
        self.Map.set_CurrentUsersList(players)

    def move_player(self, points: int, player_id: str):
        """ """
        x, y = self.Map.get_MapSize # или вынести за функцию
        players = self.Map.get_CurrentUsersList
        cards = self.Map.get_MapCards
        index = 0
        for i in range(len(players)):
            if players[i].get_id() == player_id:
                index = i
                break
        
        for i in range(points):
            current_card_ID = players[index].get_current_card_ID()
            for card in cards:
                if card.ID == current_card_ID:
                    if card.ID in (0, 9, 19, 29):
                        players[index].rotate(90) # повернуть угол, если на карточка угловая
                    players[index].change_pos(card.XYpos)
                    players[index].change_current_card(1)
                    players[index].offset_player()
                    # отрисовать скин в соответствие с новыми координатами и углом


    def mainmenu_game(self):
        """
        Функция запуска главного меню
        TODO: Дорабатывается Игорем 
        """
        mm = interface.MainMenu()
        # mm.menu_draw(self.screen)
        mm.buttons_draw(self.screen)
        # print(mm.buttons_draw(self.screen))

    def testing(self):
        """Для тестирования
        TODO: Доделать взаимодействие с вводом текста
        """
        self.screen.fill(self.bg_color_setup)
        pygame.display.flip()  # обновление кадра
    
        box = interface.InputBox(100, 100, 100, 100)
        box.main(self.screen)
        while self.running:
            self.clock.tick(self.fps_setup)
            # self.event_control()
            pygame.display.flip()

    def run(self):
        """
            Запускает саму игру
        """
        self.screen.fill(self.bg_color_setup)
        pygame.display.flip()  # обновление кадра
        # self.mainmenu_game()
        self.start_game()
        while self.running:
            self.clock.tick(self.fps_setup)
            self.event_control()
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
