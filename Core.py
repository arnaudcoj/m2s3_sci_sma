import json
import sys
import random

from Environment import *
from SMA import *
from Particle import *
from View import *

class Core(object):
    """docstring for Core"""
    def __init__(self, nbParticles=None):
        super(Core, self).__init__()

        self.data = dict()
        if len(sys.argv) > 1:
            fileName = sys.argv[1]
            self.loadPropertiesFromJSON(fileName)
        self.setDefaultProperties()

        self.delay = self.data["delay"]
        if nbParticles != None:
            self.data["nbParticles"] = nbParticles
        self.createEnvironment()
        agentlist = []
        self.populate(agentlist)
        self.createSMA(agentlist)
        self.createWindow()
        self.createView()

    def loadPropertiesFromJSON(self, fileName):
        dataFile = open(fileName, 'r')
        try:
            self.data = json.loads(dataFile.read())
        finally:
            dataFile.close()

    def setDefaultProperties(self):
        raise NotImplementedError("Core.setDefaultProperties to be implemented")

    def createEnvironment(self):
        gridSizeX = self.data["gridSizeX"]
        gridSizeY = self.data["gridSizeY"]
        torus = self.data["torus"]

        self.environment = Environment(gridSizeX, gridSizeY, torus)

    def populate(self, agentlist):
        raise NotImplementedError("Core.populate needs to be implemented")

    def createSMA(self, agentlist):
        scheduling = self.data["scheduling"]
        nbTicks = self.data["nbTicks"]
        trace = self.data["trace"]

        self.SMA = SMA(self.environment, agentlist, scheduling, nbTicks, trace)

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
        self.SMA.addObserver(self.view)

    def run(self):
        self.SMA.emitSignal("modelCreated")
        self.window.after(self.delay, self.update)
        self.window.mainloop()

    def update(self):
        if self.SMA.hasFinished() and (self.data["profile"] or self.data["autoquit"]):
            self.SMA.emitSignal("finished")
        else:
            self.SMA.run()
            self.window.after(self.delay, self.update)

def runSystem(systemType):
    system = systemType()
    system.run()

#def profileSystem(systemType):
#    nbParticles = self.data["nbParticles"]
#    profileStep = self.data["profileStep"]
#    nbTicks = self.data["nbTicks"]
#    for i in range(0, nbParticles +1, int(nbParticles / profileStep)):
#        startTime = time.clock()
#        system = systemType(nbParticles=i)
#        system.main()
#        endTime = time.clock()
#        executionTime = endTime - startTime
#        tps = nbTicks / executionTime
#        print("%d,%f" % (i, tps))


def main(systemType):
#    if "profile" in data and self.data["profile"]:
#        profileSystem(systemType)
#    else:
#        runSystem(systemType)
    runSystem(systemType)

if __name__ == '__main__':
    main(Core)
