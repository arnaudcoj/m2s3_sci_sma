from Agent import *

class Avatar(Agent):
    """docstring for Avatar"""
    def __init__(self, environment, posX, posY, name, keyListener):
        super(Avatar, self).__init__(environment, posX, posY, name)
        self.color = "Purple"
        self.keyListener = keyListener

    def decide(self):
        keysPressed = self.keyListener.lastDirPressed
        self.pasX = 0
        self.pasY = 0
        if 'Up' in keysPressed:
            self.pasY -= 1
        if 'Down' in keysPressed:
            self.pasY += 1
        if 'Left' in keysPressed:
            self.pasX -= 1
        if 'Right' in keysPressed:
            self.pasX += 1

    def update(self):
        self.move()
