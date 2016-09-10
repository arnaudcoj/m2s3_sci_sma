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

    def onReceive(self, signal, emitter):
        if signal == "modelUpdated":
            if emitter.tick % self.refresh == 0:
                self.updateParticles()
        elif signal == "modelCreated":
            if self.grid:
                self.drawGrid(emitter.environment)
            self.drawParticles(emitter.agentlist)
        elif signal == "destroy":
            self.window.destroy()

    def drawGrid(self, environment):
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

    def updateParticles(self):
        for particle in self.particleList:
            agent = particle[0]
            oval = particle[1]
            x1 = agent.posX * self.boxSize + self.margin
            y1 = agent.posY * self.boxSize + self.margin
            x2 = (agent.posX + 1) * self.boxSize - self.margin
            y2 = (agent.posY + 1 ) * self.boxSize - self.margin
            self.canvas.coords(oval, x1, y1, x2, y2)
