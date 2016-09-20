from tkinter import *

class KeyListener(object):
    """docstring for KeyListener"""
    def __init__(self, window):
        super(KeyListener, self).__init__()
        window.bind("<Key>", self.onKeyPressed)
        self.lastDirPressed = None

    def onKeyPressed(self, event):
        lastKeyPressed = event.char
        if lastKeyPressed == "Up" or lastKeyPressed == "Down" or lastKeyPressed == "Left" or lastKeyPressed == "Right" :
            self.lastDirPressed
