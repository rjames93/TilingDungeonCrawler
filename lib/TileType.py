from enum import IntEnum as Enum
import pygame
from os import listdir
from os.path import isfile, join

def TileMap(imageDirectory):
    tilePrefix = imageDirectory+'tiles/'
    print(tilePrefix)
    tileMap = {}

    files = [f for f in listdir(tilePrefix) if isfile(join(tilePrefix, f))]
    print(files)
    for Tile in TileType:
            tileMap[Tile] = pygame.image.load("blank.png")

    return tileMap

class TileType(Enum):
    VOID = 0
    AIR = 1
    BRICK_HORIZONTAL = 2
    BRICK_VERTICAL = 3
