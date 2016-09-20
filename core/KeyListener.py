from tkinter import *

class KeyListener(object):
    """docstring for KeyListener"""
    def __init__(self, window):
        super(KeyListener, self).__init__()
        window.bind("<Up>", self.onKeyPressed)
        window.bind("<Down>", self.onKeyPressed)
        window.bind("<Left>", self.onKeyPressed)
        window.bind("<Right>", self.onKeyPressed)
        self.lastDirPressed = []
        self.canBeCleared = False

    def onKeyPressed(self, event):
        if self.canBeCleared:
            self.clear()
        self.lastDirPressed.append(event.keysym)
        print(event.keysym)

    def clear(self):
        self.lastDirPressed.clear()
        self.canBeCleared = False
