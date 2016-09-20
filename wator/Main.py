import json
import sys
import random

sys.path.append('../core')
from Core import *
from Environment import *
from SMA import *
from Shark import *
from Fish import *
from View import *

class Main(Core):
    """docstring for Main"""
    def __init__(self, nbParticles=None):
        super(Main, self).__init__()

    def populate(self):
        #Fetch data
        nbSharks = self.data["nbSharks"]
        nbFishes = self.data["nbFishes"]

        #Fetch the free cells from the environment
        freeCells = self.environment.getFreeCells()

        #Check if there are enough cells for each particle
        if len(freeCells) < nbSharks + nbFishes :
            print("Error ! There are more particles than free cells !")
            print("nbSharks", nbSharks, "nbFishes", nbFishes)
            return

        #Shuffle the list
        random.shuffle(freeCells)

        #Pop a free cell from the list then create and place an agent in this cell
        for i in range(nbSharks):
            position = freeCells.pop()
            self.createAgent(Shark, position[0], position[1], "Shark" + str(i))

        for i in range(nbFishes):
            position = freeCells.pop()
            self.createAgent(Fish, position[0], position[1], "Fish" + str(i))

        self.environment.nbSharks = nbSharks
        self.environment.nbFishes = nbFishes

    def setDefaultProperties(self):
        if not "gridSizeX" in self.data:
            self.data["gridSizeX"] = 50
        if not "gridSizeY" in self.data:
            self.data["gridSizeY"] = 50
        if not "torus" in self.data:
            self.data["torus"] = True
        if not "canvasSizeX" in self.data:
            self.data["canvasSizeX"] = 500
        if not "canvasSizeY" in self.data:
            self.data["canvasSizeY"] = 500
        if not "boxSize" in self.data:
            self.data["boxSize"] = 0
        if not "delay" in self.data:
            self.data["delay"] = 1
        if not "scheduling" in self.data:
            self.data["scheduling"] = "sequential"
        if not "nbTicks" in self.data:
            self.data["nbTicks"] = 1000
        if not "grid" in self.data:
            self.data["grid"] = True
        if not "trace" in self.data:
            self.data["trace"] = True
        if not "seed" in self.data:
            self.data["seed"] = 0
        if not "refresh" in self.data:
            self.data["refresh"] = 1
        if not "autoquit" in self.data:
            self.data["autoquit"] = False
        if not "nbSharks" in self.data:
            self.data["nbSharks"] = 5
        if not "nbFishes" in self.data:
            self.data["nbFishes"] = 200
        if not "sharkBreedTime" in self.data:
            self.data["sharkBreedTime"] = 10
        if not "sharkStarveTime" in self.data:
            self.data["sharkStarveTime"] = 3
        if not "fishBreedTime" in self.data:
            self.data["fishBreedTime"] = 2

if __name__ == '__main__':
    main(Main)
