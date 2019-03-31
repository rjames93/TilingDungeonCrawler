import pygame
import random
from lib.Level import Level
from lib.Entity import *
from lib.TileType import TileMap
from os import listdir
from os.path import isfile, join


class GameEngine:
    nlevels = 1
    levels = [] # A list of the levels in the game
    entities = [] # A list of the entities in the game

    def __init__(self):
        self.runSetup()

    def runSetup(self):
        pygame.init()
        screen_width=700
        screen_height=700
        self.screen=pygame.display.set_mode([screen_width,screen_height])

    def setimgdir(self,directory):
        self.imgdir = directory
        self.tileMap = TileMap(self.imgdir)

    def setlvldir(self,directory):
        self.lvldir = directory

    def loadLevelsFromDir(self):
        files = [f for f in listdir(self.lvldir) if isfile( self.lvldir + f )]
        self.nlevels = len(files)
        for i in range(self.nlevels):
            tmp = Level(files[i]) # This generates a random file anyway
            self.levels.append(tmp)
    
    def setNumberOfLevels(self, nlevels):
        self.nlevels = nlevels

    def generateLevels(self):
        for i in range(self.nlevels):
            self.levels.append( Level(100,100) )

    def finish(self):
        print("Cleaning Up")
        pygame.quit()

    def addPlayerChar(self):
        (posx, posy, level) = self.findFreeSpace(0)
        self.entities.append( playerEntity(posx,posy,level,"Player") )

    def findFreeSpace(self,level=None):
        if level == None:
            level = random.randint(0,len(self.levels))
        # Now we need to go through the levels list and find some empty space
        currentLevel = self.levels[level]
        (posx,posy) = currentLevel.findFreeSpace()

        return (posx,posy,level)

    def populateEntities(self):
        # Select a number of entities
        nNonPCEntities = random.randint(1,10)
        (posx, posy, level) = self.findFreeSpace()
        self.entities.append( aiEntity(posx,posy, level,"AI") )

    def play(self):
        print("Starting Game Loop")
        self.addPlayerChar()
        self.populateEntities()

        while True:
            ev = pygame.event.poll() # Look for events
            if ev.type == pygame.QUIT:
                break

            # Write backgroundColor
            self.screen.fill((0,0,0))
            
            # The entity of focus is the one whose perspective we render from. :)
            entityInFocus = 0
            currentLevel = self.levels[self.entities[entityInFocus].getLevel()]
            
            if ev.type == pygame.KEYDOWN:
                self.entities[ entityInFocus ].updatePosition(ev,currentLevel)
            
            
            
            # Render from the Perspective            
            entitiesOnLevel = [ ent for ent in self.entities if ent.getLevel() == self.entities[entityInFocus].getLevel() ]
            self.entities[ entityInFocus ].render( currentLevel , entitiesOnLevel, self.screen, self.tileMap ) # Give the Current Level and the Entities that are on the Same Level to the entityInFocus
                
            # Flip the Screen
            pygame.display.flip()


