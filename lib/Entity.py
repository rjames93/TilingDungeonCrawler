import uuid
import thorpy
from lib.TileType import TileType
import pygame

class Entity:
    def __init__(self, initx, inity, initLevel, name):
        self.position = (initx,inity)
        self.uuid = uuid.uuid4()
        self.name = name
        self.initLevel = initLevel
    def getLevel(self):
        return self.initLevel
    def getName(self):
        return self.name
    def getUUID(self):
        return self.uuid
    def getPosition(self):
        return self.position

class animateEntity(Entity):
    def __init__(self, initx, inity, initLevel, name):
        Entity.__init__(self, initx, inity, initLevel, name)

    def render(self, level, entities, surface, imgdata):
        raise NotImplementedError() # Basically if this happens then the child class doesn't have their own render method.

    def updatePosition(self,key,levelMap):
        print(key)
        if(key.key == pygame.K_UP):
            proposedCoords = (self.position[0], self.position[1]-1)
            if( self.checkCollision( proposedCoords, levelMap) == True):
                self.position = proposedCoords
        if(key.key == pygame.K_DOWN):
            proposedCoords = (self.position[0], self.position[1]+1)
            if( self.checkCollision( proposedCoords, levelMap) == True):
                self.position = proposedCoords
        if(key.key == pygame.K_LEFT):
            proposedCoords = (self.position[0]-1, self.position[1])
            if( self.checkCollision( proposedCoords, levelMap) == True):
                self.position = proposedCoords
        if(key.key == pygame.K_RIGHT):
            proposedCoords = (self.position[0]+1, self.position[1])
            if( self.checkCollision( proposedCoords, levelMap) == True):
                self.position = proposedCoords



    def checkCollision(self,newposition,levelMap):
        if( levelMap.getTileType(newposition[0], newposition[1]) != TileType.AIR ):
            return False
        else:
            return True


# Pretty Obvious right? player, nature and ai
class playerEntity(animateEntity):
    def __init__(self, initx, inity, initLevel, name):
        animateEntity.__init__(self, initx, inity, initLevel, name)

    def render(self, level, entities, surface, imgdata):
        # Need to get the Tile Image Data 
        screencentralcoords = [surface.get_width()/2,surface.get_height()/2]

        # Lets do some 'ray projection' for vision 
        radius = 5

        centralTile = level.getTileType(self.position[0],self.position[1])
        centralcoords= ( screencentralcoords[0] - imgdata[centralTile].get_rect().centerx, screencentralcoords[1] - imgdata[centralTile].get_rect().centery )
        #surface.blit(imgdata[centralTile],centralcoords)

        for x in range(-radius,radius):
            for y in range(-radius,radius):
                tile = level.getTileType(self.position[0]+x,self.position[1]+y)
                surface.blit( imgdata[tile], (screencentralcoords[0] + x*imgdata[tile].get_rect().centerx, screencentralcoords[1] + y*imgdata[tile].get_rect().centery) )

        surface.blit(imgdata[TileType.PLAYER],centralcoords) 




class natureEntity(animateEntity):
    def __init__(self, initx, inity, initLevel, name):
        animateEntity.__init__(self, initx, inity, initLevel, name)

class aiEntity(animateEntity):
    def __init__(self, initx, inity, initLevel, name):
        animateEntity.__init__(self, initx, inity, initLevel, name)


# Pretty Obvious too. inanimateEntity at the moment is just a subclass for the itemEntity
class inanimateEntity(Entity):
    def __init__(self, initx, inity, initLevel, name):
        Entity.__init__(self, initx, inity, initLevel, name)

class itemEntity(inanimateEntity):
    def __init__(self, initx, inity, initLevel, name):
        inanimateEntity(self, initx, inity, initLevel, name)

