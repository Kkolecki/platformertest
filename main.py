import pygame
from config import *
from level import Level
import sys


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    # main run function, typical for pygame loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('white')  # make custom background later so its not just single color
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()