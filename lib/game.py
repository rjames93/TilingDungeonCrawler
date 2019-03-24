import pygame
import random
from lib.Level import Level
from lib.Entity import *

class GameEngine:
    nlevels = 1
    levels = [] # A list of the levels in the game
    entities = [] # A list of the entities in the game

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

    def addPlayerChar(self):
        (posx, posy) = self.findFreeSpace(0)
        self.entities.append( playerEntity(0,0,"Player") )

    def findFreeSpace(self,level=None):
        if level == None:
            level = random.randint(0,len(self.levels))
        # Now we need to go through the levels list and find some empty space
        currentLevel = self.levels[level]
        (posx,posy) = currentLevel.findFreeSpace()

        return (posx,posy)

    def populateEntities(self):
        # Select a number of entities
        nNonPCEntities = random.randint(1,10)
        (posx, posy) = self.findFreeSpace()
        self.entities.append( aiEntity(posx,posy,"AI") )

    def play(self):
        print("Starting Game Loop")
        self.addPlayerChar()
        self.populateEntities()
