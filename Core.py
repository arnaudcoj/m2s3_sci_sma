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
        self.delay = data["delay"]
        if nbParticles != None:
            data["nbParticles"] = nbParticles
        self.createEnvironment()
        agentlist = []
        self.populate(agentlist)
        self.createSMA(agentlist)
        self.createWindow()
        self.createView()

    def createEnvironment(self):
        gridSizeX = data["gridSizeX"]
        gridSizeY = data["gridSizeY"]
        torus = data["torus"]

        self.environment = Environment(gridSizeX, gridSizeY, torus)

    def populate(self, agentlist):
        raise NotImplementedError("Core.populate needs to be implemented")

    def createSMA(self, agentlist):
        scheduling = data["scheduling"]
        nbTicks = data["nbTicks"]
        trace = data["trace"]

        self.SMA = SMA(self.environment, agentlist, scheduling, nbTicks, trace)

    def createWindow(self):
        self.window = Tk()
        self.window.title("S.M.A")
        self.canvas = Canvas(self.window, width = data["canvasSizeX"] + 1, height = data["canvasSizeY"] + 1, background = 'white', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()

    def createView(self):
        boxSize = data["boxSize"]

        if boxSize == 0 :
            boxSize = min(data["canvasSizeX"], data["canvasSizeY"]) / max(data["gridSizeY"], data["gridSizeX"])

        self.view = View(self.window, self.canvas, data["gridSizeX"], data["gridSizeY"], boxSize, data["grid"], data["refresh"])
        self.SMA.addObserver(self.view)

    def run(self):
        self.SMA.emitSignal("modelCreated")
        self.window.after(self.delay, self.update)
        self.window.mainloop()

    def update(self):
        if self.SMA.hasFinished() and (data["profile"] or data["autoquit"]):
            self.SMA.emitSignal("finished")
        else:
            self.SMA.run()
            self.window.after(self.delay, self.update)

def loadPropertiesFromJSON(fileName):
    global data
    dataFile = open(fileName, 'r')
    try:
        data = json.loads(dataFile.read())
    finally:
        dataFile.close()

def setDefaultProperties():
    raise NotImplementedError("Core.setDefaultProperties to be implemented")

def runSystem(systemType):
    system = systemType()
    system.run()

def profileSystem(systemType):
    nbParticles = data["nbParticles"]
    profileStep = data["profileStep"]
    nbTicks = data["nbTicks"]
    for i in range(0, nbParticles +1, int(nbParticles / profileStep)):
        startTime = time.clock()
        system = systemType(nbParticles=i)
        system.main()
        endTime = time.clock()
        executionTime = endTime - startTime
        tps = nbTicks / executionTime
        print("%d,%f" % (i, tps))


def main(systemType):
    global data
    data = dict()
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        loadPropertiesFromJSON(fileName)
    setDefaultProperties()
    if data["profile"]:
        profileSystem(systemType)
    else:
        runSystem(systemType)

if __name__ == '__main__':
    main(Core)
