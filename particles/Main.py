import json
import sys
import random

sys.path.append('../core')
from Core import *
from Environment import *
from SMA import *
from Particle import *
from View import *

class Main(Core):
    """docstring for Main"""
    def __init__(self, nbParticles=None):
        super(Main, self).__init__()

    def populate(self):
        #Fetch data
        nbParticles = self.data["nbParticles"]

        #Fetch the free cells from the environment
        freeCells = self.environment.getFreeCells()

        #Check if there are enough cells for each particle
        if len(freeCells) < nbParticles :
            print("Error ! There are more particles than free cells !")
            return

        #Shuffle the list
        random.shuffle(freeCells)

        #Pop a free cell from the list then create and place an agent in this cell
        for i in range(nbParticles):
            position = freeCells.pop()
            self.createAgent(Particle, position[0], position[1], i)

    def setDefaultProperties(self):
        if not "gridSizeX" in self.data:
            self.data["gridSizeX"] = 10
        if not "gridSizeY" in self.data:
            self.data["gridSizeY"] = 10
        if not "torus" in self.data:
            self.data["torus"] = True
        if not "canvasSizeX" in self.data:
            self.data["canvasSizeX"] = 500
        if not "canvasSizeY" in self.data:
            self.data["canvasSizeY"] = 500
        if not "boxSize" in self.data:
            self.data["boxSize"] = 0
        if not "delay" in self.data:
            self.data["delay"] = 100
        if not "scheduling" in self.data:
            self.data["scheduling"] = "sequential"
        if not "nbTicks" in self.data:
            self.data["nbTicks"] = 100
        if not "grid" in self.data:
            self.data["grid"] = True
        if not "trace" in self.data:
            self.data["trace"] = True
        if not "seed" in self.data:
            self.data["seed"] = 0
        if not "pause" in self.data:
            self.data["pause"] = False
        if not "refresh" in self.data:
            self.data["refresh"] = 1
        if not "nbParticles" in self.data:
            self.data["nbParticles"] = 10
        if not "autoquit" in self.data:
            self.data["autoquit"] = False
        #if not "profile" in self.data:
         #   self.data["profile"] = False
        #if not "profileStep" in self.data:
         #   self.data["profileStep"] = 40

if __name__ == '__main__':
    main(Main)
