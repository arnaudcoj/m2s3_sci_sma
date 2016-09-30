from tkinter import *

class KeyListener(object):
    """docstring for KeyListener"""
    def __init__(self, window, data):
        super(KeyListener, self).__init__()
        window.bind("<Up>", self.onDirectionPressed)
        window.bind("<Down>", self.onDirectionPressed)
        window.bind("<Left>", self.onDirectionPressed)
        window.bind("<Right>", self.onDirectionPressed)
        window.bind("a", self.onHunterAccelerate)
        window.bind("z", self.onHunterDecelerate)
        window.bind("o", self.onAvatarAccelerate)
        window.bind("p", self.onAvatarDecelerate)
        window.bind("w", self.onSimulationAccelerate)
        window.bind("x", self.onSimulationDecelerate)
        window.bind("<space>", self.onStartPressed)
        self.lastDirectionPressed = None
        self.data = data

    def onDirectionPressed(self, event):
        self.lastDirectionPressed = event.keysym
        print(event.keysym)

    def onHunterAccelerate(self, event):
        print(event.keysym)
        if self.data["speedHunter"]:
            self.data["speedHunter"] = max(1, self.data["speedHunter"] - 1)
            print("Hunter accelerated. Tick(s) before update =", self.data["speedHunter"])

    def onHunterDecelerate(self, event):
        print(event.keysym)
        if self.data["speedHunter"]:
            self.data["speedHunter"] = self.data["speedHunter"] + 1
            print("Hunter decelerated. Tick(s) before update =", self.data["speedHunter"])

    def onAvatarAccelerate(self, event):
        print(event.keysym)
        if self.data["speedAvatar"]:
            self.data["speedAvatar"] = max(1, self.data["speedAvatar"] - 1)
            print("Avatar accelerated. Tick(s) before update =", self.data["speedAvatar"])

    def onAvatarDecelerate(self, event):
        print(event.keysym)
        if self.data["speedAvatar"]:
            self.data["speedAvatar"] = self.data["speedAvatar"] + 1
            print("Avatar decelerated. Tick(s) before update =", self.data["speedAvatar"])

    def onSimulationAccelerate(self, event):
        if self.data["delay"]:
            self.data["delay"] = max(10, self.data["delay"] - 100)
            print("Simulation accelerated. Delay =", self.data["delay"], "ms")

    def onSimulationDecelerate(self, event):
        if self.data["delay"]:
            self.data["delay"] = self.data["delay"] + 100
            print("Simulation decelerated. Delay =", self.data["delay"], "ms")

    def onStartPressed(self, event):
        print(event.keysym)
        pass
