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
        seed = data["seed"]
        nbParticles = data["nbParticles"]

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
        agent = Particle(self.environment, x, y, name, data["torus"], data["trace"])
        agentlist.append(agent)
        self.environment.setInCell(x, y, agent)
        if data["trace"]:
            agent.printTrace()

def setDefaultProperties():
    if not "gridSizeX" in data:
        data["gridSizeX"] = 10
    if not "gridSizeY" in data:
        data["gridSizeY"] = 10
    if not "torus" in data:
        data["torus"] = True
    if not "canvasSizeX" in data:
        data["canvasSizeX"] = 500
    if not "canvasSizeY" in data:
        data["canvasSizeY"] = 500
    if not "boxSize" in data:
        data["boxSize"] = 0
    if not "delay" in data:
        data["delay"] = 100
    if not "scheduling" in data:
        data["scheduling"] = "sequential"
    if not "nbTicks" in data:
        data["nbTicks"] = 100
    if not "grid" in data:
        data["grid"] = True
    if not "trace" in data:
        data["trace"] = True
    if not "seed" in data:
        data["seed"] = 0
    if not "refresh" in data:
        data["refresh"] = 1
    if not "nbParticles" in data:
        data["nbParticles"] = 10
    if not "autoquit" in data:
        data["autoquit"] = False
    if not "profile" in data:
        data["profile"] = False
    if not "profileStep" in data:
        data["profileStep"] = 40

if __name__ == '__main__':
    main(Particules)
