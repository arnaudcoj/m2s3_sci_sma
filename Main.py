import json
import sys
import random

from Environment import *
from SMA import *
from Agent import *
from View import *

class Main(object):
    """docstring for Main"""
    def __init__(self, fileName):
        super(Main, self).__init__()
        self.loadPropertiesFromJSON(fileName)
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
            print("Properties from", fileName, "successfully loaded.")


        self.delay = self.data["delay"]

    def createEnvironment(self):
        gridSizeX = self.data["gridSizeX"]
        gridSizeY = self.data["gridSizeY"]
        torus = self.data["torus"]

        self.environment = Environment(gridSizeX, gridSizeY, torus)

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
            self.createAgent(agentlist, position[0], position[1])
            print("added particle", i, "on", nbParticles, "to position", position)

        print(nbParticles, "particles have been created and placed on the grid with the seed :", seed)

    def createAgent(self, agentlist, x, y):
        agent = Agent(self.environment, x, y, "Yellow", self.data["torus"])
        agentlist.append(agent)
        self.environment.setInCell(x, y, agent)

    def createSMA(self, agentlist):
        scheduling = self.data["scheduling"]
        nbTicks = self.data["nbTicks"]
        trace = self.data["trace"]

        self.SMA = SMA(self.environment, agentlist, scheduling, nbTicks, trace)

    def createWindow(self):
        self.window = Tk()
        self.window.title("S.M.A")
        self.canvas = Canvas(self.window, width = self.data["canvasSizeX"], height = self.data["canvasSizeX"], background = 'yellow', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()

    def createView(self):
        self.view = View(self.window, self.canvas, self.data["gridSizeX"], self.data["gridSizeY"], self.data["boxSize"], self.data["grid"], self.data["refresh"])
        self.SMA.addObserver(self.view)

    def run(self):
        self.SMA.emitSignal("modelUpdated")
        self.window.after(self.delay, self.update)
        self.window.mainloop()

    def update(self):
        self.SMA.run()
        if not self.SMA.hasFinished():
            self.window.after(self.delay, self.update)


def main():
    main = Main("properties.json")
    main.run()

if __name__ == '__main__':
    main()
