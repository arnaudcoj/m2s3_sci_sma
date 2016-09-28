from tkinter import *

class KeyListener(object):
    """docstring for KeyListener"""
    def __init__(self, window):
        super(KeyListener, self).__init__()
        window.bind("<Up>", self.onDirectionPressed)
        window.bind("<Down>", self.onDirectionPressed)
        window.bind("<Left>", self.onDirectionPressed)
        window.bind("<Right>", self.onDirectionPressed)
        self.lastDirectionPressed = None

    def onDirectionPressed(self, event):
        self.lastDirectionPressed = event.keysym
        print(event.keysym)

    def onHunterAccelerate(self):
        pass

    def onHunterDecelerate(self):
        pass

    def onAvatarAccelerate(self):
        pass

    def onAvatarDecelerate(self):
        pass

    def onSimulationAccelerate(self):
        pass

    def onSimulationDecelerate(self):
        pass

    def onStartPressed(self):
        pass
