from distutils.command.config import config
from pygame import *
from settings.config import *
from time import sleep


class MainMenu:
    """
    Объект меню
    """
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.XYpos = (
            int(config.get("Display", "width"))//3,
            int(config.get("Display", "height"))//2
        )
        self.Size = (600, 600)
        self.buttons_path = "assets/img/menu"
        self.buttons_y_pos = [self.XYpos[0] +
                              ((self.Size[1]//3)*n) for n in range(0, 3)]
        self.rect: list = []
        self.image: list = []
        self.cfg_margin: int = 10
        self.cfg_coord: tuple = (int(config.get("Display", "width")) - self.cfg_margin, int(config.get("Display", "height")) - self.cfg_margin)
        self.hover = False

    def buttons_draw(self, screen) -> NoReturn:
        """
        Отрисовка кнопок
        """
        images_name: tuple = ('run_but.png', 'con_but.png', 'quit_but.png', 'cfg_but.png')
        count: int = 0
        for y in self.buttons_y_pos:
            self.rect.append(Rect(self.XYpos[0], y,
                             self.Size[0], self.Size[1]//3))
            self.image.append(image.load(f"{self.buttons_path}/{images_name[count]}"))
            screen.blit(self.image[count], (self.XYpos[0], y))
            count += 1
        self.image.append(image.load(f"{self.buttons_path}/{images_name[-1]}"))
        screen.blit(self.image[-1], (self.cfg_coord[0] - self.image[-1].get_width(),
                                     self.cfg_coord[1] - self.image[-1].get_height()))

    def get_btn_areas(self) -> list:
        """
        Возвращает области кнопок
        """
        areas: list = []
        count: int = 0
        for y in self.buttons_y_pos:
            areas.append((range(self.XYpos[0], self.XYpos[0] + self.image[count].get_width()),
                          range(y, y + self.image[count].get_height())))
        areas.append((range(self.cfg_coord[0] - self.image[-1].get_width(), self.cfg_coord[0] + self.image[-1].get_width()),
                      range(self.cfg_coord[1] - self.image[-1].get_height(), self.cfg_coord[1] + self.image[-1].get_height())))
        return areas

    def hovered(self, screen: display, btn_numb: int):
        margin: int = 4
        images_name: tuple = ('run_but.png', 'con_but.png', 'quit_but.png', 'cfg_but.png')
        try:
            if btn_numb == 3:
                rect = Rect(self.cfg_coord[0] - self.image[-1].get_width(), self.cfg_coord[0] + self.image[-1].get_width(),
                            self.cfg_coord[1] - self.image[-1].get_height(), self.cfg_coord[1] + self.image[-1].get_height())
            else:
                rect = Rect(self.XYpos[0] - margin, self.buttons_y_pos[btn_numb] - margin,
                            self.XYpos[1] + margin, self.Size[1] + margin)
            # подгрузка изображения
            self.hov_image = image.load(f"{self.buttons_path}/{images_name[btn_numb]}").convert()
            self.hov_image = transform.scale(self.hov_image, (self.image[btn_numb].get_width() + margin, self.image[btn_numb].get_height() + margin))
            screen.blit(self.hov_image, (rect.x, rect.y))
        except:
            pass


class PlayerList:
    """
    Объект списка игроков
    """
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.XYpos: tuple = (0, 0)
        self.Size: tuple = (0, 0)
        self.rect = Rect(self.XYpos[0], self.XYpos[1],
                         self.Size[0], self.Size[1])
        self.Player_offset: int = 8 #отступ
        self.PLayer_btn_Size: tuple = (self.Size[0] - self.Player_offset * 2, (self.Size[1] - self.Player_offset * 5) // 4)

    def draw(self, screen: display) -> NoReturn:
        """
        Отрисовывает игроков (пока что цветные прямоугольники)
        """
        self.image = Surface(self.Size)
        self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.XYpos[0], self.XYpos[1]))
        self.Player_btn_Pos: list = [self.XYpos[0] + self.Player_offset + ((self.Size[1] - self.Player_offset)//4)*n for n in range(4)]
        self.Player_colors: tuple = ("#990000", "#009900", "#009999", "#999900")
        for y in range(4):
            self.Player_image = Surface((self.Size[0] - self.Player_offset * 2, self.Size[1]//4 - self.Player_offset * 1.5))
            self.Player_image.fill(Color(self.Player_colors[y]))
            screen.blit(self.Player_image, (self.XYpos[0] + self.Player_offset, self.XYpos[1] + self.Player_btn_Pos[y]))


class ConfigWind:
    """
    Окно конфигураций(прямоугольник с отступами от краев экрана)
    """
    def __init__(self, margin=10):
        sprite.Sprite.__init__(self)
        self.margin: int = margin
        self.XYpos: tuple = (
            self.margin,
            int(config.get("Display", "height"))//2.5
        )
        self.Size = (int(config.get("Display", "width")) - self.margin * 2,
                     int(config.get("Display", "height")) - self.margin * 2)

    def Draw(self, screen) -> NoReturn:
        """
        Отрисовывает сам прямоугольник
        """
        self.image = Surface(self.Size)
        self.image.fill(Color("#888888"))
        screen.blit(self.image, self.XYpos)
        print(self.Size)
