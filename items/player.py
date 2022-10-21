from typing import NoReturn


class Player:
    """ """

    counter_players: int = 0

    def __init__(self):
        """ """
        Player.counter_players += 1 

        self._ID: str = str(Player.counter_players)
        self._money: int = 500
        # self.cards: List[] # должен быть List типа класса, который хранит карточки 
        self._pos: int = 0

    def get_id(self) -> str:
        """ """

        return self._ID

    def get_money(self) -> int:
        """ """

        return self._money

    # def get_cards(self) -> List:
    #     """ """

    #     return self.cards

    def get_pos(self) -> int:
        """ """

        return self._pos

    def change_money(self, val: int) -> NoReturn:
        """ """

        if self._money + val < 0:
            self._money = 0
        else:
            self._money += val

    def change_pos(self, val: int) -> NoReturn:
        """ """

        if self._pos + val > 39:
            self._pos += val - 39
        else:
            self._pos += val