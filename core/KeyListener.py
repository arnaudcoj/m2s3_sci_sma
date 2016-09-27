from tkinter import *

class KeyListener(object):
    """docstring for KeyListener"""
    def __init__(self, window):
        super(KeyListener, self).__init__()
        window.bind("<Up>", self.onUDPressed)
        window.bind("<Down>", self.onUDPressed)
        window.bind("<Left>", self.onLRPressed)
        window.bind("<Right>", self.onLRPressed)
        self.UDPressed = None
        self.LRPressed = None
        self.canBeCleared = False

    def onUDPressed(self, event):
        if self.canBeCleared:
            self.clear()
        self.UDPressed = event.keysym
        print(event.keysym)

    def onLRPressed(self, event):
        if self.canBeCleared:
            self.clear()
        self.LRPressed = event.keysym
        print(event.keysym)

    def clear(self):
        self.UDPressed = None
        self.LRPressed = None
        self.canBeCleared = False
