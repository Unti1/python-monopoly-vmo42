from pygame import *
from typing import NoReturn


#################################################################################################################################
class CardMap:
    """
    Класс объекта карт на игровое поле
    """

    def __init__(self, name: str, id: int, x: int, y: int, width: int, height: int):
        """

        Args:
            name (str): Имя карты, (название картинки)
            id (int): Уникальный ID
            x (int): X позиция на экране
            y (int): Y позиция на экране
            width (int): Ширина
            height (int): Высота
        """
        sprite.Sprite.__init__(self)
        self.Name: str = name
        self.ID: str = id
        self.XYpos: tuple = (x, y)
        self.Size: tuple = (width, height)
        self.card_offset: int = 2  # отступ между карточками

    def draw(self, screen: display, rotate: int = 0, miror: tuple[int,int] = (0, 0)) -> NoReturn:
        self.rect = Rect(self.XYpos[0], self.XYpos[1],
                         self.Size[0], self.Size[1])
        try:
            # подгрузка изображения
            self.image = image.load(f"assets/img/map/{self.Name}").convert()
            # подгон картинки под размер объекта
            self.image = transform.scale(self.image, self.Size)
            self.image = transform.rotate(
                self.image, rotate)  # поворот объекта
            self.image = transform.flip(
                self.image, miror[0], miror[1])  # отражение объекта
        except:
            self.image = Surface(self.Size)
            transform.scale(self.image, self.Size)
            self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.rect.x, self.rect.y))  # отрисовка
    
    def back_draw(self,screen: display, x:int, y:int, size:tuple[int,int]) -> NoReturn:
        self.rect = Rect(x, y, size[0],size[1])
        try:
            # подгрузка изображения
            self.image = image.load(f"assets/img/back_cards/{self.Name}").convert()
            # подгон картинки под размер объекта
            self.image = transform.scale(self.image, size)
        except:
            self.image = Surface(size)
            transform.scale(self.image, size)
            self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.rect.x, self.rect.y))  # отрисовка

    @property
    def card_area(self) -> tuple[range,range]:
        """
        Выводит область взаимодействия карты от их позиции по X и Y
        """
        return (range(self.XYpos[0], self.XYpos[0]+self.Size[0]), range(self.XYpos[1], self.XYpos[1]+self.Size[1]))

#################################################################################################################################
class Map:
    """
        Объект игрового поля
    """

    def __init__(self):
        self.__SessionID: str = ""
        self.__CurrentUsersList: dict = {}
        self.__MapImagePath: str = ""
        self.__MapStructure: list[str] = [
            ".---------.",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            ".---------.",
        ]
        self.__MapCards: list[CardMap] = []

    def reshuffle_cards(self) -> NoReturn:
        """
            Тосовка карточек поля
        """
        import random
        if len(self.__MapCards) > 4:
            cards = self.__MapCards[4:]
            random.shuffle(cards)
            self.__MapCards[4:] = cards

    def append_card(self, card: CardMap) -> NoReturn:
        """
            Добавление карты в конец списка
        Args:
            card (CardMap): объект карточки
        """
        self.__MapCards.append(card)

    def insert_card(self, ind, card: CardMap) -> NoReturn:
        """
            Вставка карты на определенную позицию
        Args:
            ind (_type_): позиция в списке
            card (CardMap): объект карты
        """
        self.__MapCards.insert(ind, card)

    def set_MapImagePath(self, value: str) -> NoReturn:
        """[Depracted] Путь к основному полю

        Args:
            value (str): путь
        """
        self.__MapImagePath = value

    def set_CurrentUsersList(self, value: dict) -> NoReturn:
        """
            Задать список игроков
        Args:
            value (dict): данные игроков . Шаблон {"уникальный id игрока": [*данные*]}
        """
        self.__CurrentUsersList = value

    def set_SessionID(self, value: str) -> NoReturn:
        """ID игровой сессии

        Args:
            value (str): ID сессии
        """
        self.__SessionID = value

    @ property
    def get_MapImagePath(self) -> str:
        """[Depracted] Путь к картинке основному поля"""
        return (self.__MapImagePath)

    @ property
    def get_CurrentUsersList(self) -> list[str]:
        """Получить список текущих игроков на карте"""
        return (self.__CurrentUsersList)

    @ property
    def get_SessionID(self) -> str:
        """Получить ID сессию"""
        return (self.__SessionID)

    @ property
    def get_MapStructure(self) -> list[str]:
        """Получить структуру поля(для рендеринга карты)"""
        return (self.__MapStructure)

    @ property
    def get_MapCards(self) -> list[CardMap]:
        """Получить карты на поле"""
        return (self.__MapCards)

#################################################################################################################################