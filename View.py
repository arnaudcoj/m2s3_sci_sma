from Observer import *
from tkinter import *

class View(Observer):
    """docstring for View"""
    def __init__(self, canvas, gridSizeX, gridSizeY, boxSize, grid, refresh):
        super(View, self).__init__()
        self.canvas = canvas
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY
        self.boxSize = boxSize
        self.grid = grid
        self.refresh = 60

    def onReceive(self, signal, emitter):
        if signal == "modelUpdated":
            #emitter.environment.printASCII()
            self.draw(emitter.environment.grid)

    def draw(self, environment):
        if environment:
            self.canvas.delete("all")
            for j in range(len(environment)):
                for i in range(len(environment[j])):
                    '''grid'''
                    if self.grid:
                        self.canvas.create_rectangle(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize)

                    '''marble'''
                    if environment[j][i]:
                        self.canvas.create_oval(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize, fill = 'blue', width = 0)