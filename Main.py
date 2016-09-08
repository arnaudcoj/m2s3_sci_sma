import json

from Environment import *
from SMA import *
#from Agent import *

class Main(object):
    """docstring for Main"""
    def __init__(self, fileName):
        super(Main, self).__init__()
        self.loadPropertiesFromJSON(fileName)
        self.createEnvironment()
        agentlist = []
        self.populate(agentlist)
        self.createSMA(agentlist)

    def loadPropertiesFromJSON(self, fileName):
        dataFile = open(fileName, 'r')
        try:
            self.data = json.loads(dataFile.read())
        finally:
            dataFile.close()
            print("Properties from", fileName, "successfully loaded.")

    def createEnvironment(self):
        gridSizeX = self.data["gridSizeX"]
        gridSizeY = self.data["gridSizeY"]
        torus = self.data["torus"]

        self.environment = Environment(gridSizeX, gridSizeY, torus)

    def populate(self, agentlist):
        seed = self.data["seed"]
        nbParticles = self.data["nbParticles"]

        self.createAgent(agentlist, 0, 1)
        self.createAgent(agentlist, 2, 2)

        print(nbParticles, "particles have been created and placed on the grid with the seed :", seed)

    def createAgent(self, agentlist, x, y):
        agent = x + y
        agentlist.append(agent)
        self.environment.setInCell(x, y, agent)

    def createSMA(self, agentlist):
        delay = self.data["delay"]
        scheduling = self.data["scheduling"]
        nbTicks = self.data["nbTicks"]
        trace = self.data["trace"]

        self.SMA = SMA(self.environment, agentlist, delay, scheduling, nbTicks, trace)

    def run(self):
        self.SMA.run()

def main():
    main = Main("properties.json")
    main.run()

if __name__ == '__main__':
    main()
