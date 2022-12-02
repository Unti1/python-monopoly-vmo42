from settings.config import *

COLOR_INACTIVE = Color('lightskyblue3')
COLOR_ACTIVE = Color('dodgerblue2')
FONT = font.Font(None, 32)

class InputBox:

    def __init__(self,screen:display, x:int, y:int, w:int, h:int, text=''):
        self.screen = screen
        self.rect = Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
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
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_RETURN:
                    print(self.text)
                    self.text = self.text
                elif event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        draw.rect(screen, self.color, self.rect, 2)


    # Форма заполнения будет работать до тех пор пока не заполнена и не закончена ентером
    def input_init(self):
        input_box1 = InputBox(100, 100, 140, 32)
        input_box2 = InputBox(100, 300, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in event.get():
                if event.type == QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            self.screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(self.screen)

            display.flip()

if __name__ == '__main__':
    quit()