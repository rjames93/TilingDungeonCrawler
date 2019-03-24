import uuid
import thorpy

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

# Pretty Obvious right? player, nature and ai
class playerEntity(animateEntity):
    def __init__(self, initx, inity, initLevel, name):
        animateEntity.__init__(self, initx, inity, initLevel, name)

    def render(self, level, entities, surface, imgdata):
        # Need to get the Tile Image Data 
        centralTile = level.getTileType(self.position[0],self.position[1])
        surfacewidth = surface.get_width()
        surfaceheight = surface.get_height()
        screencentralcoords = [surface.get_width()/2,surface.get_height()/2]

        # Lets do some 'ray projection' for vision
        centralcoords= ( screencentralcoords[0] - imgdata[centralTile].get_rect().centerx, screencentralcoords[1] - imgdata[centralTile].get_rect().centery )
        surface.blit(imgdata[centralTile],centralcoords)


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

