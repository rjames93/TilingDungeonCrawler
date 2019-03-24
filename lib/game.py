import pygame
from lib.Level import Level

class GameEngine:
    nlevels = 1
    levels = []

    def init(self):
        pygame.init()

    def setNumberOfLevels(self, nlevels):
        self.nlevels = nlevels

    def generateLevels(self):
        for i in range(self.nlevels):
            self.levels.append( Level(i) )

    def finish(self):
        print("Cleaning Up")
