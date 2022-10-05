from pygame import *


class MainMenu:
    pass


class PlayerList:
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.XYpos = (0, 0)
        self.Size = (0, 0)
        self.rect = Rect(self.XYpos[0], self.XYpos[1],
                         self.Size[0], self.Size[1])

    def draw(self, screen: display):  # Выводим себя на экран
        self.image = Surface(self.Size)
        self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.XYpos[0], self.XYpos[1]))
