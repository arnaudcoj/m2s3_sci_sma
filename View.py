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
                self.draw(emitter.environment)
        elif signal == "modelCreated":
            self.draw(emitter.environment)
        elif signal == "destroy":
            self.window.destroy()

    def draw(self, environment):
        self.canvas.delete("all")
        if environment:
            for j in range(environment.getNbRow()):
                for i in range(environment.getNbCol()):
                    '''grid'''
                    if self.grid:
                        self.canvas.create_rectangle(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize, fill = 'white', width = 1)

                    '''marble'''
                    if environment.grid[i][j]:
                        self.canvas.create_oval(i * self.boxSize + self.margin, j * self.boxSize + self.margin, (i + 1) * self.boxSize - self.margin, (j + 1 ) * self.boxSize - self.margin, fill = environment.grid[i][j].color, width = 0)
