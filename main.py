#!./env/bin/python

from lib.game import GameEngine


game = GameEngine()
game.setimgdir('./img/')
game.setlvldir('./lvls/')

# Set or Load Levels
# game.setNumberOfLevels(1)
# game.generateLevels()

game.loadLevelsFromDir()


game.play()

game.finish()
