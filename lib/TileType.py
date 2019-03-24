from enum import IntEnum as Enum
import pygame
from os import listdir
from os.path import isfile, join

def TileMap(imageDirectory):
    tilePrefix = imageDirectory+'tiles/'
    tileMap = {}

    files = [f for f in listdir(tilePrefix) if isfile( tilePrefix + f)]
    
    for f in files:
        enumNumber = int(f.split('-')[0])
        filename = (tilePrefix+f)
        tileMap[TileType(enumNumber)] = pygame.transform.smoothscale(pygame.image.load(filename),(32,32))
    return tileMap

class TileType(Enum):
    VOID = 0 # Void is for the edges
    AIR = 1 # Stone Tile Floor (basic floor

    BRICK_WALL_HORIZONTAL = 100
    BRICK_WALL_VERTICAL = 101

    PLAYER = 999
