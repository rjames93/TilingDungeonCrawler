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
    VOID = 0 # Void is for the edges
    AIR = 1 # Stone Tile Floor (basic floor

    BRICK_WALL_HORIZONTAL = 100
    BRICK_WALL_VERTICAL = 101
