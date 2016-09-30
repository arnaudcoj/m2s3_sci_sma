import json
import sys
import random

from Environment import *
from SMA import *
from Agent import *
from View import *

class Core(object):
    """docstring for Core"""
    def __init__(self):
        super(Core, self).__init__()

        self.data = dict()
        if len(sys.argv) > 1:
            fileName = sys.argv[1]
            self.loadPropertiesFromJSON(fileName)
        self.setDefaultProperties()

        self.initRandom()

    # Initialization methods

    def loadPropertiesFromJSON(self, fileName):
        dataFile = open(fileName, 'r')
        try:
            self.data = json.loads(dataFile.read())
        finally:
            dataFile.close()

    def setDefaultProperties(self):
        raise NotImplementedError("Core.setDefaultProperties to be implemented")

    def initRandom(self):
        seed = self.data["seed"]
        #Check if there is a given seed
        if seed == 0 or seed == "0" :
            #if not, create a random seed
            seed = random.randint(0, sys.maxsize)

        #Initialize the random engine with the seed
        random.seed(seed)


    # Creation methods

    def createSystem(self):
        self.createWindow()
        self.createView()
        self.createModel()
        self.SMA.emitSignal("modelCreated")

    def createModel(self):
        self.createEnvironment()
        self.populate()
        self.createSMA()

    def createEnvironment(self):
        self.environment = Environment(self.data, [], [])

    def populate(self):
        raise NotImplementedError("Core.populate needs to be implemented")

    def createAgent(self, agentType, x, y, name):
        agent = agentType(self.environment, x, y, name)
        self.environment.agentlist.append(agent)
        self.environment.setInCell(x, y, agent)

    def createSMA(self):
        self.SMA = SMA(self.environment, self.data)
        self.SMA.addObserver(self.view)

    def createWindow(self):
        self.window = Tk()
        self.window.title("S.M.A")
        self.canvas = Canvas(self.window, width = self.data["canvasSizeX"] + 1, height = self.data["canvasSizeY"] + 1, background = 'white', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()

    def createView(self):
        boxSize = self.data["boxSize"]

        if boxSize == 0 :
            boxSize = min(self.data["canvasSizeX"], self.data["canvasSizeY"]) / max(self.data["gridSizeY"], self.data["gridSizeX"])

        self.view = View(self.window, self.canvas, self.data["gridSizeX"], self.data["gridSizeY"], boxSize, self.data["grid"], self.data["refresh"])


    #Execution methods

    def run(self):
        delay = self.data["delay"]
        self.createSystem()
        self.window.after(delay, self.update)
        self.window.mainloop()

    #def profile(self):
        #nbTicks = self.data["nbTicks"]
        #nbParticles = self.data["nbParticles"]
        #profileStep = self.data["profileStep"]
        #for i in range(0, nbParticles +1, int(nbParticles / profileStep)):
            #self.data["nbParticles"] = i
            #startTime = time.clock()
            #self.run()
            #endTime = time.clock()
            #executionTime = endTime - startTime
            #tps = nbTicks / executionTime
            #print("%d,%f" % (i, tps))
            #self.clearSystem()

    def update(self):
        delay = self.data["delay"]
        if self.SMA.hasFinished() and self.data["autoquit"]:
            self.SMA.emitSignal("finished")
        else:
            self.SMA.run()
            self.window.after(delay, self.update)

    #Misc

    def clearSystem(self):
        self.environment = None
        self.SMA = None
        self.view = None
        self.agentlist = []
        self.view

def runSystem(systemType):
    system = systemType()
    #if systemType == "Particle" and system.data["profile"]:
     #   system.profile()
    #else:
    system.run()

def main(systemType):
    runSystem(systemType)

if __name__ == '__main__':
    main(Core)
