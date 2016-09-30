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

        self.signalFunc = {"modelCreated":self.onModelCreated,"modelUpdated":self.drawParticles,"finished":self.onFinished}

    def onFinished(self, SMA):
        self.canvas.destroy()
        self.window.destroy()

    def onModelCreated(self, SMA):
        self.drawGrid(SMA.environment)
        self.drawWalls(SMA)
        self.drawParticles(SMA)

    def drawGrid(self, environment):
        if self.grid:
            if environment:
                for j in range(environment.getNbRow()):
                    for i in range(environment.getNbCol()):
                        x1 = i * self.boxSize
                        y1 = j * self.boxSize
                        x2 = (i + 1) * self.boxSize
                        y2 = (j + 1 ) * self.boxSize
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill = 'white', width = 1)

    def drawWalls(self, SMA):
        if SMA.tick % self.refresh == 0:
            self.canvas.delete("wall")
            walllist = SMA.environment.walllist
            for wall in walllist:
                x1 = wall.posX * self.boxSize
                y1 = wall.posY * self.boxSize
                x2 = (wall.posX + 1) * self.boxSize
                y2 = (wall.posY + 1 ) * self.boxSize
                self.canvas.create_rectangle(x1, y1, x2, y2, fill = wall.color, width = 1, tag = "wall")

    def drawParticles(self, SMA):
        #self.particleList = []
        if SMA.tick % self.refresh == 0:
            self.canvas.delete("agent")
            agentlist = SMA.environment.agentlist
            for agent in agentlist:
                x1 = agent.posX * self.boxSize
                y1 = agent.posY * self.boxSize
                x2 = (agent.posX + 1) * self.boxSize
                y2 = (agent.posY + 1 ) * self.boxSize
                self.canvas.create_oval(x1, y1, x2, y2, fill = agent.color, width = 0, tag = "agent")
