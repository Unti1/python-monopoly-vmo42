from threading import Thread
from settings.config import *
import pygame


class Game(Thread):
    def __init__(self):
        Thread.__init__(self)

        pygame.init()
        pygame.mixer.init()  # для звука
        screen = pygame.display.set_mode(
            (int(config['Display']['WIDTH']), int(config['Display']['WIDTH'])))
        pygame.display.set_caption("Monopoly")
        clock = pygame.time.Clock()

        self.running = True

    def run(self):
        while self.running:
            pass


if __name__ == '__main__':
    Game().start()
