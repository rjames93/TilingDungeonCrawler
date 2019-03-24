#!./env/bin/python

from lib.game import GameEngine


game = GameEngine()
game.setimgdir('./img/')

game.setNumberOfLevels(1)


game.generateLevels()

game.play()

game.finish()
