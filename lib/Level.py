from lib.TileType import TileType
import random
import numpy as np

class Level:
    tilemap= [[]]
    xsize = 100
    ysize = 100

    def setMapSize(self,xsize,ysize):
       self.xsize = xsize
       self.ysize = ysize

    def generateTilemap(self):
        print("Generating Tilemap")
        random.seed(self.levelID)
        # Put a void type on the edge of the map ensuring xsize/ysize available in the middle
        # Preallocating the Lists
        tilemap = np.empty([self.xsize,self.ysize],dtype=TileType)


    def __init__(self,levelID,xsize=None,ysize=None):
        print("Generating Level "+str(levelID))
        self.levelID = levelID

        if(xsize == None and ysize == None):
            print("Defaulting to 100x100 per level")
        else:
            self.setMapSize(xsize,ysize)
        
        self.generateTilemap()



