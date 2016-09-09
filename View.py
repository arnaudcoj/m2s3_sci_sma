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
        self.refresh = 60

        self.margin = self.boxSize * 0.2

    def onReceive(self, signal, emitter):
        if signal == "modelUpdated":
            self.draw(emitter.environment.grid)

    def draw(self, environment):
        self.canvas.delete("all")
        if environment:
            for j in range(len(environment)):
                for i in range(len(environment[j])):
                    '''grid'''
                    if self.grid:
                        self.canvas.create_rectangle(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize)

                    '''marble'''
                    if environment[j][i]:
                        self.canvas.create_oval(i * self.boxSize + self.margin, j * self.boxSize + self.margin, (i + 1) * self.boxSize - self.margin, (j + 1 ) * self.boxSize - self.margin, fill = 'blue', width = 0)
        self.window.update_idletasks()
        self.window.update()