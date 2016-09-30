import json
import sys
import random

sys.path.append('../core')
from Core import *
from Environment import *
from KeyListener import *
from SMA import *
from Avatar import *
from Wall import *
from Hunter import *
from View import *
from MapGenerator import *

class Main(Core):
    """docstring for Main"""
    def __init__(self, nbParticles=None):
        super(Main, self).__init__()

    def populate(self):
        self.createWalls()
        self.keyListener = KeyListener(self.window, self.data)
        nbHunters = self.data["nbHunters"]

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

        position = freeCells.pop()
        self.createDefender(position[0], position[1], None)

    def createWalls(self):
        generator = MapGenerator(self.environment);
        generator.generateMap();
        cellMap = generator.cellMap

        for x in range(generator.width):
            for y in range(generator.height):
                if cellMap[x][y] == 1 :
                    wall = Wall(self.environment, x, y, None)
                    self.environment.walllist.append(wall)
                    self.environment.setInCell(x, y, wall)

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

    def createDefender(self, x, y, name):
        agent = Defender(self.environment, x, y, name)
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
            self.data["seed"] = 0
        if not "refresh" in self.data:
            self.data["refresh"] = 1
        if not "autoquit" in self.data:
            self.data["autoquit"] = False
        if not "nbHunters" in self.data:
            self.data["nbHunters"] = 1
        if not "nbDefenders" in self.data:
            self.data["nbDefenders"] = 1
        if not "speedHunter" in self.data:
            self.data["speedHunter"] = 1
        if not "speedAvatar" in self.data:
            self.data["speedAvatar"] = 1
        if not "defenderLife" in self.data or self.data["defenderLife"] <= 0:
            self.data["defenderLife"] = (self.data["gridSizeY"] * self.data["gridSizeX"]) / 5
        if not "birthLimit" in self.data:
            self.data["birthLimit"] = 4
        if not "deathLimit" in self.data:
            self.data["deathLimit"] = 3
        if not "chanceToStartAlive" in self.data:
            self.data["chanceToStartAlive"] = 0.4
        if not "numberOfSteps" in self.data:
            self.data["numberOfSteps"] = 10

if __name__ == '__main__':
    main(Main)
