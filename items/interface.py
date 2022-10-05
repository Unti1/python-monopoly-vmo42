from distutils.command.config import config
from pygame import *
from settings.config import *


class MainMenu:
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

    def buttons_draw(self, screen):
        for y in self.buttons_y_pos:
            self.rect = Rect(self.XYpos[0], y,
                             self.Size[0], self.Size[1]//3)
            self.image = image.load(f"{self.buttons_path}/run_but.png")
            screen.blit(self.image, (self.XYpos[0], y))


class PlayerList:
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.XYpos = (0, 0)
        self.Size = (0, 0)
        self.rect = Rect(self.XYpos[0], self.XYpos[1],
                         self.Size[0], self.Size[1])

    def draw(self, screen: display):
        self.image = Surface(self.Size)
        self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.XYpos[0], self.XYpos[1]))
