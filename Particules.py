import json
import sys
import random

from Core import *
from Environment import *
from SMA import *
from Particle import *
from View import *

class Particules(Core):
    """docstring for Particules"""
    def __init__(self, nbParticles=None):
        super(Particules, self).__init__()

    def populate(self, agentlist):
        #Fetch data
        seed = self.data["seed"]
        nbParticles = self.data["nbParticles"]

        #Check if there is a given seed
        if seed == 0 or seed == "0" :
            #if not, create a random seed
            seed = random.randint(0, sys.maxsize)

        #Initialize the random engine with the seed
        random.seed(seed)

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
            self.createAgent(agentlist, position[0], position[1], i)

    def createAgent(self, agentlist, x, y, name):
        agent = Particle(self.environment, x, y, name, self.data["torus"], self.data["trace"])
        agentlist.append(agent)
        self.environment.setInCell(x, y, agent)
        if self.data["trace"]:
            agent.printTrace()

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
        if not "refresh" in self.data:
            self.data["refresh"] = 1
        if not "nbParticles" in self.data:
            self.data["nbParticles"] = 10
        if not "autoquit" in self.data:
            self.data["autoquit"] = False
        if not "profile" in self.data:
            self.data["profile"] = False
        if not "profileStep" in self.data:
            self.data["profileStep"] = 40

if __name__ == '__main__':
    main(Particules)
