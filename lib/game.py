import pygame
from lib.Level import Level

class GameEngine:
    nlevels = 1
    levels = []

    def init(self):
        pygame.init()
        screen_width=700
        screen_height=400
        screen=pygame.display.set_mode([screen_width,screen_height])

    def setNumberOfLevels(self, nlevels):
        self.nlevels = nlevels

    def generateLevels(self):
        for i in range(self.nlevels):
            self.levels.append( Level(i) )

    def finish(self):
        print("Cleaning Up")
        pygame.quit()

    def play(self):
        print("Starting Game Loop")
