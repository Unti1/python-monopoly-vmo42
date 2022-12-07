from settings.config import *

class Player:
    """ """

    counter_players: int = 0
    free_skins: list = os.listdir('assets/img/animation')
    free_skins.remove("emotion")

    def __init__(self, XYpos: tuple[int,int] = (0,0)):
        """ """
        sprite.Sprite.__init__(self)
        self._Size: tuple = (40,40) # Размеры спрайта игрока
        self._ID: str = "" # Будет задаваться из .env от каждого пользователя
        self._money: int = 500 # Количество денег при начале игры
        self._skin_name: str = Player.free_skins[random.randint(0, len(Player.free_skins)-1)]
        # self.cards: List[] # должен быть List типа класса, который хранит карточки 
        self._player: int = Player.counter_players
        self._set_init_pos(XYpos)
        self._current_card_ID: int = 0
        self._rotate: int = 0
        self._offsetted: bool = False
        self._rotate: int = 0
        self._miror: tuple[int,int] = (0, 0)

        Player.counter_players += 1 
        Player.free_skins.remove(self._skin_name)

    def _set_init_pos(self, XYpos) -> NoReturn:
        if (self._player == 0):
            self._XYpos = (XYpos[0], XYpos[1]+20)
        elif (self._player == 1):
            self._XYpos = (XYpos[0]+40, XYpos[1]+20)
        elif (self._player == 2):
            self._XYpos = (XYpos[0], XYpos[1]+70)
        elif (self._player == 3):
            self._XYpos = (XYpos[0]+40, XYpos[1]+70)

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

        return self._XYpos

    def change_money(self, val: int) -> NoReturn:
        """ """

        if self._money + val < 0:
            self._money = 0
        else:
            self._money += val

    def change_pos(self, val: tuple[int,int]|list[int,int]) -> NoReturn:
        """ """

        self._XYpos = val

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

    def offset_player(self) -> NoReturn:
        """ """
        pos = self._XYpos
        if self._player == 0:
            self.change_pos((pos[0] - 30, pos[1] + 30))
        elif self._player == 1:
            self.change_pos((pos[0] + 30, pos[1] + 30))
        elif self._player == 2:
            self.change_pos((pos[0] - 30, pos[1] - 30))
        elif self._player == 3:
            self.change_pos((pos[0] + 30, pos[1] - 30))
        
    def draw(self, screen: display, rotate: int = 0, miror: tuple[int,int] = (0, 0)):
        self._rotate = rotate
        self._miror = miror
        self.rect = Rect(self._XYpos[0], self._XYpos[1],
                         self._Size[0], self._Size[1])
        try:
            # подгрузка изображения
            dir = f"assets/img/animation/{self._skin_name}"
            sprites = os.listdir(dir)
            sprite = sprites[random.randint(0, len(sprites)-1)]
            self.image = image.load(dir + f"/{sprite}")
            # подгон картинки под размер объекта
            self.image = transform.scale(self.image, self._Size)
            self.image = transform.rotate(
                self.image, rotate)  # поворот объекта
            self.image = transform.flip(
                self.image, miror[0], miror[1])  # отражение объекта
        except:
            self.image = Surface(self._Size)
            transform.scale(self.image, self._Size)
            self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.rect.x, self.rect.y))  # отрисовка