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
        self.rect = Rect(self.XYpos[0], self.XYpos[1],
                         self.Size[0], self.Size[1])
        self.buttons_path = "assets\img\menu"
        self.buttons_pos = []
    
    def buttons_draw(self,screen):
        

    def draw(self, screen: display):
        self.image = Surface(self.Size)
        self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.XYpos[0], self.XYpos[1]))


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
