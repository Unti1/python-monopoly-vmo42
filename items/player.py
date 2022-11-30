from settings.config import *

class Player:
    """ """

    counter_players: int = 0
    free_skins: List[str] = ["man", "robot", "woman", "zombie"] #os.listdir('/assets/img/animation').remove("emotion")

    def __init__(self):
        """ """
        sprite.Sprite.__init__(self)
        self._Size: tuple = (50,50) # Размеры спрайта игрока
        self._ID: str = "" # Будет задаваться из .env от каждого пользователя
        self._money: int = 500 # Количество денег при начале игры
        self._skin: str = Player.free_skins[random.randint(0, len(Player.free_skins)-1)]
        # self.cards: List[] # должен быть List типа класса, который хранит карточки 
        self._pos: tuple = (0,0)
        self._current_card_ID: int = 0
        self._rotate: int = 0
        self._player: int = Player.counter_players
        self._offsetted: bool = False
        Player.counter_players += 1 
        Player.free_skins.remove(self._skin)

    def get_size(self) -> str:
        return self._Size

    def get_id(self) -> str:
        """ """

        return self._ID

    def get_money(self) -> int:
        """ """

        return self._money

    def get_current_card_ID(self) -> int:
        """ """

        return self._current_card_ID

    # def get_cards(self) -> List:
    #     """ """

    #     return self.cards

    def get_pos(self) -> tuple:
        """ """

        return self._pos

    def change_money(self, val: int) -> NoReturn:
        """ """

        if self._money + val < 0:
            self._money = 0
        else:
            self._money += val

    def change_pos(self, val: tuple[int,int]|list[int,int]) -> NoReturn:
        """ """

        self._pos = val

    def change_current_card(self, val: int) -> NoReturn:
        if self._current_card_ID + val > 39:
            self._current_card_ID += val - 39
        else:
            self._current_card_ID += val
    
    def change_size(self,val:tuple[int,int]|list[int,int]) -> NoReturn:
        if len(val) == 2:
            self._Size = val

    def rotate(self, angle: int) -> NoReturn:
        """ """

        if self._rotate + angle > 360:
            self._rotate += angle - 360
        else:
            self._rotate += angle

    def change_size(self, val: tuple(int,int)) -> NoReturn:
        """ """

        self._Size = val

    def offset_player(self) -> NoReturn:
        """ """
        pos = self._pos
        if self._player == 0:
            self.change_pos((pos[0] - 30, pos[1] + 30))
        elif self._player == 1:
            self.change_pos((pos[0] + 30, pos[1] + 30))
        elif self._player == 2:
            self.change_pos((pos[0] - 30, pos[1] - 30))
        elif self._player == 3:
            self.change_pos((pos[0] + 30, pos[1] - 30))
        