import json
import sys
import random

sys.path.append('../core')
from Core import *
from Environment import *
from KeyListener import *
from SMA import *
from Avatar import *
from Hunter import *
from View import *

class Main(Core):
    """docstring for Main"""
    def __init__(self, nbParticles=None):
        super(Main, self).__init__()

    def populate(self):
        self.keyListener = KeyListener(self.window)
        nbHunters = 4

        #Fetch the free cells from the environment
        freeCells = self.environment.getFreeCells()

        #Shuffle the list
        random.shuffle(freeCells)

        ###PLACING AVATAR
        position = freeCells.pop()
        avatar = self.createAvatar(position[0], position[1], None)

        ###PLACING HUNTERS
        #Check if there are enough cells for each particle
        if len(freeCells) < nbHunters :
            print("Error ! There are more particles than free cells !")
            return

        for i in range(nbHunters):
            #creates the hunters
            position = freeCells.pop()
            hunter = self.createHunter(position[0], position[1], None)
            avatar.avatarNotifier.addObserver(hunter.avatarFollower)

        avatar.computeDijkstraMatrix

    def createAvatar(self, x, y, name):
        agent = Avatar(self.environment, x, y, name, self.keyListener)
        self.environment.agentlist.append(agent)
        self.environment.setInCell(x, y, agent)
        return agent

    def createHunter(self, x, y, name):
        agent = Hunter(self.environment, x, y, name)
        self.environment.agentlist.append(agent)
        self.environment.setInCell(x, y, agent)
        return agent

    def update(self):
        super().update()
        self.keyListener.canBeCleared = True

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
            self.data["delay"] = 100
        if not "scheduling" in self.data:
            self.data["scheduling"] = "sequential"
        if not "nbTicks" in self.data:
            self.data["nbTicks"] = 0
        if not "grid" in self.data:
            self.data["grid"] = True
        if not "trace" in self.data:
            self.data["trace"] = True
        if not "seed" in self.data:
            self.data["seed"] = "toto"
        if not "refresh" in self.data:
            self.data["refresh"] = 1
        if not "autoquit" in self.data:
            self.data["autoquit"] = False

if __name__ == '__main__':
    main(Main)
