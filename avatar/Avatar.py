from Agent import *

class Avatar(Agent):
    """docstring for Avatar"""
    def __init__(self, environment, posX, posY, name, keyListener):
        super(Avatar, self).__init__(environment, posX, posY, name)
        self.color = "Purple"
        self.keyListener = keyListener

    def decide(self):
        lastDirectionPressed = self.keyListener.lastDirectionPressed
        self.pasX = 0
        self.pasY = 0
        if lastDirectionPressed == 'Up':
            self.pasY -= 1
        elif lastDirectionPressed == 'Down':
            self.pasY += 1
        if lastDirectionPressed == 'Left':
            self.pasX -= 1
        elif lastDirectionPressed == 'Right':
            self.pasX += 1

    def update(self):
        self.move()
