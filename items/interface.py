from pygame import *
from settings.config import *

class Text_Boxes:
    """
    TODO: Доделать взаимодействие с выводом текста на экран по позиции
    """
    def __init__(self) -> None:
        pass
        


class InputBox:

    """
    TODO: Доделать взаимодействие со строкой ввода
    """
    def __init__(self, x, y, w, h, text=''):
        self.COLOR_INACTIVE = Color('lightskyblue3')
        self.COLOR_ACTIVE = Color('dodgerblue2')
        self.FONT = font.Font(None, 32)
        self.rect = Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        draw.rect(screen, self.color, self.rect, 2)

    def main(self,screen):
        clock = time.Clock()
        input_box1 = InputBox(100, 100, 140, 32)
        input_box2 = InputBox(100, 300, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(screen)
            display.flip()
        

class MainMenu:
    """
    TODO: Доделать модуль Главного Меню
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

    def buttons_draw(self, screen):
        for y in self.buttons_y_pos:
            self.rect = Rect(self.XYpos[0], y,
                             self.Size[0], self.Size[1]//3)
            self.image = image.load(f"{self.buttons_path}/run_but.png")
            screen.blit(self.image, (self.XYpos[0], y))


class PlayerList:
    '''TODO: Доделать модуль Списка игроков'''
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
