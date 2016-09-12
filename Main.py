import json
import sys
import random

from Environment import *
from SMA import *
from Agent import *
from View import *

class Main(object):
    """docstring for Main"""
    def __init__(self, nbParticles=None):
        super(Main, self).__init__()
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
        agent = Agent(self.environment, x, y, name, data["torus"], data["trace"])
        agentlist.append(agent)
        self.environment.setInCell(x, y, agent)
        if data["trace"]:
            agent.printTrace()

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
        print("its k", data)
    finally:
        dataFile.close()

def setDefaultProperties():
    if not "gridSizeX" in data:
        data["gridSizeX"] = 10
    if not "gridSizeY" in data:
        data["gridSizeY"] = 10
    if not "torus" in data:
        data["torus"] = True
    if not "canvasSizeX" in data:
        data["canvasSizeX"] = 800
    if not "canvasSizeY" in data:
        data["canvasSizeY"] = 800
    if not "boxSize" in data:
        data["boxSize"] = 0
    if not "delay" in data:
        data["delay"] = 500
    if not "scheduling" in data:
        data["scheduling"] = "sequential"
    if not "nbTicks" in data:
        data["nbTicks"] = 20
    if not "grid" in data:
        data["grid"] = True
    if not "trace" in data:
        data["trace"] = True
    if not "seed" in data:
        data["seed"] = 0
    if not "refresh" in data:
        data["refresh"] = 1
    if not "nbParticles" in data:
        data["nbParticles"] = 15
    if not "autoquit" in data:
        data["autoquit"] = False
    if not "profile" in data:
        data["profile"] = False
    if not "profileStep" in data:
        data["profileStep"] = 40

def main():
    global data
    data = dict()
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        print(fileName)
        loadPropertiesFromJSON(fileName)
        print(data)
    setDefaultProperties()
    if data["profile"]:
        profile()
    else:
        run()

def profile():
    nbParticles = data["nbParticles"]
    profileStep = data["profileStep"]
    for i in range(0, nbParticles +1, int(nbParticles / profileStep)):
        startTime = time.clock()
        main = Main(nbParticles=i)
        main.run()
        endTime = time.clock()
        executionTime = endTime - startTime
        print("%d,%5f" % (i, executionTime))

def run():
    main = Main()
    main.run()

if __name__ == '__main__':
    main()
