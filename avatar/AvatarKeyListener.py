from KeyListener import *

class AvatarKeyListener(KeyListener):
    """docstring for AvatarKeyListener"""
    def __init__(self, window, data):
        super(AvatarKeyListener, self).__init__(window, data)
        window.bind("<Up>", self.onDirectionPressed)
        window.bind("<Down>", self.onDirectionPressed)
        window.bind("<Left>", self.onDirectionPressed)
        window.bind("<Right>", self.onDirectionPressed)
        window.bind("a", self.onHunterAccelerate)
        window.bind("z", self.onHunterDecelerate)
        window.bind("o", self.onAvatarAccelerate)
        window.bind("p", self.onAvatarDecelerate)

    def onDirectionPressed(self, event):
        if not "pause" in self.data or not self.data["pause"]:
            self.lastDirectionPressed = event.keysym
            print(event.keysym)

    def onHunterAccelerate(self, event):
        print(event.keysym)
        if "speedHunter" in self.data:
            self.data["speedHunter"] = max(1, self.data["speedHunter"] - 1)
            print("Hunter accelerated. Tick(s) before update =", self.data["speedHunter"])

    def onHunterDecelerate(self, event):
        print(event.keysym)
        if "speedHunter" in self.data:
            self.data["speedHunter"] = self.data["speedHunter"] + 1
            print("Hunter decelerated. Tick(s) before update =", self.data["speedHunter"])

    def onAvatarAccelerate(self, event):
        print(event.keysym)
        if "speedAvatar" in self.data:
            self.data["speedAvatar"] = max(1, self.data["speedAvatar"] - 1)
            print("Avatar accelerated. Tick(s) before update =", self.data["speedAvatar"])

    def onAvatarDecelerate(self, event):
        print(event.keysym)
        if "speedAvatar" in self.data:
            self.data["speedAvatar"] = self.data["speedAvatar"] + 1
            print("Avatar decelerated. Tick(s) before update =", self.data["speedAvatar"])
