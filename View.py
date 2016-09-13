from Observer import *
from tkinter import *

class View(Observer):
    """docstring for View"""
    def __init__(self, window, canvas, gridSizeX, gridSizeY, boxSize, grid, refresh):
        super(View, self).__init__()
        self.window = window
        self.canvas = canvas
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY
        self.boxSize = boxSize
        self.grid = grid
        self.refresh = refresh

        self.margin = self.boxSize * 0.2

        self.signalFunc = {"modelCreated":self.onModelCreated,"modelUpdated":self.onModelUpdated,"finished":self.onFinished}

    def onFinished(self, SMA):
        self.canvas.destroy()
        self.window.destroy()

    def onModelCreated(self, SMA):
        self.drawGrid(SMA.environment)
        self.drawParticles(SMA.agentlist)

    def onModelUpdated(self, SMA):
        for particle in self.particleList:
            agent = particle[0]
            oval = particle[1]
            x1 = agent.posX * self.boxSize + self.margin
            y1 = agent.posY * self.boxSize + self.margin
            x2 = (agent.posX + 1) * self.boxSize - self.margin
            y2 = (agent.posY + 1 ) * self.boxSize - self.margin
            self.canvas.coords(oval, x1, y1, x2, y2)

    def drawGrid(self, environment):
        if self.grid:
            if environment:
                for j in range(environment.getNbRow()):
                    for i in range(environment.getNbCol()):
                        self.canvas.create_rectangle(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize, fill = 'white', width = 1)

    def drawParticles(self, agentlist):
        self.particleList = []
        for agent in agentlist:
            x1 = agent.posX * self.boxSize + self.margin
            y1 = agent.posY * self.boxSize + self.margin
            x2 = (agent.posX + 1) * self.boxSize - self.margin
            y2 = (agent.posY + 1 ) * self.boxSize - self.margin
            oval = self.canvas.create_oval(x1, y1, x2, y2, fill = agent.color, width = 0)
            self.particleList.append((agent, oval))
