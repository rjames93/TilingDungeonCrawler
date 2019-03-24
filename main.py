#!./env/bin/python

from lib.game import GameEngine


game = GameEngine()

game.setNumberOfLevels(1)

game.generateLevels()


game.finish()
