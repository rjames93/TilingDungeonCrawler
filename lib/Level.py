from lib.TileType import TileType
import random
import numpy as np
import sys, types, pprint

class Level:
    xsize = None
    ysize = None
    tilemap = None
    rooms = []

    def __init__(self,*args, **kwargs):
        if len(args) == 1:
            # This is the simple filename version
            self.initLoadMapFromFile(args[0])
        if len(args) == 2:
            self.initCreateNewMap(args[0],args[1])

    def initLoadMapFromFile(self,filename):
        print(filename)
        self.tilemap = np.loadtxt(filename)
        self.xsize = self.tilemap.shape[0]
        self.ysize = self.tilemap.shape[1]

    def initCreateNewMap(self, xsize = None, ysize = None):
        if( xsize == None or ysize == None ):
            self.xsize = 100
            self.ysize = 100
        else:
            self.xsize = xsize
            self.ysize = ysize
        # Now create the tilemap object
        self.tilemap = np.empty( (self.xsize,self.ysize), TileType)
        self.generateTilemap()

    def findFreeSpace(self):
        x = random.randint(0,self.xsize-1)
        y = random.randint(0,self.ysize-1)

        while( self.tilemap[x][y] != TileType.AIR ):
            x = random.randint(0,self.xsize)
            y = random.randint(0,self.ysize)
        return (x,y)

    def loadTilemapFromFile(self,filename):
        self.tilemap = np.loadtxt(filename)
        self.xsize = self.tilemap.shape[0]
        self.ysize = self.tilemap.shape[1]

    def generateTilemap(self):
        self.placeRooms(10)
        #self.fillMazesEmptyRegion()
        #self.connectRoomsToMazes()
        #self.cleanDeadEnds()

    def placeRooms(self,nRooms=None):
        if(nRooms == None):
            nRooms = random.randint(5,15)

        for i in range(nRooms):
            topCornerCoords = [random.randint(0,self.xsize),random.randint(0,self.ysize)]
            roomDimensions = [random.randint(10,20),random.randint(10,20)]
            while ( self.roomCollision([topCornerCoords,roomDimensions]) == False ):
                topCornerCoords = [random.randint(0,self.xsize),random.randint(0,self.ysize)]
                roomDimensions = [random.randint(10,20),random.randint(10,20)]

            self.rooms.append( [topCornerCoords,roomDimensions]  )
        
        # Rooms have walls innit :p
        for room in self.rooms:
            for x in range(room[0][0],room[1][0]):
                for y in range(room[0][1],room[1][1]):
                    print(x,y)

    def roomCollision(self,room):
        # Room contains the top corner [0] and the size [1]
        coords = room[0]
        size = room[1]
        proposedmap = self.tilemap[ coords[0] : coords[0]+size[0] ][ coords[1] : coords[1]+size[1] ] # This is the subset of the tilemap that the proposed room is going into
        if ( proposedmap.all(TileType.VOID).all() == True ):
            return False
        else:
            return True

    def getTileType(self,x,y):
        return self.tilemap[x][y]
