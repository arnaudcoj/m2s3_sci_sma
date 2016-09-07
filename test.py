from tkinter import *
import json
from pprint import pprint

test_model = [[True,False,False,True,False],
              [False,True,False,False,True]]

class View(object):
    def __init__(self, gridSizeX):
        super(View, self).__init__()
        self.window = Tk()

        self.canvasSizeX = 400
        self.canvasSizeY = 400
        self.boxSize = min(self.canvasSizeX, self.canvasSizeY) / max(len(self.model), len(self.model[0]))
        self.grid = True
        self.refresh = 60

        self.canvas = Canvas(self.window, width=self.canvasSizeX, height=self.canvasSizeY, background='white')
        self.canvas.pack()

    def draw(self):
        if self.model:
            for j in range(len(self.model)):
                for i in range(len(self.model[j])):
                    '''grid'''
                    if self.grid:
                        self.canvas.create_rectangle(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize)

                    '''marble'''
                    if self.model[j][i]:
                        self.canvas.create_oval(i * self.boxSize, j * self.boxSize, (i + 1) * self.boxSize, (j + 1 ) * self.boxSize, fill='yellow', width=0)

    def update(model):
        self.model = model


    def update_and_draw(self):
        print("tick")
        #self.update()
        self.draw()
        self.window.after(int(1000 / self.refresh), self.update_and_draw)

    def start(self):
        self.update_and_draw()
        self.window.mainloop()

view = View(test_model)
view.start()

#dataF = open("properties.json").read()
#data = json.loads(dataF)

#pprint(data['gridSizeX'])
