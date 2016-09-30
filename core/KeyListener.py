from tkinter import *

class KeyListener(object):
    """docstring for KeyListener"""
    def __init__(self, window, data):
        super(KeyListener, self).__init__()
        window.bind("s", self.onPrintSeed)
        window.bind("w", self.onSimulationAccelerate)
        window.bind("x", self.onSimulationDecelerate)
        window.bind("<space>", self.onStartPressed)
        self.lastDirectionPressed = None
        self.data = data

    def onPrintSeed(self, event):
        if "seed" in self.data:
            print("seed=", self.data["seed"])

    def onSimulationAccelerate(self, event):
        if "delay" in self.data:
            self.data["delay"] = max(1, self.data["delay"] - 100)
            print("Simulation accelerated. Delay =", self.data["delay"], "ms")

    def onSimulationDecelerate(self, event):
        if "delay" in self.data:
            self.data["delay"] = self.data["delay"] + 100
            print("Simulation decelerated. Delay =", self.data["delay"], "ms")

    def onStartPressed(self, event):
        if "pause" in self.data:
            self.data["pause"] = not self.data["pause"]
            if self.data["pause"]:
                print("Simulation paused")
            else:
                print("Simulation resumed")
