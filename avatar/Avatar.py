from Agent import *

class Avatar(Agent):
    """docstring for Avatar"""
    def __init__(self, environment, posX, posY, name, keyListener):
        super(Avatar, self).__init__(environment, posX, posY, name)
        self.color = "Purple"
        self.keyListener = keyListener

    def decide(self):
        print(self.keyListener.lastDirPressed)

    def update(self):
        pass
