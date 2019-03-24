from lib.TileType import TileType
import random
import numpy as np

class Level:
    xsize = 100
    ysize = 100
    tilemap = None

    def setMapSize(self,xsize,ysize):
       self.xsize = xsize
       self.ysize = ysize

    def generateTilemap(self):
        print("Generating Tilemap")
        random.seed(self.levelID)
        # Put a void type on the edge of the map ensuring xsize/ysize available in the middle
        # Preallocating the Lists
        self.tilemap = np.zeros([self.xsize,self.ysize],dtype=TileType)

        n_rooms = random.randint(2,5) # A room here is a square region of air tiles.

        self.generateRooms(n_rooms)

    def minimalOverlap(self,tlRoom,roomsize):
        # This function looks at the existing tilemap and the proposed new room and says true if far overlap is small and false if not


        return True

    def findFreeSpace(self):
        tarx = random.randint(0,self.xsize)
        tary = random.randint(0,self.ysize)

        while ( self.tilemap[tarx][tary] != TileType.AIR ):
            tarx = random.randint(0,self.xsize)
            tary = random.randint(0,self.ysize)
        return (tarx,tary)

    def generateRooms(self, n_rooms):
        # First thing we do. Generate the top left most corner coordinates
        for room in range(n_rooms):
            tlRoom = (random.randint(0,self.xsize),random.randint(0,self.ysize)) # Tuple with the coordinate
           
            # Now lets generate the size of the room based around the maximum level size (normal distribution)
            roomsize = ( int(random.uniform(0, self.xsize)), int(random.uniform(0, self.ysize)) )

            while( (tlRoom[0]+roomsize[0] >= self.xsize or tlRoom[1]+roomsize[1] >= self.ysize) and self.minimalOverlap(tlRoom,roomsize) ):
                tlRoom = (random.randint(0,self.xsize),random.randint(0,self.ysize)) # Tuple with the coordinate
                roomsize = ( int(random.uniform(0, self.xsize)), int(random.uniform(0, self.ysize)) )

            self.tilemap[tlRoom[0]:(tlRoom[0]+roomsize[0]), tlRoom[1]:(tlRoom[1]+roomsize[1])] = TileType.AIR

        # Now we've placed the rooms into the numpy array we need to check that they are all accessible from one another (else we've just generated a horrible solution)
        # Find out how many TileType.AIR there are in the array
        condition = self.tilemap == TileType.AIR
        airrooms = np.extract(condition, self.tilemap)
        nfreetiles = len(airrooms)
        
        # Saving an output of the progress so far
        np.savetxt('Level'+str(self.levelID)+'.out',self.tilemap,fmt='%d')





    def __init__(self,levelID,xsize=None,ysize=None):
        print("Generating Level "+str(levelID))
        self.levelID = levelID

        if(xsize == None and ysize == None):
            print("Defaulting to 100x100 per level")
        else:
            self.setMapSize(xsize,ysize)
        
        self.generateTilemap()



